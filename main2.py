class Student:

    Uni = "KBTU"

    def __init__(self, name = "Unknown", group = "Unknown", sudid = 0, gpa = 1.0):
        self.name = name
        self.group = group
        self.studentid = sudid
        self.gpa = gpa
    def __bool__(self):
        return self.gpa >= 2.0

    def __str__(self):
        return f"Student {self.name} have GPA {self.gpa}"

    def sayhello(self):
        print(f'hello, my name is {self.name}')

    def info(self):
        print("Name:", self.name)
        print("Group:", self.group)
        print("ID:", self.studentid)
        print("Uni:", self.Uni)

s1 = Student("DeltaBust", "1313", 12, 2.5)
print(bool(s1))
print(s1)