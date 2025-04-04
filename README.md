# ✨ Linear System Solver

This repository contains a Python script that solves a system of linear equations using **NumPy**. The script provides **two methods** for solving the system:

- ✅ **Using `np.linalg.solve()`**: A direct and efficient method for solving linear equations.
- 🧠 **Using matrix inverse**: An alternative method (if the matrix is invertible).

---

## ⭐ Repository Name: `linear-system-solver`

---

## 📑 Table of Contents

1. [📜 Description](#-description)
2. [🔧 Cloning the Repository](#-cloning-the-repository)
3. [📦 Installing Dependencies](#-installing-dependencies)
4. [▶️ Running the Code](#️-running-the-code)
5. [📊 Expected Output](#-expected-output)
6. [⚠️ Error Handling](#-error-handling)
7. [🤝 How to Contribute](#-how-to-contribute)
8. [📄 License](#-license)
9. [🌟 Starring the Repository](#-starring-the-repository)

---

## 📜 Description

This project solves a system of linear equations in the form:

A * X = B


Where:
- `A` is the coefficient matrix
- `X` is the vector of unknowns
- `B` is the constant vector

### 🧮 Methods Used

- **`np.linalg.solve()`**: Efficient built-in solver from NumPy.
- **Matrix Inverse**: Calculates the inverse of `A` and multiplies with `B`.

---

### 📘 Example

Solving the system of equations:

2x + 3y = 8
3x + 4y = 11


The output will be:

x = 1
y = 2


---

## 🔧 Cloning the Repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/M-Aitisam/linear-system-solver.git
cd linear-system-solver


📦 Installing Dependencies
This project requires NumPy & streamlit. To install it, run:

pip install numpy
pip install streamlit

▶️ Running the Code
To run the Python script, use the following command:

python linearalgebra.py

If you are using Streamlit, run this instead:

streamlit run linearalgebra.py

📊 Expected Output
When running with the provided example, you will see:

Solving using np.linalg.solve()...

Solution:
x = 1.0
y = 2.0

Solving using matrix inverse...
Solution using matrix inverse:
x = 1.0
y = 2.0

⚠️ Error Handling
If the system has no solution or infinite solutions, the script will notify you.

If the matrix A is not invertible, it will handle that error gracefully.

🤝 How to Contribute
Fork the repository 🔱
Clone your fork locally:

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🌟 Starring the Repository
If you found this project helpful, please give it a ⭐ to show your support!

Go to the GitHub repository

Click the Star button at the top right of the page

Your support helps others discover this project! 🙌
