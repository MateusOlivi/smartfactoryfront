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
      my_history.extend([{'datetime':f'2022-09-{i}T{j}:00:00', 'temperature': random.uniform(20,27)} for j in range(1, 24)])
    
    return my_history


  
  