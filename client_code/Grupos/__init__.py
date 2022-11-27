from ._anvil_designer import GruposTemplate
from anvil.js.window import localStorage, sessionStorage
from anvil import *
import anvil.server

from .. import routes

class Grupos(GruposTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.painel.items = self.group_list()
    
  def group_list(self):
    my_token = localStorage.get("access_token")
    groupList = routes.getAllGroups(my_token)
    
    if(groupList == False):
      return []
    else:
      return [{
        "group_id": group["id"],
        "group_name": group["name"],
      } for group in groupList["groups"]]
      
  def button_create(self, **event_args):
    my_token = localStorage.get("access_token")
    
    if(self.group_name.text != ''):
      created = routes.createGroup(my_token, self.group_name.text)
      
      if(created == False):
        alert(content="Houve um problema ao criar o grupo, verifique se já não existe um grupo com esse nome", title="Grupo não criado", large=True)
      else:
        alert(content="Grupo Criado!", title="Grupo criado", large=False)

      self.painel.items = self.group_list()

