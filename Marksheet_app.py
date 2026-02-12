import streamlit as st

st.title("Marksheet")

a = st.number_input("Enter marks for Sub1:", min_value=0.0, max_value=100.0)
b = st.number_input("Enter marks for Sub2:", min_value=0.0, max_value=100.0)
c = st.number_input("Enter marks for Sub3:", min_value=0.0, max_value=100.0)
d = st.number_input("Enter marks for Sub4:", min_value=0.0, max_value=100.0)

if st.button("Submit"):
    total = a + b + c + d
    if a > 33 and b > 33 and c > 33 and d > 33:
        per = total / 4
        st.write(f"Total: {total}")
        st.write(f"Percentage: {per}")
        if per > 80:
            st.write("Grade: A+")
        elif 60 < per <= 80:
            st.write("Grade: B+")
        elif 40 < per <= 60:
            st.write("Grade: C+")
        else:
            st.write("Fail")
    else:
        st.write("You failed (mark <33 in some subject).")
