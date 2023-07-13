import streamlit as st
import numpy as np
import pandas as pd


#Containers
header=st.container()
input=st.container()
grades=st.container()
results=st.container()
info=st.container()


#Functions
@st.cache_data
def get_result(grades,credits):
    result=0
    for i in range(len(grades)):
        result+=grades[i]*credits[i]
    result/=sum(credits)
    return round(result,2)

#Functionalities
with header:
    st.title("SGPA Calcultor")
    st.subheader("This App gives the Semister Grade Point Average.")
    

with input:

    st.header("Enter the Number of Subjects and Make Sure to Check the Box")
    no_of_sub=st.number_input("no.of subjects",1,20)

    st.write("You Have Entered",no_of_sub,"Subject(s)","\nClick on the below button to enter the grades and credits")

    checked=st.checkbox("Confirm That you Entered Correct Number Of Subjects")
    


with grades:
    grades=[]
    credits=[]
    grades_disp,credits_disp=st.columns(2)
    if(checked==True ):
        st.write("Enter the Grades Here")
        grade_map={"o":10,"s":9,"a":8,"b":7,"c":6,"d":5,"f":0,"p":0}
        for i in range(no_of_sub):
            gr=grades_disp.text_input("subject"+str(i+1)+" grade","o")
            cr=credits_disp.text_input("subject"+str(i+1)+" credit",3)
            grades.append(grade_map[gr.lower()])
            credits.append(float(cr))
        clicked=st.button("Check Result")

with results:
    if(checked==False):
        a=0
    elif(clicked==True):
        st.success("Results Sucessfully Fetched")
        result=get_result(grades,credits)
        st.write(result)
with info:
    st.header("Results Are Calculated Based on This Table")
    data=pd.DataFrame(data=["o","s","a","b","c","d","f","p"],index=[10,9,8,7,6,5,0,0],columns=["Points"])
    data.index.rename('Row', inplace=True)
    st.table(data)
