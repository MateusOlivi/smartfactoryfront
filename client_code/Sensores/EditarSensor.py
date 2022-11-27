from ._anvil_designer import EditarSensorTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .. import routes
from anvil.js.window import localStorage, sessionStorage

class EditarSensor(EditarSensorTemplate):
  def __init__(self, properties):
    self.sensor = properties['item']
    
    self.repeating_panel_1.items = properties['item']['info']
    # Set Form properties and Data Bindings. 
    self.init_components(**properties)
    

  def apply_button_click(self, **event_args):
    sensor_id = self.sensor["sensor_id"]
    located_at = self.text_located_at.text
    
    my_token = localStorage.get("access_token")

    if(located_at == ""):
      located_at = None
    
    patch_json = {
      "located_at": located_at
    }
    
    error_list = []
    
    for item in self.repeating_panel_1.items:
      if("info" not in patch_json.keys()):
        patch_json["info"] = []
        
      patch_json["info"].append({
        "type":item["type"],
        "upper_limit": item["upper_limit"],
        "bottom_limit": item["bottom_limit"]
      })
      
      if(item["bottom_limit"] != None and item["upper_limit"] != None and item["bottom_limit"] >= item["upper_limit"]):
        error_list.append(item["type"])
    
    if(len(error_list) == 0):
      success = routes.patchSensors(my_token, sensor_id, patch_json)
      
      if(success):
        alert(content="Os dados do sensor foram atualizados", title="Sucesso", large=True)
        open_form('Sensores')
      else:
        alert(content="Houve um erro ao atualizar os dados do sensor", title="Erro", large=True)
    
    else:
      alert(content="Os limites inferiores estão maiores que os superiores para: " + ", ".join(error_list), title="Erro", large=True)

      
  
  


