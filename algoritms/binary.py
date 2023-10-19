def binary_search(list, item):
    low = 0
    # high = round((len(list) - 1)/2)
    high = len(list) - 1
    i = 0

    while low <= high:
        i = i + 1
        mid = round((low + high)/2)
        gess = list[mid]
        if gess == item:
            print ('i = {0}'.format(i))
            return mid
        if gess > item:
            high = mid - 1
        else:
            low = mid + 1
    print ('i = {0}'.format(i))       
    return None        


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 20, 25, 52]

print (binary_search(my_list, 3))
print (binary_search(my_list, 20))
print (binary_search(my_list, 13))

