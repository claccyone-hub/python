import os

# Step 1: Ask the user to enter a new item
item = input("Enter the name of the new item: ")

# Step 2: Check if file exists
filename = "items.txt"

if not os.path.exists(filename):
    # File does not exist → Create and write
    with open(filename, "w") as file:
        file.write(item + "\n")
    print("File created and item added.")
else:
    # File exists → Open in append mode
    with open(filename, "a") as file:
        file.write(item + "\n")
    print("Item added to existing file.")

# Step 3: Read and display full list of items
print("\nFull List of Items:")
with open(filename, "r") as file:
    items = file.readlines()
    for i in items:
        print(i)