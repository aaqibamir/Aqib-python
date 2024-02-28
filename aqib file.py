import streamlit as st
import pandas as pd

# Create a dataframe to store admitted students' information
admitted_students = pd.DataFrame(columns=["Name", "Roll No.", "Department", "Score"])

# Function to admit a student
def admit_student(name, roll_no, department, score):
    global admitted_students
    admitted_students = admitted_students.append({"Name": name, "Roll No.": roll_no, "Department": department, "Score": score}, ignore_index=True)
    st.success("Student admitted successfully!")

# Function to display admitted students
def display_admitted_students():
    st.header("Admitted Students")
    st.write(admitted_students)

def main():
    st.title("College Admission System")

    menu = ["Home", "Apply for Admission", "View Admitted Students"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to College Admission System")

    elif choice == "Apply for Admission":
        st.subheader("Apply for Admission")
        name = st.text_input("Name")
        roll_no = st.text_input("Roll No.")
        department = st.text_input("Department")
        score = st.number_input("Score", min_value=0)
        if st.button("Apply"):
            admit_student(name, roll_no, department, score)

    elif choice == "View Admitted Students":
        display_admitted_students()

if __name__ == "__main__":
    main()