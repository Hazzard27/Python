#Lists in Python
#Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))
#Accessing elements in a list
print(my_list[0])  # First element
print(my_list[2])  # Third element
print(my_list[-1]) # Last element
#Modifying elements in a list
my_list[1] = 20
print(my_list)
#Adding elements to a list
my_list.append(6)
print(my_list)
#Removing elements from a list
my_list.remove(3)
print(my_list)
my_list.pop()  # Removes and returns the last item
print(my_list)
#Looping through a list
for item in my_list:
    print(item)