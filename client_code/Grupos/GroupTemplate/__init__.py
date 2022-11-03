from ._anvil_designer import GroupTemplateTemplate
from anvil import *
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
    # Any code you write here will run when the form opens.

  def delete_button_click(self, **event_args):
    my_token = localStorage.get("access_token")
    deleted = routes.deleteGroup(my_token, self.item["group_id"])
    
    if(deleted == False):
      alert(content="Houve um problema ao deletar o grupo", title="Grupo não deletado", large=True)
    else:
      alert(content="Grupo Deletado!", title="Grupo deletado", large=False)
      open_form('Grupos')

  def sensors_button_click(self, **event_args):
    my_token = localStorage.get("access_token")
    
    sensors = routes.getSensors(my_token)
    
    #user_groups_names = [group["name"] for group in user_groups["groups"]]
        
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
    
    added = True
    for sensor_id in added_list:
      added = added and routes.addGroupSensor(my_token, sensor_id,self.item["group_name"])
      print("oi")
    print(added)

