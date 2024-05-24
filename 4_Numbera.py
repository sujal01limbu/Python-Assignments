#print binary representation of 17

# Define the number
number = 17

# Initialize an empty string to store the binary representation
binary_representation = ""

# While loop to convert the number to binary
while number > 0:
    # Get the remainder when the number is divided by 2
    remainder = number % 2
    # Add the remainder to the front of the binary representation string
    binary_representation = str(remainder) + binary_representation
    # Divide the number by 2
    number = number // 2

# Print the binary representation
print("Binary representation of 17 is", binary_representation)
