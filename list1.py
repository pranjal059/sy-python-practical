marks=[45,56,78,90,87,65,80.29]

marks.append(100)
marks.remove(56)
marks[4]=70

print("updated list=",marks)
print("Highest marks=",max(marks))
print("Average marks=",sum(marks)/len(marks))
