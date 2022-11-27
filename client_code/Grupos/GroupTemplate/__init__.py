from ._anvil_designer import GroupTemplateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..SensorsList import SensorsList

from anvil.js.window import localStorage, sessionStorage
from ... import routes


class GroupTemplate(GroupTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    if(self.item["group_name"] == "Admin"):
      self.delete_button.enabled = False
      self.sensors_button.enabled = False
    # Any code you write here will run when the form opens.

  def delete_button_click(self, **event_args):
    my_token = localStorage.get("access_token")
    deleted = routes.deleteGroup(my_token, self.item["group_id"])
    
    if(deleted == False):
      alert(content="Houve um problema ao deletar o grupo", title="Grupo não deletado", large=True)
    else:
      sensors = routes.getSensors(my_token)
      
      for sensor in sensors:
        if(self.item["group_name"] in sensor["groups"]):
          routes.removeGroupSensor(my_token, sensor["sensor_id"],self.item["group_name"])
          
      alert(content="Grupo Deletado!", title="Grupo deletado", large=False)
      open_form('Grupos')

  def sensors_button_click(self, **event_args):
    my_token = localStorage.get("access_token")
    
    sensors = routes.getSensors(my_token)
            
    sensors_form = SensorsList()
    
    sensors_form.repeating_panel_1.items = [{
      "sensor_name": sensor["name"],
      "in_group": self.item["group_name"] in sensor["groups"],
      "sensor_id": sensor["sensor_id"],
    } for sensor in sensors]
    
    participating = [sensor["name"] for sensor in sensors if self.item["group_name"] in sensor["groups"]]
    
    result = alert(content=sensors_form, title="Sensores permitidos", large = True)
    
    if(result == None):
      return 
    
    items = (sensors_form.repeating_panel_1.items)

    added_list = [item["sensor_id"] for item in items if item['in_group'] == True and item['sensor_name'] not in participating]
    removed_list = [item["sensor_id"] for item in items if item['in_group'] == False and item['sensor_name'] in participating]
    
    success = True
    for sensor_id in added_list:
      success = success and routes.addGroupSensor(my_token, sensor_id,self.item["group_name"])
    
    for sensor_id in removed_list:
      success = success and routes.removeGroupSensor(my_token, sensor_id,self.item["group_name"])
    