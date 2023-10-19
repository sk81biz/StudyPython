myList = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]

print(myList)


def findItem(baseList, x):
    count = 1
    for i in baseList:
        
        if i == x:
            print(f"i={i} and x={x} the count = {count}")
            break
        count += 1

findItem(myList, 50)
