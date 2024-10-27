lst = ['Apple','Guava','Mango','Banana','Kiwi']

print("Lenght of list",len(lst))
print("first Element", lst[0])
print("Last Element", lst[-1])

lst.append('papaya')
print("Update List :", lst)

lst.remove('Guava')
print("Update List :", lst)

lst.sort()
print("Sorted List :", lst)

lst.pop(1)
print("Update List :",lst)

lst.reverse()
print("Update List :", lst)

print("Multiplacation on List:",lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()
print("Update List :", lst)