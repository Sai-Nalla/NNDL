list_heights = []
heights_in_cm = []
while True:
    h1 = input("Enter heights of customers(inches) (press q to quit):")
    if h1 == 'q':
        break
    else:
        list_heights.append(h1)
    
print("L1: ",list_heights)
heights_in_cm = [int(height) * 2.54 for height in list_heights]
print("Output: ", heights_in_cm)


