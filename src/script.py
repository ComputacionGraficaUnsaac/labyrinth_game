x = 35 #nro de lineas
M = []
for i in range(x):
  row = input()
  row = row[1:-2].split(',')
  row.reverse()
  for j in range(len(row)):
    row[j] = int(row[j])

  M.append(row)

for i in M:
  print(i)