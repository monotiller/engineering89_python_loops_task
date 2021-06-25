# Loops task
This task is a demonstration of what to do with loops! The task summary reads as follows:
* make a loop with a range that says hello 10 times
* create another loop with a range that asks for names and appends to list names
* make a loop that iterated over each name in list_name and format's it into lowercase in a new variable called list_names_lower
* Iterate over the list of values to find if the are even

There are comments in the code to help walk you through

## `loops.py`
First we will print out `Hello` 10 times, just to test that we know that loops are working:
```python
for _ in range(10):
    print("Hello")
```
Then we're going to initialise a list where we can enter some information:
```python
list_names = []
```
What we're going to do is ask the user to fill this wth names, they can add as many as they like and all they have to do is type `exit` to stop entering in name:
```python
new_names = input("Enter a name into the list or type 'exit' when you're done!: ")
while new_names.strip().lower() != "exit": # Keeps asking the user for new names UNTIL they're done and they type "exit"
    list_names.append(new_names.strip()) # Appends the user entered name to the end of the name list whilst also stripping white spaces
    new_names = input("Enter a name into the list or type 'exit' when you're done!: ")
print("The list completed list:", list_names)
```
Then we're going to convert the names to lower case using `lower()` and then print those out to the screen
```python
counter = 0
list_names_lower = []
for names in list_names:
    list_names_lower.append(list_names[counter].lower())
    counter += 1
print(list_names_lower)
```
Finally, we count the amount of names in the list and tell the user if there are an even or odd amount!
```python
if counter % 2 == 0: # The modulous will check if the amount of values in the list is even or odd using our counter!
    print("There are an even amount of names in the list")
else:
    print("There are an odd amount of names in the list")
```