import streamlit as st


def max_width_():
    max_width_str = f"max-width: 1100px;"
    st.markdown(
        f"""
    <style>
    .appview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )



def hide_streamlit_style_():
    ### 여기부터는 햄버거 메뉴 없애는 곳들
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                [data-testid="collapsedControl"] {
                    display: none
                }
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def hide_toppadding_():
    st.markdown("""
            <style>
                .block-container {
                        padding-top: 0rem;
                        padding-bottom: 0rem;
                    }
            </style>
            """, unsafe_allow_html=True)
    


## 스트림릿 메뉴만 없애는것

def hide_streamlit_style2_():
    ### 여기부터는 햄버거 메뉴 없애는 곳들
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
