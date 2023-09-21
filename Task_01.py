import math
class Calculate_Area():
    def calculate_area(self, args):
        if len(args) == 1:
            radius = int(args[0])
            print("Area of Circle")
            return math.pi * radius * radius
        elif len(args) == 2:
            length, width = args
            print("Area of Rectangle")
            return int(length) * int(width)
        elif len(args) == 3 and (args[2].lower()) == "triangle":
            base, height, triangle = args
            print("Area of Triangle")
            return 0.5 * int(base) * int(height)
        else:
            print("Enter valid number of arguments")

input_str = input("Enter a list of arguments: ")
input_list = [x for x in input_str.split(",")]
Area = Calculate_Area()

try:
    area = Area.calculate_area(input_list)
    print("Area:", area)
except ValueError as e:
    print("Error:", e)
