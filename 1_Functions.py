# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,

def calculate_area(b,h) :
    return  (1/2)*b*h

b = int(input("Enter the breadth: "))
h = int(input("Enter the Height: "))

result = calculate_area(b,h)
print("Area of a triangle = ",result)

