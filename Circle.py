class Circle:
    def __init__(self):
        choice = input("Press['r'] to calculate the radius: ")
        if choice == 'r':
            self.radius = float(input("Enter radius: "))
        else:
            raise ValueError("Invalid choice. Please try again.")

    def calculate_area(self):
        return 3.141592653589793 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.141592653589793 * self.radius

# Creating Circle object and calculating area and perimeter
circle = Circle()
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print("Area of the circle is:", area)
print("Perimeter of the circle is:", perimeter)