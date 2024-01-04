import streamlit as st

### 기본셋팅
from cus.run_style import basicStyle, button_to_page
basicStyle()



st.header("	:four_leaf_clover: :green[봄톡], 카카오톡 자동발송")



def file_download_button(file_name, button_name):
    with open(file_name,'rb') as f:
        st.download_button(button_name, f, file_name=file_name, type="primary", use_container_width=True)


def link_button(button_name, link):
    st.link_button(button_name, url=link, use_container_width=True)



def main_page():
    st.write("")


    with st.expander(label="봄톡 사용법",expanded=True):
        st.markdown("""
        #### 클릭 몇번만 해보세요, 누구나 쉽게 따라할 수 있어요                    
        """)

        st.divider()

        cols_a = st.columns([2,0.5,2])

        with cols_a[0]:
            # st.caption("네이버블로그로 연결되요")
            link_button("**봄톡 사용법 보기**  \n네이버 블로그로 연결되요",'https://blog.naver.com/bombomskr/223293292462')

        with cols_a[2]:
            # st.caption("바로 받으실 수 있어요")
            file_download_button('bomtalk.zip',"**봄톡 다운로드 받기**  \n 폴더에 압축만 풀면 끝")


if __name__ == "__main__":
    # intro_page()
    main_page()

    # file_download_button('manual.pdf',"봄톡 메뉴얼 보기")
    button_to_page("처음으로 다시가기","home")
    # side_bar()
