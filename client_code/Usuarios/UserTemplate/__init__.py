from ._anvil_designer import UserTemplateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EditGroups import EditGroups
from ... import routes

class UserTemplate(UserTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(self.item)

  def clicar_grupos(self, **event_args):
    group_form = EditGroups()
    
    groups = routes.getGroups()
    print(groups)
    group_form.repeating_panel_1.items = [{
      "group": 1,
      "in_group": 2
    }]
    
    
    alert(content=group_form,
          title="EditarGrupos")
          
    print(f"You entered: {t.text}")
    pass

