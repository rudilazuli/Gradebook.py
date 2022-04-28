last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# step 1
subjects = ["physics", "calculus", "poetry", "history"]
# step 2
grades = [98, 97, 85, 88]
# step 3
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
# step 4
print(gradebook)
# step 5
gradebook.append("computer science")
gradebook.append(100)
print(gradebook)
# step 6
gradebook.append(["visual arts", 93])
print(gradebook)
# step 7
gradebook[-1][-2]
# step 8
gradebook[2].remove(85)
# step 9
gradebook[2].append("Pass")
print(gradebook)
# step 10
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
