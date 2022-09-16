from ._anvil_designer import AdminTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.get_limit()
  
  def get_limit(self):
    my_data = anvil.server.call('get_limite')
    my_limit = list(my_data)[-1]["Limite"]
    
    self.limit.text = my_limit
    
    
  def button_1_click(self, **event_args):
    my_limit = int(self.limit.text)
    anvil.server.call('set_limite', my_limit)
    
    



