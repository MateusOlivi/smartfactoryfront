from ._anvil_designer import DashBoard_V3Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

import anvil.server
from datetime import datetime
from anvil.js.window import localStorage, sessionStorage
from .. import routes

class DashBoard_V3(DashBoard_V3Template):
  def __init__(self, **properties):
    # Preparando atributos
    self.sensor_id = properties.get('item', None)
    self.token = localStorage.get("access_token")

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
        
    self.setItems()
        
  # Any code you write here will run when the form opens.
  def setItems(self):  
    self.sersors = self.prepareSensorList()
    self.telemetry_data = self.prepareTelemetry()
    
    my_items = [{
      "telemetry": data["telemetry"],
      "sensor": data["sensor"]
    } for data in self.telemetry_data.values()]
    
    self.repeating_panel_1.items = my_items
    
  def prepareSensorList(self):
    if(self.sensor_id == None):
      sensor_list = routes.getSensors(self.token)
    else:
      sensor_list = [routes.getSensor(self.token, self.sensor_id)]
    
    return sensor_list

  def prepareTelemetry(self):
    data = {}
    telemetry_data = routes.getTelemetryList(self.token)

    for sensor in self.sersors:
      my_id = sensor["sensor_id"]
      my_telemetry = [tele for tele in telemetry_data if tele["sensor_id"] == my_id]
      
      for telemetry in my_telemetry:
#         if(datetime.timestamp(datetime.now()) - telemetry["inserted_at"]/1000 > 86400):
#           continue
          
        my_type = telemetry["type"]
        
        if((my_id, my_type) not in data.keys()):
          data[(my_id, my_type)] = {}
          data[(my_id, my_type)]["telemetry"] = []
          data[(my_id, my_type)]["sensor"] = sensor
          
        data[(my_id, my_type)]["telemetry"].append(telemetry)
    
    return data

#   def timer_1_tick(self, **event_args):
#     with anvil.server.no_loading_indicator:
#       print("oi")
#       self.setItems()

  