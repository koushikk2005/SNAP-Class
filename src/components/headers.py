import streamlit as st

def header_home():

    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
                <div style='display:flex;flex-direction:column;align-items:center;justify-content:center;margin-bottom:20px;margin-top:20px'>
                <img src="{logo_url}" width="100" />
                <h1 style='text_align:center;color:#E0E3FF'>SNAP<br>CLASS</h1>
                </div>
                """,unsafe_allow_html=True)

def header_dashboard():

    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
                <div style='display:flex;align-items:left;justify-content:center;gap:20px'>
                <img src="{logo_url}" width="80" />
                <h2 style='text_align:center;color:#E0E3FF'>SNAP<br>CLASS</h2>
                </div>
                """,unsafe_allow_html=True)