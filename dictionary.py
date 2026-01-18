#Dictionary in Python
#Creating a dictionary
car = {"Company": "Ford",
       "Model": "Mustang",
        "Year": 1964}

print(car)
print(car["Company"])

#Adding items to a dictionary
car["Color"] = "Red"
print(car)

#Modifying items in a dictionary
car["Year"] = 2020
print(car)

#Removing items from a dictionary
del car["Model"]
print(car)

#Looping through a dictionary
for key in car:
    print(f"{key}: {car[key]}")

