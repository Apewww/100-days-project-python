# 1
# for i in range(5, 0, -1):
#     print(i)

# 2
# count =  5
# while count > 0:
#     print(count)
#     count -= 1

# count =  0
# while count < 5:
#     print(count)
#     count += 1

# 4
# import time
# for i in range(10, 0, -2):
#     print(i)
#     time.sleep(2)
# print("Welcome to the World!")

# 5
import time

# Step 1: Get user input for countdown start
start = int(input("Enter the number to start the countdown: "))

# Step 2: Countdown using a while loop
print("\n------- Countdown Begin -------")
while start > 0:
    print(start)
    time.sleep(1)
    start -= 1
    
# Step 3: Print Final Message
print("Countdown Complete")