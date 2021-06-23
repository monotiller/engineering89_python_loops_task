for _ in range(10): # Will repeat the following command 10 times
    print("Hello")

list_names = [] # Initialising our list of names
new_names = input("Enter a name into the list or type 'exit' when you're done!: ") # Asking the user for the first name to add to the list or
while new_names.strip().lower() != "exit": # Keeps asking the user for new names UNTIL they're done and they type "exit"
    list_names.append(new_names.strip()) # Appends the user entered name to the end of the name list whilst also stripping white spaces
    new_names = input("Enter a name into the list or type 'exit' when you're done!: ")
print("The list completed list:", list_names) # Prints the list of names

counter = 0 # Initialises a counter for helping with the next part
list_names_lower = [] # Initialises a list for the lower case entries to come in to
for names in list_names: # For all the names in the list do the following:
    list_names_lower.append(list_names[counter].lower()) # Appends the lower case name to the end of the the new list. The counter is used to reference the index of list_names
    counter += 1 # Increments the counter by 1
print(list_names_lower) # Prints out the lower case version of the list

if counter % 2 == 0: # The modulous will check if the amount of values in the list is even or odd using our counter!
    print("There are an even amount of names in the list")
else:
    print("There are an odd amount of names in the list")