class Employee:
    def __init__(self, name, salary, mobile, email):
        self.name = name
        self.salary = salary
        self.mobile = mobile
        self.email = email

    def display_info(self):
        print("Employee Information:")
        print("Name  :", self.name)
        print("Salary:", self.salary)
        print("mobile :", self.mobile)
        print("Email :", self.email)







