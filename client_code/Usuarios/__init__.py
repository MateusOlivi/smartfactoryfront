from ._anvil_designer import UsuariosTemplate
from .. import routes

class Usuarios(UsuariosTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.painel.items = routes.get_users()
    
  def button_aplicar(self, **event_args):
    pass
    




