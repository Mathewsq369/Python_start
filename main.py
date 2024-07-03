class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make: " + self.make + " Model: " + self.model + " Year: " + str(self.year))

car1 = Car("Toyota","Corolla",2022)

car1.display_info()


class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self,length,width):
        return length * width


class Circle(Shape):
    def area(self,radius):
        return 3.14 * radius ** 2

rectangle = Rectangle()
result_rectangle = rectangle.area(4,5)
print(result_rectangle)

circle = Circle()
result_circle = circle.area(3)
print(result_circle)


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:",result)
except ZeroDivisionError:
    print("Error: cannot divide by zero.")
except ValueError:
    print("Error: Invalid input.")



file = open("myfile.txt", "w")
file.write("Programming is fun")
file.close()

file = open("myfile.txt", "r")
content = file.read()
print(content)
file.close()




class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def delete_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("task deleted")
        else:
            print("task not found")
    def edit_task(self,old_task,new_task):
        if old_task in self.tasks:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task
            print("task changed successfuly")
        else:
            print("task not found!")


manager = ToDoListManager()
manager.add_task("Wash Dishes")
manager.add_task("Cook Ugali")
manager.add_task("Take a shower")
manager.view_tasks()
manager.edit_task("Wash Dishes","Clean Dishes")
manager.view_tasks()
manager.delete_task("Washroom")

my_list = []
my_list.append("oeeeee")
my_list.append("ayeiyaa")

for item in my_list:
    print(item)

my_list.append("niajee msela")
index = my_list.index("ayeiyaa")
my_list[index] = "buruburu"

for item in my_list:
    print(item)

