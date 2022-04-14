import plotly.express as px
import pandas as pd

def main(n: int):
  data = []
  step = 0

  curr = n
  while curr != 1:
    if curr % 2 != 0:
      data.append({"step": step, "value": curr})
      curr = (3 * curr) + 1
      step += 1
      if curr == 1: 
        print("end")
        data.append({"step": step, "value": curr}) 
    else:
      data.append({"step": step, "value": curr})
      curr = int(curr / 2)
      step += 1
      if curr == 1: 
        print("end")
        data.append({"step": step, "value": curr}) 

  
  chart_data = pd.DataFrame(data)
  
  fig = px.line(chart_data, y="value", x="step")
  
  fig.show()

main(27)