class Staff():
    def __init__(self, a, b, c, d):
        self.first_name = a
        self.last_name = b
        self.location = c
        self.role = d

    def printinfo(self):
        print("Name:", self.first_name, self.last_name, "Location:", self.location, "Role:", self.role)



staff1 = Staff('Shuping', 'Zhang', 'International Campus', 'faculty')
staff1.printinfo()

staff2 = Staff(input(), input(), input(), input())
staff2.printinfo()

print(staff2.first_name)