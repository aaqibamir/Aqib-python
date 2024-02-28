import streamlit as st

# Title
st.title('College Admission System')




# Sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home', 'Add Student', "View student",'Contact Us', 'About Us'])

# Main content
if page == 'Home':
    st.write('Welcome to the College Admission System!')



# Function to add student data
def add_student_data():
    st.title('Add Student Data')
    # Add input fields for student data
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0, max_value=150)
    address = st.text_input('Address')
    # Add a button to submit the data
    if st.button('Submit'):
        # Once submitted, display the confirmation message
        st.success('Student data submitted successfully!')

# Function to view student data
def view_student_data():
    st.title('View Student Data')
    # Display a placeholder for the student data
    student_data = None  # Placeholder, you would retrieve actual data here
    if student_data is not None:
        st.write('### Student Data')
        st.write(student_data)
    else:
        st.write('No student data available.')

# Main function to control the app flow
def main():
    # Add navigation to switch between input and view pages
    page = st.sidebar.radio('Navigation', ['Add Student Data', 'View Student Data'])

    # Conditionally display pages based on navigation choice
    if page == 'Add Student Data':
        add_student_data()
    elif page == 'view Student Data':
        view_student_data()
        

if __name__ == '__main__':
    main()



elif page == 'Contact Us':
    st.header('Contact Us')
    # Add contact information
    st.write('Email : ubaidmemon530@gmail.com\n Phone : 03216740458')
elif page == 'About Us':
    st.header('About Us')
    # Add information about the college
    st.write("this is a banoqabil assignment home page about us add student view student and contact us" )
        
    
