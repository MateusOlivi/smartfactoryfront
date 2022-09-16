from ._anvil_designer import MenuLateralTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MenuLateral(MenuLateralTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('DashBoard')

  def button_2_click(self, **event_args):
    open_form('Admin')


