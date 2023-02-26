import streamlit as st

st.title("Rakesh Data App")

st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :wave:")
    st.subheader("To know more :point_down:")
    st.subheader("My Linked in id")
    st.markdown("https://www.linkedin.com/in/vemulapalli-sai-rakesh-2702a7203/")
    st.balloons()