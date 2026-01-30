import streamlit as st
import numpy as np

# st.title("Hello")
# st.write("Task")

# name = st.text_input("Enter your name:")

# if st.button("Say Hello"):
#     st.success(f"Hello {name}")

# Calculator

def run_calculator():
    st.header("Simple Calculator")
    
    num1 = st.number_input("Enter 1st number: ", value=0.0)
    num2 = st.number_input("Enter 2nd number: ", value=0.0)

    operation = st.selectbox("Select an Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    if st.button("Calculate"):
        result = None
        
        if operation == "Addition":
            result = np.add(num1, num2)
        elif operation == "Subtraction":
            result = np.subtract(num1, num2)
        elif operation == "Multiplication":
            result = np.multiply(num1, num2)
        elif operation == "Division":
            if num2 != 0:
                result = np.divide(num1, num2)
            else:
                st.error("Error: Division by zero is mathematically undefined.")
                return

        if result is not None:
            st.success(f"The result of the {operation} is: {result}")

if __name__ == "__main__":
    run_calculator()