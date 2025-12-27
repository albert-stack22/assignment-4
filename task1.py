try:
  fh = open('sample.txt', "rt")
  print("Readings of a file :")
  i=1
  for j in fh.readlines():
    print(f"This is line {i} {j}")
    i=i+1
  fh.close()
except FileNotFoundError as ferr :
 print(ferr)
