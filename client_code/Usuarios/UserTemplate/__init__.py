from ._anvil_designer import UserTemplateTemplate
from anvil import *
import anvil.server
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EditGroups import EditGroups
from anvil.js.window import localStorage, sessionStorage
from ... import routes
from .. import Usuarios

class UserTemplate(UserTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def clicar_grupos(self, **event_args):
    my_token = localStorage.get("access_token")
    current_user_id = self.item["id"]
    
    groups = routes.getAllGroups(my_token)
    user_groups = routes.getUserGroups(my_token, user_id = current_user_id)
    user_groups_names = [group["name"] for group in user_groups["groups"]]
        
    group_form = EditGroups()
    group_form.repeating_panel_1.items = [{
      "group": group["name"],
      "in_group": group["name"] in user_groups_names,
      "group_id": group["id"],
    } for group in groups["groups"]]
    
    result = alert(content=group_form, title="Grupos do Usuario")
    
    if(result == None):
      return 
    
    items = (group_form.repeating_panel_1.items)
    
    added = [item["group_id"] for item in items if item['in_group'] == True and item['group'] not in user_groups_names]
    removed = [item["group_id"] for item in items if item['in_group'] == False and item['group'] in user_groups_names]
    
    if(len(added) != 0):
      routes.addGroup(my_token, current_user_id, added)
    if(len(removed) != 0):
      routes.removeGroup(my_token, current_user_id, removed)
      

  def button_delete(self, **event_args):
    my_token = localStorage.get("access_token")
    current_user_id = self.item["id"]
    
    deleted = routes.deleteUser(my_token, current_user_id)

    if(deleted == False):
      alert(content="Houve um problema ao deletar o usuario", title="Usuario não deletado", large=True)
    else:
      alert(content="Usuario Deletado!", title="Usuario deletado", large=False)
      open_form('Usuarios')
    
