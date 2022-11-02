from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

import anvil.server


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.set_last_style()
    
  def set_last_style(self):
      self.style_plot(self.plot_1)
      
      self.plot_1.layout.title = "Valor x Tempo"
      
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


    






