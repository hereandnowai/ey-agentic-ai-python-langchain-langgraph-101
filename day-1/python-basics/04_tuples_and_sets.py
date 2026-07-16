# tuples in python are immutable lists,
# meaning they cannot be changed after creation.
# They are defined using parentheses ().

point = (12.5, 48.1)
color = (255, 200, 0)
person = ("Priya", 30, "savings")

print("point:", point)
print("color:", color)

print(point[0]) # access first element
print(color[1]) # access second element
print(person[-1]) # access last element

name, age, account_type = person # unpacking a tuple into variables
print(f"name: {name}, age: {age}, account_type: {account_type}")

# what is a function in python?
# fun
def min_and_max(a, b):
    """Returns the minimum and maximum of two numbers."""
    if a < b:
        return a, b
    return b, a

low, high = min_and_max(9, 4)
print(f"low: {low}, high: {high}")


# sets in python are unordered collections of unique elements.
# They are defined using curly braces {}.
# it automatically removes duplicates and does not maintain order.

tags = {"loan", "priority", "loan", "kyc", "priority"}
print("tags:", tags) # duplicates are removed

print("loan" in tags) # check if an element is in the set
print("car" in tags) # check if an element is not in the set

tags.add("verified") # add an element to the set
print("tags after adding 'verified':", tags)
tags.add("loan") # adding an existing element does nothing
print("tags after adding 'loan' again:", tags)
tags.discard("kyc") # remove an element from the set
print("tags after discarding 'kyc':", tags)

raw_words = ["yes", "no", "yes", "maybe", "no", "yes"]
unique_words = list(set(raw_words)) # convert list to set to remove duplicates, then back to list
print("unique_words:", unique_words)

skills_needed = {"python", "sql", "apis"}
skills_have = {"python", "excel", "apis"}
print("\nin BOTH (intersection):", skills_needed & skills_have)
print("in EITHER (union):", skills_needed | skills_have)
print("needed but MISSING: ", skills_needed - skills_have)