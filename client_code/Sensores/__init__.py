from ._anvil_designer import SensoresTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Sensores(SensoresTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = [{
      "id":1,
      "name": "Temperatura 1",
      "limit": 30,
      "url": "https://www.paresteck.com.br/5400-large_default/arduino-sensor-de-temperatura-e-umidade-dht11.jpg"
    },{
      "id":2,
      "name": "Temperatura 2",
      "limit": 5,
      "url": "https://www.paresteck.com.br/5400-large_default/arduino-sensor-de-temperatura-e-umidade-dht11.jpg"
    }]

    # Any code you write here will run when the form opens.
    
