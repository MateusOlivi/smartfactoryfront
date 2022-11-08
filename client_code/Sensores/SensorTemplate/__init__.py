from ._anvil_designer import SensorTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SensorTemplate(SensorTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def edit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Sensores.EditarSensor', {"item": self.item})
    

  def dashboard_button_click(self, **event_args):
    open_form('DashBoard', sensor_id = self.item["sensor_id"])


