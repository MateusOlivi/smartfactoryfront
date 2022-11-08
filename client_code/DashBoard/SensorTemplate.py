from ._anvil_designer import SensorTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go
from datetime import datetime

class SensorTemplate(SensorTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    my_type = self.item['telemetry'][0]["type"]
    info_dict = [info for info in self.item['sensor']["info"] if info["type"] == my_type]
    
    upper_limit = info_dict[0]["upper_limit"]
    bottom_limit = info_dict[0]["bottom_limit"]
        
    self.name.text = self.item['sensor']["name"]
    self.type.text = my_type
    self.upper_limit.text = upper_limit if upper_limit != None else "Não definido"
    self.bottom_limit.text = bottom_limit if bottom_limit != None else "Não definido"
    
    self.last_value.text = max(self.item['telemetry'], key = lambda x: x["inserted_at"])["value"]
    self.plot_data(self.item['telemetry'])
    
            
  def plot_data(self, data):                        
    self.plot_1.data= go.Scatter(
                    x = [datetime.fromtimestamp(x['inserted_at']/1000) for x in data],
                    y = [x['value'] for x in data],
                    lines = dict(color='#2196f3')
            )
    
    self.style_plot(self.plot_1)

  def style_plot(self, plot):
    # expand the graphs
    plot.layout = go.Layout(
        title= "<b>Valor x Tempo</b>",
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








