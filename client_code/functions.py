import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.js.window import localStorage, sessionStorage
from . import routes

def validate_session():
  access_token = localStorage.getItem("access_token")
  
  if(access_token != None):
    return routes.validate_token(access_token)
    
  return False
