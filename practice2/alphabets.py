str =input('enter a number:')
length =len(str)
for row in range(length):
    for col in range(row,row+1):
        print(str[col],end=" ")
print()

