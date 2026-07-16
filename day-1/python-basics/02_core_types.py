
count = 42              # integer
temperature = 0.7       # float
name = "Caramel"        # string
is_active = True        # boolean - True or False (note the capital T and F)
missing = None          # NoneType - represents the absence of a value

print(count)
print(type(count))

print(f"count: {count}, type: {type(count)}")
print(f"temperature: {temperature}, type: {type(temperature)}")
print(f"name: {name}, type: {type(name)}")
print(f"is_active: {is_active}, type: {type(is_active)}")
print(f"missing: {missing}, type: {type(missing)}")

age_text = "42"  # string representation of an integer
age_number = int(age_text)

print(type(age_text))
print(type(age_number))

price = float("19.99") # str -> float
print("float('19.99') ->", price)

print(int('30') + 5)

print("\n\nArithmetic operations:")
print(" 7 + 3 =", 7 + 3)
print(" 7 - 3 =", 7 - 3)
print(" 7 * 3 =", 7 * 3)
print(" 7 / 3 =", 7 / 3)   # always returns a float
print(" 7 // 3 =", 7 // 3) # floor division throws away the decimal part
print(" 7 % 3 =", 7 % 3)   # modulus operator returns the remainder of the division
print(" 7 ** 3 =", 7 ** 3)

print(" is 10 even? ->", 10 % 2 == 0) # True if 10 is even, False otherwise
print(" is 11 even? ->", 11 % 2 == 0) # True if 11 is even, False otherwise

# comparison operators: <, <=, >, >=, ==, !=
print("\nComparison operations:")
print(" 5 > 3 -->", 5 > 3) # greater than
print(" 5 < 3 -->", 5 < 3) # less than
print(" 5 >= 3 -->", 5 >= 3) # greater than or equal to
print(" 5 <= 3 -->", 5 <= 3) # less than or equal to
print(" 5 == 3 -->", 5 == 3) # equal to ('==' asking if 5 is equal to 3)
print(" 5 != 3 -->", 5 != 3) # not equal to

# logical operators: and, or, not
has_account = True
is_verified = False
print("\nLogical operations:")
print(has_account and is_verified)
print(has_account or is_verified)
print(not has_account)
print(not is_verified)

balance = 15000
eligible = balance > 10000 and has_account
print(" eligible for a loan? ->", eligible)

# truthiness of values in Python
print("\nTruthiness of values:")
print("\nbool('') ->", bool('')) # empty string is False
print("bool('Hello') ->", bool("Hello")) # non-empty string is True
print("bool(0) ->", bool(-1)) # 0 is False
print("bool(None) ->", bool(None)) # None is False