print("Hello Agent!")

# concept 1: what is a variable in python?

agent_name = "Caramel AI" # str
version = 1 # int
is_ready = True # bool

print(agent_name)
print(version)

# concept 2: what is f-string in python?
print("I am Caramel AI, running bootcamp version 1")
print("I am " + agent_name + ", running bootcamp version " + str(version)) # hard way
print("I am {agent_name}, running bootcamp version {version}")
print(f"I am {agent_name}, running bootcamp version {version}")

# concept 3: changing a variable
mood = "curious"
print(f"{agent_name} feels {mood}")

mood = "confident"
print(f"{agent_name} now feels {mood}.")

# PEP 8 Python Enhancement Proposal 8
# 1. Use snake_case for variable names
# 2. Use 4 spaces for indentation
# 3. put spaces around operators ("+", "-", "*", */) and after commas
# 4. choose descriptive variable names: `agent_name` instead of `a`, `version` instead of `v`, etc.