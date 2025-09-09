import math

students = int(input("How many students on the course?"))
size = int(input("Desired group size?"))
groups = math.ceil(students / size)

print(f"Number of groups formed: {groups}")


