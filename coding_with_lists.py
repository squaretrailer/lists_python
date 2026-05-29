
# Step One: Create Lists
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
numbers = [10, 15, 20, 25, 30]

# Print an element by Index
print("Best car: ", cars[2])
print("Favorite fruit: ", fruits[4])
print("Largest number: ", numbers[4])

# Add an item to the list
cars.append("Tesla")
fruits.append("Pineapple")
numbers.append(35)

print("Updated cars list: ", cars)
print("Updated fruits list: ", fruits)
print("Updated numbers list: ", numbers)

# Remove an item from the list
cars.remove("Ford")
fruits.remove("Grapes")
numbers.remove(20)

print("Updated cars list: ", cars)
print("Updated fruits list: ", fruits)
print("Updated numbers list: ", numbers)

# To iterate through a list
print("\n Iterating through cars:")
for car in cars:
    print(f"- {car}")

print("\n Iterating through fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print("\n Iterating through numbers:")
for number in numbers:
    print(f"- {number}")



# To reverse a list
cars.reverse()
fruits.reverse()
numbers.reverse()

print("\n Reversed cars list: ", cars)
print("Reversed fruits list: ", fruits)
print("Reversed numbers list: ", numbers)
