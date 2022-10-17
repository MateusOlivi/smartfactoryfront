from ._anvil_designer import SensorTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import functions

class Sensor(SensorTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('EditarSensor', item = self.item)
    pass

  def validate_session(self, **event_args):
    validate = functions.validate_session_and_group("Admin")
    
    if(validate["logged"] == False):
      open_form('Login')
    else:
      self.button_1.enabled = validate['in_group']


