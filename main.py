import plotly.express as px
import pandas as pd
import time
from os import path, mkdir
from sys import argv

def get_user_input():
  user_input = None

  try:
    user_input = int(input("Please input an integer value:"))
  except:
    raise Exception("Input must be an integer!")
  
  if user_input <= 0: raise Exception("Input cannot be 0 or lower!")

  return user_input

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
        data.append({"step": step, "value": curr}) 
    else:
      data.append({"step": step, "value": curr})
      curr = int(curr / 2)
      step += 1
      if curr == 1: 
        data.append({"step": step, "value": curr}) 
  
  return data

def check_dirs():
  dirs = ["./out_image", "./out_html"]

  for directory in dirs:
    if not path.exists(directory): mkdir(directory)

def chartify_data(data):
  chart_data = pd.DataFrame(data)
  fig = px.line(chart_data, y="value", x="step")

  curr_time = time.localtime()
  time_str = f"{curr_time.tm_mday}-{curr_time.tm_mon}-{curr_time.tm_year}-{curr_time.tm_hour}-{curr_time.tm_min}-{curr_time.tm_sec}"
  
  fig.write_image(f"./out_image/{time_str}.png")
  fig.write_html(f"./out_html/{time_str}.html")

def run_range():
  if len(argv) < 4:
    raise Exception("Please input 2 integers for range values")
  i = int(argv[2])
  while i < int(argv[3]):
    data = get_data(i)
    chartify_data(data)
    time.sleep(1)
    i += 1

def main():
  check_dirs()

  if "--range" in argv:
    run_range()
    return
  
  n = get_user_input()
  data = get_data(n)
  chartify_data(data)

if __name__ == "__main__":
  main()