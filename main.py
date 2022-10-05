numbers = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************

average = sum(numbers)/len(numbers)

for i in range(len(numbers)):
    print (f'{abs(average - numbers[i]):.2f}', end=' ')

# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
