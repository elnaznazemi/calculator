Calculator Application Documentation
Introduction
The Calculator application is a simple graphical calculator implemented in Python using the Tkinter library. It provides a user-friendly interface for performing basic arithmetic operations, including addition, subtraction, multiplication, and division. The calculator also supports other mathematical functions such as square root, exponentiation, percentage, and decimal input.

Features
1. Arithmetic Operations
Addition (+): Adds two numbers.
Subtraction (-): Subtracts the second number from the first.
Multiplication (*): Multiplies two numbers.
Division (/): Divides the first number by the second. Note: Division by zero is not handled explicitly.
2. Other Operations
Exponentiation ():** Raises the first number to the power of the second.
Square Root (√): Calculates the square root of the input.
Percentage (%): Converts the input to a percentage.
3. Additional Input
Decimal (.): Appends a decimal point to the input.
4. Clear and Equal Buttons
Clear (C): Clears the input field.
Equal (=): Evaluates and displays the result of the mathematical expression.

Usage
Numeric Buttons (0-9): Click on these buttons to input numeric values.
**Operation Buttons (+, -, *, /, , √, %): Click on these buttons to perform the corresponding mathematical operations.
Decimal Button (.): Click to add a decimal point to the input.
Clear Button (C): Click to clear the input field.
Equal Button (=): Click to calculate and display the result.

Notes
Division by zero will result in an error message.
The square root operation is applied immediately upon pressing the square root button.
Percentage is applied to the entire expression.
The calculator follows standard order of operations.
Code Structure
The code is organized into functions for button actions, promoting a modular approach for improved readability and maintainability.

Dependencies
Python 3.x
Tkinter library

How to Run
Ensure Python is installed on your system.
Run the Python script containing the calculator code:
"python calculator_script.py"

Conclusion
This Calculator application provides a straightforward interface for performing basic mathematical calculations. It serves as a foundation that can be extended to include more advanced features or tailored to specific requirements.
