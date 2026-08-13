Feedback=input("Enter feedback:")

print("\n******CUSTOMER FEEDBACK REPORT******** ")

print("\nORIGINAL FRRDBACK:",Feedback.swapcase())


print("     \n FEEDBACK SUMMARY        ")

print("Total characters:", len(Feedback))
print("Total words:", Feedback.split())
print("Total Spaces:", Feedback.count(" "))
print("Total Exlamation Marks:", Feedback.count(" !"))


print("        \nFORMATTED FEEDBACK             ")

print("Lower Case Feedback:", Feedback.lower())
print("Upper Case Feedback:", Feedback.upper())