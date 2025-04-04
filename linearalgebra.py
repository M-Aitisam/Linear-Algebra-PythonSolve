# streamlit_app.py

import streamlit as st
import numpy as np

st.title("🧮 Linear System Solver")

def solve_linear_system(A, B):
    try:
        X = np.linalg.solve(A, B)
        st.success("✅ Solution using np.linalg.solve():")
        st.write(f"x = {X[0]}")
        st.write(f"y = {X[1]}")
        return X
    except np.linalg.LinAlgError as e:
        st.error(f"❌ Error: {e}")
        return None

def solve_using_inverse(A, B):
    try:
        A_inv = np.linalg.inv(A)
        X = np.dot(A_inv, B)
        st.success("📐 Solution using matrix inverse:")
        st.write(f"x = {X[0]}")
        st.write(f"y = {X[1]}")
        return X
    except np.linalg.LinAlgError as e:
        st.error(f"❌ Error: {e}")
        return None

# User input
st.subheader("Enter coefficients for the equations:")
a11 = st.number_input("A[0][0]", value=2.0)
a12 = st.number_input("A[0][1]", value=3.0)
a21 = st.number_input("A[1][0]", value=3.0)
a22 = st.number_input("A[1][1]", value=4.0)

b1 = st.number_input("B[0]", value=8.0)
b2 = st.number_input("B[1]", value=11.0)

A = np.array([[a11, a12], [a21, a22]])
B = np.array([b1, b2])

if st.button("Solve Equations"):
    st.divider()
    st.write("🔧 Solving using `np.linalg.solve()`...")
    solution1 = solve_linear_system(A, B)
    
    st.divider()
    st.write("🔁 Solving using matrix inverse...")
    solution2 = solve_using_inverse(A, B)
