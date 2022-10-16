from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def enter_button(self, **event_args):
    username = self.user_box.text
    password = self.pwd_box.text
    
    if(len(username) == 0 or len(password) == 0):
      self.message_label.text = "Preencha todos os campos"

    print(username, type(password))
    pass

