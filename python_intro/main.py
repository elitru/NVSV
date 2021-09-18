def main():
    print("Welcome my first python program!")
    tryIfCluster()
    tryObjcets()
    calculateSum()
    
    print("\nThank you for using this software :)")

def printFunctionalityTitle(title):
    print("")
    print("=========================================")
    print(title)
    print("=========================================")
    print("")

def calculateSum():
    printFunctionalityTitle("Functionality 1 | Sum of numbers")
    numbers = []
    amount = 0

    while True:
        try:
            amount = int(input("How many numbers do you want to sum up? \nEnter: "))
        except:
            print("Not a numeric value")
            continue

        if amount < 2:
            print("You must enter a number > 1")
            continue
        break

    i = 0
    while i < amount:
        try:
            num = int(input("Enter the {}. number: ".format(i +1)))
            numbers.append(num)
            i += 1
        except:
            print("Not a numeric value")
            continue
    
    print("The sum of the numbers {} is {}.".format(numbers, sum(numbers)))

def tryObjcets():
    printFunctionalityTitle("Objects in Python")

    print("Let's first create a student...")
    studentName = input("Name: ")
    studentClass = input("Class: ")
    student = Student(studentName, studentClass)
    
    print("Now let's create a teacher...")
    teacherName = input("Name: ")
    teacherSubjects = input("Subjects (comma separated): ")
    teacher = Teacher(teacherName, teacherSubjects.split(","), [student])
    teacher.tellSubjects()

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, classKey):
        super().__init__(name)
        self.classKey = classKey

    def introduceMyself(self):
        print("{}: Hello, my name is {} and I'm in class {}.".format(self.name, self.name, self.classKey))

class Teacher(Person):
    def __init__(self, name, subjects, students):
        super().__init__(name)
        self.subjects = subjects
        self.students = students

    def tellSubjects(self):
        print("Hello, my name ist {} and I'm a teacher. I teach the following subjects: {}".format(self.name, ', '.join(self.subjects)))
        print("I teach a lot of students and I'd like to introduce you to them.")

        for student in self.students:
            student.introduceMyself()

def tryIfCluster():
    printFunctionalityTitle("If statements")
    request = input("Enter \"ping\" or \"pong\": ")

    if request == "ping":
        print("Pong")
    elif request == "pong":
        print("ping")
    else:
        print("I told you to either choose ping or pong! Didn't you listen?")

if __name__ == "__main__":
    main()