for row in range(1, 10):
    for col in range(1, row+1):
        print(col,end="")
    print()

# Ex function
def hello():
    name = input("Input your name: ")  # This is input name from claviature
    age = int(input("Input you age: "))
    print("hello {0}, nice to meet you. Your age is {1}.".format(name,age))
    print("%s you have the %d briliant years."%(name, age))

# Run function hello
hello()

# example  init the []
num = [i for i in range(19) if i > 3 and i < 16]
print(num)
