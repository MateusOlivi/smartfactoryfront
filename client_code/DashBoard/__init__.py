from ._anvil_designer import DashBoardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from datetime import datetime

class DashBoard(DashBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.set_last_temp()
    self.set_max_temp()
     
  def set_last_temp(self):
      data = anvil.server.call('get_temp_history')
      
      last_temp = max(data, key = lambda x: x["datetime"])["temperature"]
      
      self.last_temp.text = f"{last_temp}°"
            
      self.plot_1.data = go.Scatter(x = [x['datetime'] for x in data],
                               y = [x['temperature'] for x in data],
                                      lines=dict(color='#2196f3'))
      self.style_plot(self.plot_1)
      self.plot_1.layout.title = "Temperatura x Tempo"
  
  def set_max_temp(self):
      data = anvil.server.call('get_temp_history')
      
      for my_data in data:
        my_data["datetime"] = my_data["datetime"].split("T")[0]
        
      data.sort(key = lambda x: x["temperature"], reverse = True)
      data.sort(key = lambda x: x["datetime"])
      
      result = []
      added = []
      for my_data in data:
        date = my_data["datetime"]
        if(date not in added):
          added.append(date)
          result.append(my_data)
          
      last_temp = max(result, key = lambda x: x["datetime"])["temperature"]

      
      self.max_daily_temp.text = f"{last_temp}°"
            
      self.plot_2.data = go.Scatter(x = [x['datetime'] for x in result],
                                    y = [x['temperature'] for x in result],
                                      lines=dict(color='#2196f3'))
      self.style_plot(self.plot_2)
      self.plot_2.layout.title = "Max Temperatura x Dia"
    
  def style_plot(self, plot):
    # expand the graphs
    plot.layout = go.Layout(
        margin=dict(
            l=50, #left margin
            r=50, #right margin
            b=50, #bottom margin
            t=50, #top margin
        ),
        font=dict(family='Arial', size=10),
        xaxis=dict(
          zeroline=False,
          tickfont=dict(
              family='Arial',
              size=11,
              color='#808080'
          ),
        ),
        yaxis=dict(
            zeroline=False,
            tickfont=dict(
                family='Arial',
                size=11,
                color='#808080'
            ),
          rangemode = "tozero"
        ))

#   def timer_1_tick(self, **event_args):
#     with anvil.server.no_loading_indicator:
#       self.set_last_temp()











