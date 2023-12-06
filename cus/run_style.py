from cus import st_style
import streamlit as st







def basicStyle():
    ### 기본셋팅
    st.set_page_config(page_title="봄봄, 영업에 봄을 찾아드려요",page_icon=":four_leaf_clover:", layout="wide",initial_sidebar_state="collapsed")
    st_style.max_width_()
    st_style.hide_streamlit_style2_()
    st_style.hide_toppadding_()
