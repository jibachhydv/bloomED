# Get the Number whose index is to be returned
while True:
    try:
        num = int(input("Get Integer: "))
        break
    except ValueError:
        print("Your Input is not integer")

# List of Number 
numbers = [3,6,5,8]


# Function that return index of input number
def returnIndex(listNum, num):
    for i in range(len(listNum)):
        if listNum[i] == num:
            return i
    return -1
    
# Run the Function
print(f"Index of {num} in {numbers} is {returnIndex(numbers, num)}")