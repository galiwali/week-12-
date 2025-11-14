# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# lists are part of the collectors family in Python
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) # 5
print(type(my_list)) # <class 'list>
print(my_list[0]) # 1
print(my_list[1:4]) # [2, 3. 4]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:-1]) # [1, 2, 3, 4]
#reverse the list
print(my_list[::-1]) # [5, 4, 3, 2, 1]
#  Modifying a list
my_list.append(6) # adds 6 to the enf of the
print(my_list) # [1, 2, 3,4, 5]
# add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7]
# remove the last item
my_list.pop()
print(my_list) # [1, 2, 3, 4, 5, 6, 7]
#sort the list in ascending order
my_list.sort()
print(my_list) # [1, 2, 3, 4, 5, 6, 7]
# reverse the list
my_list.reverse()
print(my_list) # [7, 6, 5, 4, 3, 2, 1]
#.remove to remove a specific value
my_list.remove(4)
print(my_list) # [7, 6, 5, 4, 3, 2, 1]
#remove the last item using negative index
# add 50 more to the end of the line
new_list = list(range(12,120))
print(new_list)
my_list.append(new_list)
print(my_list)
# my_list.extend(new_list)
# pring(my_list)
new_list = list(range(120,220))
print(new_list)
my_list.append(new_list)
print(my_list)
# print every third item in the list
print(my_list[ : : 3])
# print every tenth item in the list
print(my_list[ : : 10])
# remove every 3rd item in the list
del my_list[ : : 3]
print(len(my_list))
print(my_list)

#list functions
# .append() - adds an item to the end of the list
# .extend() - addds multiple items to the end of the list
# .pop() - removes and returns an item at a given index
#   (default is the last item)
# .remove() - removes the first occurance of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
#####################################
# why is a list more useful than a variable?
# A list can hold multiple values,
#  while a variable can only hold one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
# access the first item
print(cakes[0]) # chocolate
# access the last item
print(cakes[-1]) # carrot
# want the chocolate cake instead of vanilla
cakes[0]= 'strawberry'
print(cakes) # ['strawberry', 'vanilla', 'red velvet', 'carrot']
# add a new cake to the end of the list
cakes.append('lemon')
print(cakes) # ['strawberry', ' chocolate', ' red velvet', 'carrot]
#remove the last cake
cakes.pop()
print(cakes)
# insert a new cake at index 2




# Examples:




my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

foods = ['tacos', 'spagetti', 'potato', 'tamales', 'chicken nuggets']
print(foods)

# Print the second and last item.
print(foods[-4:-5])
print(foods)


# Add a new item using .append().
foods.append('enchiladas')
print(foods)

# Remove the first item using .pop(0).
foods.pop()
print(foods)

# Reverse your list using .reverse().
foods.reverse()
print(foods[::-1])

#Tuples are ordered collections of items
#tuples are immutable, meaning you cannot modify them after creation
#tuples are created using ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1:4])
