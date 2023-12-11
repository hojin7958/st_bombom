import streamlit as st
from streamlit_extras.switch_page_button import switch_page 

### 기본셋팅
from cus.run_style import basicStyle, button_to_page
basicStyle()



st.header("	:four_leaf_clover: :green[봄톡], 카카오톡 자동발송")


def main_page():
    st.write("")


    with st.expander(label="봄톡 사용법",expanded=True):
        st.markdown("""
        #### 클릭 몇번만 해보세요, 누구나 쉽게 따라할 수 있어요
        #### 메뉴얼 제작중이에요 (23.12.1일기준)
                    
        1. 파일다운로드받고 편한 위치에 압축풀기
        (예. C:bomtalk 이라고 폴더를 만들어서 압축해제)
        2. 실행하기 (안전하지~~~ 않은 프로그램이라고 나와도 실행계속)

        """)


def file_download_button(file_name, button_name):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        with open(file_name,'rb') as f:
            st.download_button(button_name, f, file_name=file_name, type="primary", use_container_width=True)




if __name__ == "__main__":
    # intro_page()
    main_page()
    file_download_button('bomtalk.zip',"봄톡 다운로드 받기")
    
    # file_download_button('manual.pdf',"봄톡 메뉴얼 보기")
    button_to_page("처음으로 다시가기","home")
    # side_bar()
