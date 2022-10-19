import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import localStorage, sessionStorage
from . import routes

def validate_session():
  access_token = localStorage.getItem("access_token")
  
  if(access_token != None):
    data = routes.validate_token(access_token)
    is_valid = data["is_valid"]

    if(is_valid != False):
      return data
    
  return False

def validate_session_and_group(desired_group):
  my_data = validate_session()
  
  logged = False
  in_group = False
  
  if(my_data != False):
    logged = True
    
    my_groups = [group["name"] for group in my_data["groups"]]
    
    if(desired_group in my_groups):
      in_group = True
  
  return {
    "in_group": in_group,
    "logged": logged
  }
    
  