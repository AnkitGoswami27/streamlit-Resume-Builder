import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="Resume Builder",layout="wide"
)

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
st.image('https://media.cybernews.com/images/featured-big/2023/02/best-website-builders_1.jpg')
st.title("THE BEST ONLINE RESUME BUILDER")
st.subheader("A good resume objective does three things: Describes your skills, educational background, and certifications that are's relevant to the job you're applying for.")
st.write("Professional out-of-the-box resumes, instantly generated by the most advanced resume builder technology available.")
st.write("Effortless crafting. Real-time preview & pre-written resume examples.Dozens of HR-approved resume templates.")


want_to_contribute = st.button("Create My Resume")


if want_to_contribute:
        
        switch_page("Resume Builder")
        st.balloons()
       
        

  


st_lottie(lottie_coding,height=300,key="coding")