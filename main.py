import plotly.express as px
import pandas as pd
import time
from os import path, mkdir

def get_data(n: int):
  data = []
  step = 1

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
  
  return data

def check_dirs():
  dirs = ["./out_image", "./out_html"]

  for directory in dirs:
    if not path.exists(directory): mkdir(directory)

def main(n: int):
  data = get_data(n)

  chart_data = pd.DataFrame(data)
  fig = px.line(chart_data, y="value", x="step")
  curr_time = time.localtime()
  time_str = f"{curr_time.tm_mday}-{curr_time.tm_mon}-{curr_time.tm_year}-{curr_time.tm_hour}-{curr_time.tm_min}-{curr_time.tm_sec}"
  
  check_dirs()

  fig.write_image(f"./out_image/{time_str}.png")
  fig.write_html(f"./out_html/{time_str}.html")

main(21)