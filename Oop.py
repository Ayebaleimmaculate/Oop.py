#Create a user class with properties; name, age, location.
myName = "Immaculate"
myAge = "24"
myLocation = "kampala"

#create a new instance of the user class. (a new object) .
class user:
    def __init__ (my,name,age,location):
        my.name = name 
        my.age = age
        my.location = location
x = user("Immaculate", 24, "kampala")
print(x.name)
print(x.age)
print(x.location)
#Access the user's name and age.


#create a function for the user class that print a user location.
#using the string representation
class user:
    def __init__(my,name,age,location):
        my.name = name
        my.age = age
        my.location = location
    def __str__(my):
        return f"{my.name}({my.age})"
    x = user("Immaculate", 24, "kampala")
    print(x)
#printing user's location
    def print_location(my):
            print("user's location:",my)
    
#Print the user location using this function.
print("kampala")