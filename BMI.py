n = 1 # Global variable for default number of inputs

# BMI Calculator logic
def bmi_calculator(weight, height):

    # Nested function to display BMI
    def display_bmi():
        print(f"Your BMI is: {bmi:.2f}")

    bmi = weight / (height ** 2) # BMI formula

    display_bmi()

# Function to get number of inputs
def get_number_of_inputs():
    n = int(input("Enter number of inputs: "))
    return n

# Main function of the program
def start_calculator():

    # Ensures that the calculator runs at least once
    number_of_inputs = get_number_of_inputs()
    if (number_of_inputs) < 0:
        number_of_inputs = globals()['n']
    
    while number_of_inputs > 0:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
        bmi_calculator(weight, height)
        number_of_inputs -= 1

if __name__ == "__main__":
    start_calculator()