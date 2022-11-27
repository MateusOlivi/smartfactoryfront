import anvil.server
import random
import anvil.http
import datetime
import math
import json

### Users ####

def authUser(user, pwd):
  try:
    url = f"http://localhost:8000/authUser?username={user}&password={pwd}"
    
    resp = anvil.http.request(url, method="GET", json = True, data='')
    return resp
  
  except:
    return False

def validate_token(token):
  try:
    url = "http://localhost:8000/validate"
    
    headers= {
      "Authorization": token
    }
    
    resp = anvil.http.request(url, method="GET", headers= headers, json=True, data='')    
    
    return resp
  
  except Exception as e:
    return False

def getUserList(token):
  try:
    url = "http://localhost:8000/user/list/"
    resp = anvil.http.request(url, method="GET", headers={"Authorization": token}, json = True, data='')    
    return resp
  
  except Exception as e:
    return False

def getUserGroups(token, user_id):
  try:
    url = f"http://localhost:8000/userGroups?user_id={user_id}"
    resp = anvil.http.request(url, method="GET", headers={"Authorization": token}, json = True, data='')    
    return resp
  except Exception as e:
    return False

def getAllGroups(token):
  try:
    resp = anvil.http.request("http://localhost:8000/groups/list", method="GET", headers={"Authorization": token}, json = True, data='')    
    return resp
  
  except Exception as e:
    return False
  
def createGroup(token, group_name):
  try:
    url = f"http://localhost:8000/groups?group_name={group_name}"
    
    resp = anvil.http.request(url, method="POST", headers={"Authorization": token}, json = True, data='')    
    
    return True
  
  except Exception as e:
    return False

def deleteGroup(token, group_id):
  try:
    url = f"http://localhost:8000/groups?group_id={group_id}"
    
    resp = anvil.http.request(url, method="DELETE", headers={"Authorization": token}, json = True, data='')    
    
    return True
  
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
    
    anvil.http.request("http://localhost:8000/userGroups", method="POST", data = payload, headers=headers)  
    
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
    
    anvil.http.request("http://localhost:8000/userGroups", method="DELETE", data = payload, headers=headers)    
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
    
    anvil.http.request("http://localhost:8000/user", method="POST", data = payload, headers=headers)    
    return True
  
  except:
    return False

def deleteUser(token, user_id):
  try:   
   
    headers= {
      "Authorization": token
    }
    
    anvil.http.request(f"http://localhost:8000/user?user_id={user_id}", method="DELETE", headers=headers, data='')
    
    return True
  
  except:
    return False

  
# Sensores
def getSensors(token):
  try:   
      headers= {
        "Authorization": token
      }
      
      resp = anvil.http.request(f"http://localhost:8000/sensors/list", method="GET", headers=headers, json=True, data='')
      
      return resp
    
  except:
    return False

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
  
def patchSensors(token,sensor_id, patch_json):
  try:
      url = f"http://localhost:8000/sensors?sensor_id={sensor_id}"
      
      headers= {
        "Authorization": token
      }
      
      anvil.http.request(url, method="PATCH", headers=headers, json=True, data = patch_json)
      
      return True
    
  except:
    return False

def addGroupSensor(token,sensor_id, group_name):
  try:
      url = f"http://localhost:8000/sensors/groups?sensor_id={sensor_id}&group_name={group_name}"
      
      headers= {
        "Authorization": token
      }
      
      anvil.http.request(url, method="POST", headers=headers, json=True, data = '')
      
      return True
    
  except:
    return False

def removeGroupSensor(token,sensor_id, group_name):
  try:
      url = f"http://localhost:8000/sensors/groups?sensor_id={sensor_id}&group_name={group_name}"
      
      headers= {
        "Authorization": token
      }
      
      anvil.http.request(url, method="DELETE", headers=headers, json=True, data = '')
      
      return True
    
  except:
    return False

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

  
  