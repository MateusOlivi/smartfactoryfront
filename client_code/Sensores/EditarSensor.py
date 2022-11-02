from ._anvil_designer import EditarSensorTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EditarSensor(EditarSensorTemplate):
  def __init__(self, properties):
    self.sensor = properties['item']
    
    self.repeating_panel_1.items = properties['item']['info']
    # Set Form properties and Data Bindings. 
    self.init_components(**properties)
    
    
#     self.text_id.text = properties["item"]["id"]
#     self.text_name.text = properties["item"]["name"]
#     self.text_limit.text = properties["item"]["limit_value"]
#     self.text_located_at.text = properties["item"]['located_at']
#     # Any code you write here will run when the form opens.

  def apply_button_click(self, **event_args):
    sensor_id = self.sensor["sensor_id"]
    located_at = self.text_located_at.text
    
    if(located_at == ""):
      located_at = None
    
    patch_json = {
      "located_at": located_at
    }
    
    for item in self.repeating_panel_1.items:
      if("info" not in patch_json.keys()):
        patch_json["info"] = []
        
      patch_json["info"].append({
        "type":item["type"],
        "upper_limit": item["upper_limit"],
        "bottom_limit": item["bottom_limit"]
      })
    
    print(patch_json)


