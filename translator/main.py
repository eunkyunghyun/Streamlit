import streamlit as st
import urllib.request
import json


def main():
    f = open("/home/eun/PycharmProjects/education_py/Translator/client_info", 'r')
    lines = f.readlines()
    client_id = lines[0].strip('\n')
    client_secret = lines[1]

    languages = ["ko", "ja", "en", "es", "fr", "de", "vi", "id", "th", "ru", "it"]

    src = st.selectbox("", tuple(languages))
    languages.remove(src)
    tar = st.selectbox("", tuple(languages))

    srcText = st.text_area(src, "안녕하세요!")

    encText = urllib.parse.quote(srcText)
    data = "source=" + src + "&target=" + tar + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if st.button("Confirm"):
        if rescode == 200:
            response_body = response.read()

            res = json.loads(response_body.decode('utf-8'))
            from pprint import pprint
            pprint(res)

            st.text_area(tar, res['message']['result']['translatedText'])
        else:
            print("Error Code: " + rescode)


if __name__ == "__main__":
    main()
