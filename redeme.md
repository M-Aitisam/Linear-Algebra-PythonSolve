Linear System Solver ✨
This repository contains a Python script that solves a system of linear equations using NumPy. The script offers two methods for solving the system:

Using np.linalg.solve(): A direct and efficient method for solving linear equations.

Using matrix inverse: An alternative method for solving the system, if the matrix is invertible.


Repository Name: linear-system-solver ⭐

Table of Contents
Description 📜

Cloning the Repository 🔧

Installing Dependencies 📦

Running the Code ▶️

Expected Output 📊

Error Handling ⚠️

How to Contribute 🤝

License 📄

Starring the Repository ⭐

Description 📜
This project solves a system of linear equations of the form:

A * X = B

Where A is the coefficient matrix, X is the vector of unknowns (the values you're trying to solve for), and B is the constant vector.

Methods Used:
np.linalg.solve(): This method directly solves the system and is fast and efficient.

Matrix Inverse: This method computes the inverse of matrix A and multiplies it with B to find X (the solution vector).

Example
For the system of equations:

2x + 3y = 8
3x + 4y = 11

The solution is:

x = 1 y = 2

Cloning the Repository 🔧
To get started with this repository, follow these steps:

Open a terminal or command prompt.

Clone the repository to your local machine using the following command:


git clone https://github.com/M-Aitisam/linear-system-solver.git
Navigate to the project directory:

cd linear-system-solver

Installing Dependencies 📦
This project requires NumPy for matrix operations. To install NumPy, run the following command:

pip install numpy

Running the Code ▶️
Once the dependencies are installed, you can run the Python script to solve the linear system by executing the following command:

python linearalgebra.py

Expected Output 📊
When running the code with the provided example, the expected output will be:

Solving using np.linalg.solve()...

Solution:
x = 1.0
y = 2.0

Solving using matrix inverse...
Solution using matrix inverse:

x = 1.0
y = 2.0

Error Handling ⚠️
If the system has no solution or infinite solutions, the script will catch the error and notify the user.

If the matrix is not invertible (i.e., singular), the script will also handle that case gracefully.


License 📄
This project is open-source and available under the MIT License. See the LICENSE file for more details.

Starring the Repository ⭐

If you found this project helpful, please star the repository to show your support! 🌟

Go to the repository on GitHub.

Click the Star button at the top right of the page.

Stars are a great way to show appreciation and help others discover this project! 🚀
