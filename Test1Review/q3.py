import random

d = random.randint(0,9)
print(f"The random digit d is {d}")

# initializing varaibles 
count = 0
cur_num = 0
pre_num = 0

# take the first input and check conditions to cont
num = int(input("Enter a positive integer: "))
if num > 0:
    cur_num = pre_num = num
    if num % 10 == d:
        count += 1

# the rest of the inputs
while num > 0:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        break

    pre_num = cur_num
    cur_num = num
            
    if cur_num > pre_num:
        print(f"The current input {cur_num} is greater than the previous input {pre_num}")
    elif cur_num < pre_num:
        print(f"The current input {cur_num} is smaller than the previous input {pre_num}")
    # else:
    #     print(f"The current input {cur_num} is equal to the previous input {pre_num}")
    
    if num % 10 == d:
        count += 1

# final output
print(f"In total, {count} positive integers ended with the random digit {d}")


