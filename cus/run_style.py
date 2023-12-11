from cus import st_style
import streamlit as st
from streamlit_extras.switch_page_button import switch_page 



def basicStyle():
    ### 기본셋팅
    st.set_page_config(page_title="봄봄, 영업에 봄을 찾아드려요",page_icon=":four_leaf_clover:", layout="wide",initial_sidebar_state="collapsed")
    st_style.max_width_()
    st_style.hide_streamlit_style_()
    st_style.hide_toppadding_()





def button_to_page(button_name = "임시", goto_page="봄톡"):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        moveto_Downloadpage = st.button(button_name, type="secondary", use_container_width=True)
        if moveto_Downloadpage:
            switch_page(goto_page)
