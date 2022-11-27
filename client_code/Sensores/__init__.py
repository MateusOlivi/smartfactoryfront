from ._anvil_designer import SensoresTemplate
from anvil import *
import anvil.server

from anvil.js.window import localStorage, sessionStorage
from .. import routes

class Sensores(SensoresTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = self.get_sensors_data()
    
  def get_sensors_data(self):      
    my_token = localStorage.get("access_token")
    sensor_list = routes.getSensors(my_token)
    
    if(sensor_list == False):
      return []
    
    return sensor_list
    
  