import math
class Calculate_Area():
    def calculate_area(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        if a is not None and b is None and c is None:
            radius = a
            print("Area of Circle")
            return math.pi * radius * radius
        elif a is not None and b is not None and c is None:
            length, width = a, b
            print("Area of Rectangle")
            return length * width
        elif a is not None and b is not None and c is not None and (c.lower()) == "triangle":
            base, height = a, b
            print("Area of Triangle")
            return 0.5 * base * height
        else:
            print("Enter valid number of arguments")
if __name__ == "__main__":
    input_str = input("Enter a list of arguments: ")
    input_list = [x for x in input_str.split(",")]
    Area = Calculate_Area()
    try:
        if len(input_list) == 1:
            a = input_list[0]
            print(Area.calculate_area(float(a)))
        elif len(input_list) == 2:
            a, b = input_list[0], input_list[1]
            print(Area.calculate_area(float(a), float(b)))
        elif len(input_list) == 3 and (input_list[2].lower()) == "triangle":
            a, b = input_list[0], input_list[1]
            c = input_list[2]
            print(Area.calculate_area(float(a), float(b), c))
        else:
            print("Enter valid number of arguments")
    except ValueError as e:
        print("Error:", e)
