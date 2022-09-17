import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import random
#import psycopg2 
import anvil.http
import random
  
@anvil.server.callable
def get_temp_history():
    
    my_history = []
    for i in range(1,10):
      my_history.extend([{'time':f'2022-09-{i}T{j}:00:00', 'temperature': random.uniform(20,27)} for j in range(1, 24)])
    
    return my_history

@anvil.server.callable
def get_limite():
  return { "Limite": 25 }

@anvil.server.callable
def get_users():
  return [
    { 
      "id": '1',
      "nome": "Exemplo 1",
      "email": "Exemplo1@gmail.com",
      "acesso": "Admin"
    },
    { 
      "id": '2',
      "nome": "Exemplo 2",
      "email": "Exemplo2@gmail.com",
      "acesso": "User"
    },
    { 
      "id": '3',
      "nome": "Exemplo 3",
      "email": "Exemplo3@gmail.com",
      "acesso": "User"
    }
  ] 
    
@anvil.server.callable
def set_limite(my_limit):
  pass

  
  