def counter():
    i = 1
    while i<=10:
        yield f"Even - {i}"
        i += 1
        
    my_list = list(counter())
    #for i in range(1,11):
    #print(my_list)
    