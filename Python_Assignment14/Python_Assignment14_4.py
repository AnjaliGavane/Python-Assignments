class Student:
    # Class variable
    school_name = " city pride school"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print("Student Name:", self.name)
        print("School Name:", Student.school_name)


def main():
    obj1 = Student("John", 101)
    print("Before changing school name:")
    obj1.display_info()
    Student.school_name = "Podar International School"
    print("\nAfter changing school name:")
    obj1.display_info()


if __name__ == "__main__":
    main()