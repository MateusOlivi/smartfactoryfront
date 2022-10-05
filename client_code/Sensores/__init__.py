from ._anvil_designer import SensoresTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import routes

class Sensores(SensoresTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = routes.get_sensors(100)

    # Any code you write here will run when the form opens.
  

