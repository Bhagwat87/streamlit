import streamlit as st
st.set_page_config (page_title= "My Webpage")
st.subheader("Find the largest, among the 3 given numbers")
a = st.number_input("Insert a number A")
b = st.number_input("Insert a number B")
c = st.number_input("Insert a number C")

def largest(a,b,c):
	if a>=b and a>=c:
		return a, 'A'
	elif b>=a and b>=c:
		return b, 'B'
	elif c>=a and c>=b:
		return c, 'C'
largest_number, name = largest(a,b,c)

st.write("Largest Number is:", name,', ' 'Value is:', largest_number)
