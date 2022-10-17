from ._anvil_designer import UserTemplateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EditGroups import EditGroups
from anvil.js.window import localStorage, sessionStorage
from ... import routes

class UserTemplate(UserTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def clicar_grupos(self, **event_args):
    my_token = localStorage.get("access_token")
    current_user_id = self.item["id"]
    
    groups = routes.getGroups(my_token)
    user_groups = routes.getGroups(my_token, user_id = current_user_id)
    user_groups_names = [group["name"] for group in user_groups["groups"]]
        
    group_form = EditGroups()
    group_form.repeating_panel_1.items = [{
      "group": group["name"],
      "in_group": group["name"] in user_groups_names
    } for group in groups["groups"]]
    
    alert(content=group_form, title="EditarGrupos")
    
    print(group_form.repeating_panel_1.items)
    

