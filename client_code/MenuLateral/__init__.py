from ._anvil_designer import MenuLateralTemplate
from anvil import *
import anvil.server
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import functions

from anvil.js.window import localStorage, sessionStorage

class MenuLateral(MenuLateralTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('DashBoard')

  def button_2_click(self, **event_args):
    open_form('Usuarios')
    
  def button_3_click(self, **event_args):
    open_form('Sensores')
  
  def button_4_click(self, **event_args):
    open_form('Grupos')
    
  def validate_session(self, **event_args):
    validate = functions.validate_session_and_group("Admin")
    
    if(validate["logged"] == False):
      open_form('Login')
    else:
      self.button_2.visible = validate['in_group']
      self.button_4.visible = validate['in_group']
    

  def button_5_click(self, **event_args):
    localStorage.setItem('access_token', None)
    open_form('Login')






