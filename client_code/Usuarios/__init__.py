from ._anvil_designer import UsuariosTemplate
from anvil.js.window import localStorage, sessionStorage

from .. import routes

class Usuarios(UsuariosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.painel.items = routes.get_users()
    self.users_list()
    
  def users_list(self):
    my_token = localStorage.get("access_token")
    print(my_token)
    print(routes.getUserList(my_token))
  def button_aplicar(self, **event_args):
    pass
    




