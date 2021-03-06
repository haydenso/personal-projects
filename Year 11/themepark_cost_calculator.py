import math

def test_int(n):
    try:
        int(n)
        return int(n)
    except (ValueError, SyntaxError):
        raise Exception("Invalid input")

class Overall:
    #TASK 1
    def __init__(self):
        self.num_students = 0
        self.ticket_price = 30
        self.coach_price = 550
        self.max_students = 45
        self.paid_students = []
        self.unpaid_students = []
        self.num_freeticket = 0
        self.num_paid = len(self.paid_students) 
    #TASK 1
    def inputNumStudents(self):    # simple input validation
        while True:
            try:
                self.num_students = int(input("How many are estimated to go? "))
                test_int(self.num_students)
                if self.num_students > 45:
                    print("Maximum of 45 participants")
                    continue
                else:
                    break
            except Exception:
                print("Invalid input")
                continue
        return self.num_students
    #TASK 1
    def calcCPC(self):  #CPC = Cost Per Student
        self.freeticket(self.num_students)
        self.predicted_cost = (self.coach_price + ((self.num_students - self.num_freeticket) * self.ticket_price))
        self.cost_per_student = math.ceil(self.predicted_cost / self.num_students)     #math.ceil to round up
        print(f"The predicted total cost is ${self.predicted_cost} (cost of freeticket subtracted), cost per student is ${self.cost_per_student} (rounded up), {self.num_freeticket} free tickets")
        return self.cost_per_student, self.predicted_cost
    #TASK 1
    def freeticket(self, n):
        try:
            self.num_freeticket = math.floor(n/10)    # math.floor to always round down to make sure no extra tickets
            return self.num_freeticket
        except:
            print("No free tickets")  #returns the default value of 0
    #TASK 2
    def add_student(self, name, list_name):
        if int(len(list_name) + 1) <= 45:
            list_name.append(name)
        else:
            print("Maximum number of students")
        return list_name
    #TASK 3
    def calc_price(self):
        self.freeticket(self.num_paid) # calculates number of free tickets
        self.discount = self.num_freeticket * self.ticket_price 
        self.total_cost = int(self.num_paid) * int(self.ticket_price) + self.coach_price - self.discount
        return self.total_cost
    #TASK 3
    def print_paid_students(self):
        print(f"\n{len(self.paid_students)} students have paid: {', '.join(self.paid_students)}")
    def print_unpaid_students(self):
        print(f"{len(self.unpaid_students)} students have not paid {', '.join(self.unpaid_students)}")
    #TASK 3  
    def __str__(self):   #returns the details from calculations 
        self.calc_price()
        self.print_paid_students() # print list of paid students
        self.print_unpaid_students() # print list of unpaid students
        return f"\n{self.num_students} was the initial number of students\nYou get {self.num_freeticket} free ticket\nTotal overall cost is ${self.total_cost} (minus the cost of free tickets)\nThe predicted overall cost is ${self.predicted_cost}"

while True:
    trip_class = Overall()                   #initiate class
    trip_class.inputNumStudents()            # ask for user inputs
    trip_class.calcCPC() 
    count = 1
    
    while count <= 45:  # 45 and not num_students (predicted number) so that more students can come (any number as long as under 45)
        name = str(input(f"\nInput the firstname of student {count} (type END to end): "))   
        count+=1
        if name == "END":
            break
        while True:
            paid_status = str(input("Paid (Y/N)? ")).lower()
            if paid_status == "y":
                paid_status = trip_class.paid_students
                break
            elif paid_status == "n":
                paid_status = trip_class.unpaid_students
                break
            else:
                print("Invalid option, type Y or N")
                continue
        trip_class.add_student(name, paid_status)

    print(trip_class)  #__str__ method returns a string of the details
    if trip_class.predicted_cost > trip_class.total_cost:
        print(f"The school has made a lost of ${trip_class.predicted_cost -  trip_class.total_cost}")
    elif trip_class.predicted_cost < trip_class.total_cost:
        print(f"The school has made a profit ${trip_class.total_cost -  trip_class.predicted_cost}")
    else:
        print("0 profits or losts were made")
    break