from ._anvil_designer import SensoresTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil.js.window import localStorage, sessionStorage
from .. import routes

class Sensores(SensoresTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = self.sensor_list()
    
  def sensor_list(self):
    my_token = localStorage.get("access_token")
    sensors = routes.getSensors(my_token)
    
    if(sensors == False):
      return []
    
    return sensors
    
    # Any code you write here will run when the form opens.
  

