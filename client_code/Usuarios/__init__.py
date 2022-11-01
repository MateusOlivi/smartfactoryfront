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
    my_token = localStorage.get("access_token")
    create_user_form = CreateUser()
    
    result = alert(content=create_user_form, title="Criar Usuario", large=True)
    
    if(result == None):
      return 
    
    username = create_user_form.username_box.text
    firstname = create_user_form.firstname_box.text
    lastname = create_user_form.lastname_box.text
    email = create_user_form.email_box.text
    password = create_user_form.password_box.text
  
    payload = {
      "username": username,
      "email": email,
      "firstName": firstname ,
      "lastName": lastname,
      "password": password
    }
    
    created = routes.createUser(my_token, payload)
    
    if(created == False):
      alert(content="Houve um problema ao criar o usuario, verifique usuario/email já existe", title="Usuario não criado", large=True)
    else:
      alert(content="Usuario Criado!", title="Usuario criado", large=False)
      self.painel.items = self.users_list()
