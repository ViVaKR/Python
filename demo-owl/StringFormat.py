petA = "Annie"
petB = "Neo"

# hard way
print("Hard way: Hello " + petA + " and " + petB)

# easier way
print("Easier way: Hello {0} and {1}".format(petA, petB))

if petA == petB:
    print("Is Same")

# easiest
print(f"Easiest way: Hello {petA} and {petB}")

print(f"{342324423431.23424234234:.2f}")

# - {0:6}
# * { Index number of item : Number of digits to show }

# - { 0:6.2f }
# * { Index number of item : Number of digits to show.Number of decimal places }
