from ._anvil_designer import UsuariosTemplate
from anvil.js.window import localStorage, sessionStorage
from anvil import *

from .. import routes
from .CreateUser import CreateUser

class Usuarios(UsuariosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.painel.items = self.users_list()
    
  def users_list(self):
    my_token = localStorage.get("access_token")
    user_list = routes.getUserList(my_token)
    if(user_list == False):
      return []
    else:
      return [{
        "id": user.get("id", None),
        "username": user.get("username", None),
        "name": user.get("firstName", "") + " "+ user.get("lastName", ""),
        "email": user.get("email", None)
      } for user in user_list["users"]]
      
  def button_create(self, **event_args):
    create_user_form = CreateUser()
    
    alert(content=create_user_form, title="Criar Usuario")
    




