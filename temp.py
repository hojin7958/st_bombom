import streamlit as st
from send_sms import send_sms
import random

st.set_page_config("임시")


def make_verify_code():
    global verify_code
    verify_code = random.randrange(1001,9999)
    return verify_code


phone = st.text_input("핸드폰번호를 입력해주세요")
verify_phone_btn = st.button("인증번호 보내기", on_click=make_verify_code)



if phone:

    print(f"{str(phone)} 후추톡 인증번호\n 후추톡 인증번호를 알려드려요\n{verify_code}")

    send_sms(str(phone),"후추톡 인증번호",f"후추톡 인증번호를 알려드려요\n{verify_code}")
