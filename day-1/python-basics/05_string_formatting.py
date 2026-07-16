price = 1234.5
ratio = 0.8375
count = 42
name = "Priya"

print(f"raw price: {price}")
print(f"two decimal places: {price:.2f}")
print(f"0 decimal places: {price:.0f}")
print(f"pi to 4 places: {3.141592653589793:.4f}")

print(f"\nratio as percent: {ratio:.1%}")
print(f"ratio as percent: {ratio:.0%}")

big = 5000000
print(f"\nplain : {big}")
print(f"comma : {big:,}")
print(f"money style: {big:,.2f}")

print("\n Alignment: (each field is 10 wide, shown between ||)")
print(f"|{name:<10}| left aligned")
print(f"|{name:>10}| right aligned")
print(f"|{name:^10}| centered")

rows = [("Home Loan", 5000000, 0.084),
        ("Car Loan", 800000, 0.099),
        ("Personal", 150000, 0.155)]
print("\nProduct      Amount      Rate")
print("-" * 30)
for product, amount, rate in rows:
    print(f"{product:<12} {amount:>10,} {rate:>6.1%}")


print("\n\nZero padding:")
print(f"ticket #{7:03d}")
print(f"ticket #{42:03d}")
print(f"time {9:02d}:{5:02d}:{3:02d}")

print("\n\nSame sentences, three styles")
print(f"f-string: {name} has {count} points") # modern way
print("format(): {} has {} points".format(name, count)) # older way 
print("percent: %s has %d points" % (name, count)) # oldest way

print("\nLiteral braces:")
print(f"{{this is in curly braces}} and {name} is the client")