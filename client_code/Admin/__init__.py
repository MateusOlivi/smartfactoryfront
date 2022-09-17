from ._anvil_designer import AdminTemplate
from .. import routes

class Admin(AdminTemplate):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.painel.items = routes.get_users()
    self.get_limit()
  
  def get_limit(self):
    my_data = routes.get_limite()
    my_limit = my_data["Limite"]
    
    self.limit.text = my_limit
    
  def button_aplicar(self, **event_args):
    my_limit = int(self.limit.text)
    
    routes.set_limite()
    from datetime import datetime

    print(datetime.now())
    print(self.painel.items)
    




