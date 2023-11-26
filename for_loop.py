# To understanding for loop we need learn basic in python first 

# Example 1

#for any_element_that_you_want in range(1,10):
    #print(x)

# What we are doing is make ver as x and saying x = 1-9 and print(x)
# remeber we don't count the last one

#for x in range(1,10):
    #print(x)

# Its same thing we are doing but there is no start point

#for x in range(10):
    #print(x)



# Example 2 

# We are making a list and putting "list_example" after in 
# Then we are putting x because as we said it make a ver as x and saying x = Jack , Mary , Zack, Mark

#list_example = ("Jack", "Mary", "Zack", "Mark")

#for x in list_example:
    #print(x)


#list_example_2 = ["Jack", "Mary", "Zack", "Mark"]

#for x in list_example_2:
    #print(x)

#list_example_3 = {
    #"Jack", 
    #"Mary",
    #"Zack",
    #"Mark"
#}

#for x in list_example_3:
    #print(x)




# Example 3 

# EXAMPLE WHAT NOT TO DO 
#user_input = input("Input: ") # Input user_input

#for x in user_input: # Use for in loop it not working because 
#The issue with your code is related to the way you are using the for x in user_input: 
# loop and checking if x == "No". The loop is iterating over each character in the user_input string, 
# so x represents individual characters, not the entire substring "No".
    #if x == "No":
        #print("Wrong")
    
    #else:
        #print("Workk")


# Example 4 
# The loop is unnecessary if you only want to access the value for a specific key. 
# The loop would be useful if you wanted to iterate over all keys and values in the dictionary.


#key = {
    #"Mark": "Mark123",
    #"Zack": "Zack123",
    #"Mary": "Mary123"
#}

#for x in key:
    #print(key["Mark"])  # It will print 3 becuase there the three keys 

# Print keys and values in a dictionary

#person = {"name": "John", "age": 30, "city": "New York"}
#for key, value in person.items(): # Remeber .items is listing each item in person 
#    print(f"{key}: {value}")

# IF YOU DON"T UNDERSTANDT .ITEMS()

#The items() method returns a view object. 
# The view object contains the key-value pairs of the dictionary, as tuples in a list.
#The view object will reflect any changes done to the dictionary, see example below


#Example 5 

# Print each element in a list of lists

#matrix = [[1, 2, 3], [4, 6], [7, 8, 9]]

# To understand this is let say we are wanting print number but we dont 5 so we took out five and boom 
#for row in matrix:
    #for element in row:
        #print(element)



#Example 6

# Print each character in a string
#word = "Python"
# It printing each LETTER
#for char in word:
    #print(char)


# If you have any question please look up in youtube for in loops 
# To better understand the lesson
# Thank you this is end 
