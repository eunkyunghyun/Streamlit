import streamlit as st
import PIL.Image
import os

st.title("Pystagram")
col1, col2, col3 = st.columns(3)
if 'email' not in st.session_state:
    st.session_state['email'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''
if 'session' not in st.session_state:
    st.session_state['session'] = False

with col1:
    st.header("회원가입")
    email = st.text_input("이메일을 입력하세요.", key="<1>")
    password = st.text_input("비밀번호를 입력하세요.", type='password', key="<2>")
    f = open("accounts.txt", 'r')
    accounts = f.readlines()
    if st.button("회원가입"):
        flag = 0
        for account in accounts:
            if email == account.split(',')[0]:
                flag = 1
                break
        f.close()
        if flag == 1:
            st.write("이메일이 중복됩니다.")
        else:
            st.write("회원가입이 완료되었습니다. 축하합니다!")
            f = open("accounts.txt", 'a')
            f.write("\n{},{}".format(email, password))
            f.close()
            st.session_state['email'] = email
            st.session_state['password'] = password
            st.session_state['session'] = True

with col2:
    st.header("로그인")
    email1 = st.text_input("이메일을 입력하세요.", key="<3>")
    password1 = st.text_input("비밀번호를 입력하세요.", type='password', key="<4>")
    f = open("accounts.txt", 'r')
    accounts = f.readlines()
    if st.button("로그인"):
        flag = 0
        for account in accounts:
            if account.split(',')[0] == email1 and account.split(',')[1].strip('\n') == password1:
                flag = 1
                break
        if flag == 1:
            st.write("로그인이 완료되었습니다!")
            st.session_state['email'] = email1
            st.session_state['password'] = password1
            st.session_state['session'] = True
        else:
            if account.split(',')[0] != email1:
                st.write("이메일을 잘못 입력했습니다.")
            elif account.split(',')[1] != password1:
                st.write("비밀번호를 잘못 입력했습니다.")
        f.close()

with col3:
    st.header("로그아웃")
    if st.session_state['session']:
        if st.button("로그아웃"):
            st.write("로그아웃이 완료되었습니다.")
            st.session_state['email'] = ""
            st.session_state['password'] = ""
            st.session_state['session'] = False

with col1:
    if st.session_state['session']:
        st.header("포스트 게시판")
        f = open("post/posts", 'r')
        posts = f.readlines()
        for post in posts:
            st.write(post + '\n')
        f.close()
        post = st.text_input("포스트를 작성하세요.")
        button = st.button("업로드")
        if button:
            f = open("post/posts", 'a')
            f.write("{}: {}\n".format(st.session_state['email'], post))
            f.close()
            st.write("포스트 작성이 완료되었습니다.")

with col2:
    if st.session_state['session']:
        st.header("사진 게시판")
        images = os.listdir("media/")
        for image in images:
            img = PIL.Image.open("media/" + image)
            st.image(img, use_column_width=True)
        file = st.file_uploader("사진을 업로드하세요.", type=["jpg", "jpeg", "png"])
        if file is not None:
            img = PIL.Image.open(file)
            images = os.listdir("media/")
            images.sort(reverse=True)
            try:
                img.save("media/photo{}.png".format(int(images[0][5]) + 1), 'PNG')
            except IndexError:
                img.save("media/photo1.png", 'PNG')
            st.image(img, use_column_width=True)
            button2 = st.button("업로드", key="<5>")
            if button2:
                st.write("사진 업로드가 완료되었습니다.")

st.write("© 2022. All rights reserved.")
