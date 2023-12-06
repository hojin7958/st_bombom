import streamlit as st


### 기본셋팅
from cus.run_style import basicStyle
basicStyle()



st.header("	:four_leaf_clover: :green[봄톡], 카카오톡 자동발송")


def intro_page():
    st.write("")
    st.info("""
    :green[봄봄]은 영업에 도움이될 만한 작은 개발 프로젝트들을 하고 있어요  
    아! 이런게 필요한데 라고 생각이 드시면 언제든 메일로 문의주세요  
    bomboms.kr@gmail.com
            """)

def main_page():
    st.write("")
    st.markdown("""
            """)







if __name__ == "__main__":
    intro_page()
    main_page()
    # side_bar()
