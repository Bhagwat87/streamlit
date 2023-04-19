import streamlit as st
st.set_page_config (page_title= "My Webpage")
st.subheader("Hi, I am Bhagwat")
st.title("A Data Analyst")
st.write("I am passonate aboute data science")
a = st.number_input("Insert a number A")
b = st.number_input("Insert a number B")
c = st.number_input("Insert a number C")

def largest(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	elif c>=a and c>=b:
		return c
largest_number = largest(a,b,c)

st.write("Largest Number is:", largest_number)
