# List Example: Managing a to-do list
# Create a to-do list (mutable: can be updated)
todo_list = ["Finish project", "Call client", "Write report"]  # Initial tasks
print("Original To-Do List:", todo_list)

# Adding tasks
todo_list.append("Plan team meeting")  # Add a new task
print("\nAfter adding task by use 'append':", todo_list)
todo_list.insert(1, "Reply to emails")  # Insert a task at a specific position
print("\nAfter adding task by use 'insert':", todo_list)

# Sorting the list alphabetically
todo_list.sort()  # Sort the tasks in alphabetical order
print("\nAfter sorting alphabetically:", todo_list)

todo_list.sort(reverse=True)  # Sort the tasks reversely in alphabetical order
print("\nAfter sorting alphabetically backwards:", todo_list)

# Reversing the list
todo_list.reverse()  # Reverse the order of the list
print("\nAfter reversing the list:", todo_list)

# Removing tasks
todo_list.pop(0)  # Remove the first task using its index
print("\nAfter removing task by use 'pop':", todo_list)
todo_list.remove("Plan team meeting")  # Remove a task by its value
print("\nAfter removing task by use 'remove':", todo_list)

# Deleting a range of tasks using `del`
del todo_list[1:3]  # Remove tasks from index 1 to 2 (excluding index 3)
print("\nAfter deleting a range of tasks (index 1 to 2):", todo_list)

