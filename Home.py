from streamlit_extras.switch_page_button import switch_page 
import streamlit as st
import streamlit_authenticator as stauth
from cus import st_style
from cus.dependancies import sign_up, fetch_users
# from st_pages import Page, show_pages, add_page_title
# from cus.run_style import basicStyle



### 기본셋팅
from cus.run_style import basicStyle
basicStyle()



# def max_width_():
#     max_width_str = f"max-width: 1100px;"
#     st.markdown(
#         f"""
#     <style>
#     .appview-container .main .block-container{{
#         {max_width_str}
#     }}
#     </style>    
#     """,
#         unsafe_allow_html=True,
#     )


# max_width_()


# st.set_page_config(page_title="후추톡, 영업에 맛있는 후추를 톡톡",page_icon=":elevator:", layout="wide")
# st_style.max_width_()
# st_style.hide_streamlit_style_()
# st_style.hide_toppadding_()




st.header("	:four_leaf_clover: :green[봄봄], 영업에 봄이와요")

### 프론트


def intro_page():
    st.write("")
    st.info("""
    :green[봄봄]은 영업에 도움이될 만한 작은 개발 프로젝트들을 하고 있어요  
    아! 이런게 필요한데 라고 생각이 드시면 언제든 메일로 문의주세요  
    bomboms.kr@gmail.com
            """)





def main_page():
    st.subheader("")
    st.markdown("""
    \n
    :green[봄봄] 첫번째 프로젝트 🖐️
   
    #### :green[봄톡] 카카오톡 자동발송 - 고객관리를 도와드려요  
    """)

    with st.expander(label="봄톡이 뭐에요?",expanded=True):
        st.markdown("""
        ##### 카톡에 등록된 친구 :red[수백명에게 자동]으로 메시지를 보낼 수 있어요
        클릭 몇번만 해보세요, 누구나 쉽게 따라할 수 있어요
        """)


    with st.expander(label="봄톡은 무료?유료?",expanded=True):
        st.markdown("""
        ##### :red[무료]로 얼마든지 사용하세요
        **봄봄도 먹고 살아야하니깐 2024년 어느날 한달 이용료는 [커피한잔 값...] 정도로 유료화 계획이 있어요
        """)

    with st.expander(label="봄톡 사용방법은?",expanded=True):
        st.markdown("""
        ##### 윈도우 :red[메모장] 사용해봤다면 누구나 가능
        친구리스트 관리는 메모장(txt파일)을 활용하면 금방할 수 있어요  
        **자세한 사항은 메뉴얼을 참고해주세요
        """)



    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        moveto_Downloadpage = st.button("봄톡 사용해보기", type="primary")
        if moveto_Downloadpage:
            switch_page('봄톡')




### 사이드바

def side_bar():
    pass
    # with st.sidebar:
    #     st.write("사이드바제목")



if __name__ == "__main__":
    intro_page()
    main_page()
    side_bar()


