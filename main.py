import streamlit as st
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client = genai.Client()

#st.title("🌍 Travel Assistant")


import streamlit as st

# Custom CSS for 3D Animations, Plane, and Layout
st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #6dd5fa 100%);
        background-attachment: fixed;
    }

    /* The Flying Airplane */
    .plane {
        position: fixed;
        top: 20%;
        left: -100px;
        font-size: 50px;
        animation: fly 15s linear infinite;
        z-index: 1000;
    }

    @keyframes fly {
        0% { left: -100px; transform: rotate(0deg); }
        50% { left: 100%; transform: rotate(10deg); }
        51% { transform: scaleX(-1) rotate(10deg); }
        100% { left: -100px; transform: scaleX(-1) rotate(0deg); }
    }

    /* Heading Styling */
    .main-title {
        text-align: center;
        color: #ffffff;
        font-family: 'Arial Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: 5px;
        padding-top: 50px;
        text-shadow: 4px 4px 10px rgba(0,0,0,0.5);
    }

    /* 3D Sticker Container */
    .sticker {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px 0 rgba(0,0,0,0.37);
        text-align: center;
        transition: transform 0.3s;
    }
    .sticker:hover { transform: translateY(-10px); }
    </style>
""", unsafe_allow_html=True)

# Inject the Airplane
st.markdown('<div class="plane">✈️</div>', unsafe_allow_html=True)

# Main Title
st.markdown('<h1 class="main-title">Travel Assistant AI</h1>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 3D Sticker Grid
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="sticker"><h3>🌍</h3><p>Global Mapping</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="sticker"><h3>🏨</h3><p>Smart Booking</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="sticker"><h3>📸</h3><p>Hidden Gems</p></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Input Area
with st.container():
    st.markdown("""
    <div style="background: rgba(0,0,0,0.2); padding: 30px; border-radius: 15px;">
        <h3 style="color: white; text-align: center;">Ready for takeoff?</h3>
    </div>
    """, unsafe_allow_html=True)
    
    destination = st.text_input("", placeholder="Where is your dream destination?")
    if destination:
        st.balloons()
        st.info(f"Charting a course for {destination}...")
        
location=st.text_input("where you want to go")
days=st.number_input("how many days you want to go",min_value=1,max_value=30)

budget=st.selectbox("select your budget",["luxury","moderate","budgeted"])
travel=st.radio("who you are tavellling with",["solo","family","friends"])

prompt=f"""you are travel pllaner user is saying he/she wants to go 
to{location}for{days}days , he is budget of type {budget}
travel type is {travel}"""
 
if st.button("plan trip"):
    interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input=prompt)

    with st.spinner("Wait for it...", show_time=True):
        time.sleep(5)
    st.success("here are some suggestions")
    st.write(interaction.output_text)