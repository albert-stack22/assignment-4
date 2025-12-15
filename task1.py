try :
    fh = open('sample.txt', "rt")
    print("Readings of a file :")
    print(f"This is line 1 {fh.readline()}")
    print(f"This is line 2 {fh.readline()}")
    fh.close()
except FileNotFoundError as ferr :
    print(ferr)
