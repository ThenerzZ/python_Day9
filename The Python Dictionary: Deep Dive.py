#dictionary
#{key: value} #the new line after the klammer is for readabvility
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.", #this comma is not neccecary but useful -> you can instantly continue
}

#retriving items from list
#print(programming_dictionary["Bug"])

#adding new items to list
programming_dictionary["Loop"] = "This action of doing something over and over again"
#print(programming_dictionary)

#you can create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# edit an item in a dictionary
programming_dictionary["Bug"] = "different value"
#print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
    print(key) #-> just prints the keys
    print(programming_dictionary[key]) #-> to get the value
