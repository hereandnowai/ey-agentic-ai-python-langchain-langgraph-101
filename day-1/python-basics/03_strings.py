text = "Meridian Retail Bank"

print("text:", text)
print("type:", type(text))
print("length:", len(text))
print("first character:", text[0])
print("second character:", text[1])
print("last character:", text[-1])
print("second last character:", text[-2])

# Slicing: grab a range of characters with [start:end] where start is inclusive and end is exclusive
print(text[0:8])
print(text[9:15])
print(text[9:])
print(text[:8])
print(text[-4:])

messy = "  Hello, world!   "
print("\nWhitespaces removed:", repr(messy.strip())) # removes leading and trailing whitespaces
print(messy.upper())
print(messy.lower())
print(messy.title())
print("home loan".title())
print("Replace 'world' with 'Python':", messy.replace("world", "Python"))
print("Count: ", text.count("i"))
print("Find: ", text.find("Retail"))
print("Does it start with 'Meridian'? ->", text.startswith("Meridian"))
print("Does it end with 'Bank'? ->", text.endswith("Bank"))

print("Split: ", text.split()) # splits the string into a list of words
print("Slipt with comma: ", "a,b,c,d".split(",")) # splits the string into a list of words using comma as separator

words = ["compliant", "grounded", "auditable"]
print("Join: ", ", ".join(words))

raw = " YES, Please "
cleaned = raw.strip().lower()
print("chained clean:", repr(cleaned))

# more f-strings
customer = "Priya"
product = "Home Loan"
tone = "formal"

prompt = f"Respond to {customer} about their {product} enquiry in a {tone} tone."
print(prompt)

print(f"Product converted into uppercase: {product.upper()}")
print(f"Name Length: {len(customer)}")
print(f"Two products: {product} and a Car Loan")

print("\n")
# multi-line strings
system_prompt = f""" You are a helpful banking assistant.
Customer name: {customer}
Product: {product}
Rules: answer only from approved policy; keep the tone {tone}.

"""
print(system_prompt)

print('She said, "Hello!"')
print("It's a beautiful day!")
print('It\'s a beautiful day!') # escaping single quote with backslash