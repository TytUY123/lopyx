class Cat:
    def __init__(self, name = "unknown", age = 0, feedneed = 200):
        self.name = name
        self.age = age
        self.feedneed = feedneed
        

        
    
c1 = Cat("zhorik", 1, 200)






class Student:

    Uni = "KBTU"

    def __init__(self, name = "Unknown", group = "Unknown", sudid = 0, gpa = 1.0, zp = 200000, balance = 0):
        self.name = name
        self.group = group
        self.studentid = sudid
        self.gpa = gpa
        self.zp = zp
        self.balance = balance
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

    def month(self, spendm = 120000):
        self.balance += self.zp
        print(self.balance - spendm)

s1 = Student("DeltaBust", "1313", 12, 2.5, 150000, 200000)
print(bool(s1))
print(s1)
s1.month(150000)