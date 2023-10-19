def inputNumber():
    while True:
        try:
            x = int(input("Pls input number: "))
            for row in range(x):
                for col in range(x):
                    print(f"{row*col:2}", end=" ")
                print()
        except ValueError:
            print("wrong, you should input number, not a string.")
        q = input("Pls make a choice, do you want continue ? y\\n ").lower()
        if q[0] == "n":
            break

            
    

inputNumber()
