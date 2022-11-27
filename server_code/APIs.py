import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import random
#import psycopg2 
import anvil.http
  
@anvil.server.callable
def getTelemetryList(token):
  try:
      url = f"http://localhost:8000/telemetry/list"
      
      headers= {
        "Authorization": token
      }
      
      resp = anvil.http.request(url, method="GET", headers=headers, json=True, data='')
      
      return resp
    
  except:
    return False

@anvil.server.callable
def getSensors(token):
  try:   
      headers= {
        "Authorization": token
      }
      
      resp = anvil.http.request(f"http://localhost:8000/sensors/list", method="GET", headers=headers, json=True, data='')
      
      return resp
    
  except:
    return False

@anvil.server.callable
def getSensor(token, sensor_id):
  try:
      url = f"http://localhost:8000/sensors?sensor_id={sensor_id}"
      
      headers= {
        "Authorization": token
      }
      
      resp = anvil.http.request(url, method="GET", headers=headers, json=True, data='')
      
      return resp
    
  except:
    return False

@anvil.server.callable
def getTelemetry(token, sensor_id):
  try:
      url = f"http://localhost:8000/telemetry?sensor_id={sensor_id}"
      
      headers= {
        "Authorization": token
      }
      
      resp = anvil.http.request(url, method="GET", headers=headers, json=True, data='')
      
      return resp
    
  except:
    return False

  