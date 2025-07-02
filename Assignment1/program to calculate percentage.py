 # programe to calculate the percentage of student based on marks of any 5 subjects

physics = int(input("enter a physics marks"))
chemistry = int(input("enter a chemistry marks"))
biology = int(input("enter a biology marks"))
math = int(input("enter a math marks"))
english = int(input("enter a english marks"))

total_marks = (physics + chemistry + biology + math + english)
print("the total marks is =",total_marks)

percentage =  (total_marks / 5)
print("the percentage of student is =",percentage)