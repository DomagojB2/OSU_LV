try:
    ocjena = float(input())
except ValueError:
    print("Unos mora biti broj.")

if (0.0<=ocjena <=1.0):
    if (ocjena>=0.9):
         print("A")
    elif(ocjena>=0.8):
         print("B")
    elif(ocjena>=0.7):
        print("C")
    elif(ocjena>=0.6):
        print("D")
    else:
        print("F")
else:
    print("Upis broja nije u intervalu [0.0-1.0].")
