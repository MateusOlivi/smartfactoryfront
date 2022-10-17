from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import localStorage, sessionStorage
from .. import routes
from .. import functions

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
      return
      
    token = routes.authUser(username, password)
    
    if(token == False):
      self.message_label.text = "Usuário/Senha incorreto"
    else:
      localStorage.setItem('access_token', token["access_token"])
      open_form('DashBoard_V2')
            
  def verify_session(self, **event_args):
      valid_session = functions.validate_session()
      
      if(valid_session != False):
        print("User already logged in")
        open_form('DashBoard_V2')



