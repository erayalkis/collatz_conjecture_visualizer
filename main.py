
def main(n: int):
  data = {}
  step = 0

  curr = n
  while curr != 1:
    if curr % 2 != 0:
      data[step] = curr

      curr = (3 * curr) + 1
      step += 1
    else:
      data[step] = curr

      curr = int(curr / 2)
      step += 1

main(27)