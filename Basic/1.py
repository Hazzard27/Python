
nums = [ ]
try:
    while True:
        num = input("Enter the number ")
        nums.append(int(num))
        print(nums)
except KeyboardInterrupt as e:
    print(e)        
    

num = list(range(1,21))
print(min(num))
print(sum(num))
print(num)