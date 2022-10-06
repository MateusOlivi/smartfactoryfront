from ._anvil_designer import DashBoard_V2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from .. import routes

class DashBoard_V2(DashBoard_V2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    sensors = routes.get_sensors(5)
    
    my_history = []
    for i in sensors:
      my_history.append(routes.get_history(i["id"], 1))
    
    plot_data = list(map(self.set_last_data, my_history))
    my_items = [
      {
        "plot_data": plot_data[i],
        "id": sensors[i]["id"],
        "name": sensors[i]["name"],
        "max_val":  max(my_history[i], key = lambda x: x["value"])["value"],
        "val": my_history[i][0]["value"],
        "limit_val": sensors[i]["limit_value"]
      } for i in range(len(plot_data))
    ]
    
    my_items.sort(key = lambda x: abs(x["limit_val"] - x["val"]))
    self.repeating_panel_1.items = my_items
    
    
    # Any code you write here will run when the form opens.
  
  def set_last_data(self, data):      
      last_temp = max(data, key = lambda x: x["timestamp"])["value"]
                  
      return go.Scatter(x = [x['timestamp'] for x in data],
                                    y = [x['value'] for x in data],
                                      lines=dict(color='#2196f3'))
    
  