import plotly.express as px
import pandas as pd
import time
from os import path, mkdir

def run_math(n: int):
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
  data = run_math(n)

  chart_data = pd.DataFrame(data)
  fig = px.line(chart_data, y="value", x="step")
  curr_time = time.localtime()
  
  check_dirs()

  fig.write_image(f"./out_image/{curr_time.tm_year}.png")
  fig.write_html(f"./out_html/{curr_time.tm_year}.html")

  fig.show()

main(27)