userList = input("please provide a list of numbers:")
userList = userList.split()
# https://bobbyhadz.com/blog/python-split-string-into-list-of-integers
# this method allows each input of the list be converted into an integer
userList = [int(x) for x in userList]


def get_unique_list(list1):
    unique = []
    for x in list1:
        if x not in unique:
            unique.append(x)
    return unique


userResult = get_unique_list(userList)
print(userResult)

myList1 = [1, 2, 2, 3, 5, 8, 7, 7]
newList = get_unique_list(myList1)
print(newList)
