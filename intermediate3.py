string = input("Enter a string: ")
string = string.replace(" ", "")
str_char = []
dicti = {}
val = 1
for x in string:
    x = x.lower()
    str_char.append(x)

for y in str_char:
    val = str_char.count(y)
# https://phoenixnap.com/kb/python-add-to-dictionary
    dicti.update({y: val})

print(str_char)
print(dicti)
