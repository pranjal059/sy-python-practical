list=[ 1,2,3,4,5,"shreya","rutuja"]
print(list)
list.append(6)
print(list)
list.insert(2,10)
print(list)
list[3]=10
print(list)
list.extend(["s","p"])
print(list)
print(list[7])
list.remove("rutuja")
print(list)
list.pop(5)
print(list)
list.pop()
print(list)
del list[1]
print(list)
print(len(list))
if 4 in list:
    print("element is present")
    
else:
    print("element is not present") 
for i in list: 
     print(i)  

print(list.count(4))

print(list.index(4))

list=[1,3,5,6,3]
list.sort()
print(list)

list.sort(reverse=True)
print(list)


New_list=list.copy()
print(New_list)