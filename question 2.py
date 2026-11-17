marks = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks)
print("list", marks, "data type", type(marks))
print("tuple", marks_tuple, "data type", type(marks_tuple))
print(f"maximum marks: {max(marks_tuple)}")
print(f"minimum marks: {min(marks_tuple)}")
count = sum(data <= 40 for data in marks_tuple)
print(f"number of students who scored less than or equal to 40: {count}")
if all(0 <= mark <= 100 for mark in marks_tuple):
    print("All marks are valid.")
## i coudnt get how to use a bool function in this command please explain it to me
marks[1] = 48
print("Updated list", marks, "data type", type(marks))
try:
    marks_tuple[2] = 95
    print("Updated tuple", marks_tuple, "data type", type(marks_tuple))
except TypeError:
    print("Cannot modify a tuple.")
##since i already got a type error ill change this to avoid the error
