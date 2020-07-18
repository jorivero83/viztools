import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

def main():

    menu = ['Home','Sweetviz']
    choice = st.sidebar.selectbox('Menu', menu)
    if choice == 'Sweetviz':
        st.subheader("Automated EDA with Sweetviz")
    else:
        st.subheader("Home")

if __name__ == '__main__':
    main()