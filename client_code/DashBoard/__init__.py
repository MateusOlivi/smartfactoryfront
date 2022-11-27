from ._anvil_designer import DashBoardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

import anvil.server
from datetime import datetime
from anvil.js.window import localStorage, sessionStorage
from .. import routes

class DashBoard(DashBoardTemplate):
  def __init__(self, **properties):
    # Preparando atributos
    self.sensor_id = properties.get('sensor_id', None)
    self.token = localStorage.get("access_token")

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.translator = {
      "Todo momento": None,
      "Última Hora": 3600, 
      "Últimos 30 minutos": 1800, 
      "Ultimos 5 minutos": 300, 
      "Ultimo dia": 84600 
    }
    
    self.dropdown_time.items = list(self.translator.keys())
      
    self.dropdown_sensors.items = self.prepareDropdown()
    
    self.setItems()
        
  # Any code you write here will run when the form opens.
  def setItems(self):  
    self.sersors = self.prepareSensorList()
    
    if(self.dropdown_sensors.selected_value != "Todos Sensores"):
      self.sersors= [sensor for sensor in self.sersors if sensor["name"] == self.dropdown_sensors.selected_value]

    self.telemetry_data = self.prepareTelemetry()
    
    my_items = [{
      "telemetry": data["telemetry"],
      "sensor": data["sensor"],
      "time": self.translator[self.dropdown_time.selected_value]
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
#         if(datetime.timestamp(datetime.now()) - telemetry["inserted_at"]/1000 > 3600):
#           continue
          
        my_type = telemetry["type"]
        
        if((my_id, my_type) not in data.keys()):
          data[(my_id, my_type)] = {}
          data[(my_id, my_type)]["telemetry"] = []
          data[(my_id, my_type)]["sensor"] = sensor
          
        data[(my_id, my_type)]["telemetry"].append(telemetry)
    
    return data
  
  def prepareDropdown(self):
    sensor_list = self.prepareSensorList()
      
    sensors_names = [sensor["name"] for sensor in sensor_list if routes.getTelemetry(self.token,sensor["sensor_id"]) != []]
    
    if(len(sensors_names) !=1):
      sensors_names = ["Todos Sensores"] + sensors_names
      
    return sensors_names
      
  def timer_1_tick(self, **event_args):
    with anvil.server.no_loading_indicator:
      self.setItems()

  def dropdown_sensors_change(self, **event_args):
    self.setItems()

  def dropdown_time_change(self, **event_args):
    self.setItems()




  