def counter():
    i = 1
    while i <= 10:
        yield f"Even - {i}"
        i += 1

# Convert the generator to a list
my_list = list(counter())

# Print each item in the list
for item in my_list:
    print(item)
