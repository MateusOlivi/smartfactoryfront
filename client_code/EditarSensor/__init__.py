from ._anvil_designer import EditarSensorTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class EditarSensor(EditarSensorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.text_id.text = properties["item"]["id"]
    self.text_name.text = properties["item"]["name"]
    self.text_limit.text = properties["item"]["limit_value"]
    self.text_located_at.text = properties["item"]['located_at']
    # Any code you write here will run when the form opens.
