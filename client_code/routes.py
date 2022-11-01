import random
import anvil.http
import datetime
import math
import json

### Users ####

def authUser(user, pwd):
  try:
    url = f"http://127.0.0.1:8000/authUser?username={user}&password={pwd}"
    
    resp = anvil.http.request(url, method="GET", json = True, data='')
    return resp
  
  except:
    return False

def validate_token(token):
  try:
    url = "http://127.0.0.1:8000/validate"
    
    headers= {
      "Authorization": token
    }
    
    resp = anvil.http.request(url, method="GET", headers= headers, json=True, data='')    
    
    return resp
  
  except Exception as e:
    return False

def getUserList(token):
  try:
    url = "http://127.0.0.1:8000/user/list/"
    resp = anvil.http.request(url, method="GET", headers={"Authorization": token}, json = True, data='')    
    return resp
  
  except Exception as e:
    return False

def getUserGroups(token, user_id):
  try:
    url = f"http://127.0.0.1:8000/userGroups?user_id={user_id}"
    resp = anvil.http.request(url, method="GET", headers={"Authorization": token}, json = True, data='')    
    return resp
  except Exception as e:
    return False

def getAllGroups(token):
  try:
    resp = anvil.http.request("http://127.0.0.1:8000/groups/list", method="GET", headers={"Authorization": token}, json = True, data='')    
    return resp
  
  except Exception as e:
    return False

def addGroup(token, user_id, group_id_list):
  try:
    payload = json.dumps({
      "user_id": user_id,
      "groups_ids": group_id_list
    })
    
    headers= {
      "content-type": "application/json",
      "Authorization": token
    }
    
    anvil.http.request("http://127.0.0.1:8000/userGroups", method="POST", data = payload, headers=headers)  
    
  except:
    return False

def removeGroup(token, user_id, group_id_list):
  try:   
    payload = json.dumps({
      "user_id": user_id,
      "groups_ids": group_id_list
    })
    
    headers= {
      "content-type": "application/json",
      "Authorization": token
    }
    
    anvil.http.request("http://127.0.0.1:8000/userGroups", method="DELETE", data = payload, headers=headers)    
    return True
  
  except:
    return False

def createUser(token, payload):
  try:   
    payload = json.dumps(payload)
    
    headers= {
      "content-type": "application/json",
      "Authorization": token
    }
    
    anvil.http.request("http://127.0.0.1:8000/user", method="POST", data = payload, headers=headers)    
    return True
  
  except:
    return False

def deleteUser(token, user_id):
  try:   
   
    headers= {
      "Authorization": token
    }
    
    anvil.http.request(f"http://127.0.0.1:8000/user?user_id={user_id}", method="DELETE", headers=headers, data='')
    
    return True
  
  except:
    return False

  
# Sensores

def getSensors(token):
  try:   
      headers= {
        "Authorization": token
      }
      
      resp = anvil.http.request(f"http://127.0.0.1:8000/sensors/list", method="GET", headers=headers, json=True, data='')
      
      return resp
    
  except:
    return False
  
  
  
  
  
  
  
  
  
  
def sensor_builder(sensor_id):
    name_list = ["Temperature", "Humidity", "Potency"]
    locates = ["Room", "Boiler", "Cooler"]

    return {
        "id": sensor_id,
        "name": name_list[random.randint(0,len(name_list)-1)] + f"_{random.randint(0,999)}",
        "located_at": locates[random.randint(0,len(locates)-1)] + f"_{random.randint(0,999)}",
        "limit_value": random.randint(30, 50)
    }

def build_temp_history(sensor_id, n_days):
    base = datetime.datetime.today()
    date_list = [str(base - datetime.timedelta(days=x, hours=y)) for x in range(n_days) for y in range(0,25)]

    temp_history = [{
        "timestamp": date,
        "value": random.uniform(21,25) + 10*math.log10(sensor_id)
    } for date in date_list]
    
    return temp_history

def get_sensors(n):
    return [sensor_builder(i) for i in range(1, n+1)]


def get_history(sensor_id, n_days):
    return build_temp_history(sensor_id, n_days)
  
def get_users():
  return [
    { 
      "id": '1',
      "name": "Exemplo 1",
      "email": "Exemplo1@gmail.com",
      "access": "Admin"
    },
    { 
      "id": '2',
      "name": "Exemplo 2",
      "email": "Exemplo2@gmail.com",
      "access": "User"
    },
    { 
      "id": '3',
      "name": "Exemplo 3",
      "email": "Exemplo3@gmail.com",
      "access": "User"
    }
  ] 
    
def set_limite(my_limit):
  pass

  
  