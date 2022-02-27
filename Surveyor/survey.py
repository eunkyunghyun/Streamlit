import streamlit as st
import os

st.title("설문조사")

contents = "이 설문조사는 여러분의 진로 상태를 점검하기 위해 개설되었습니다." \
           "<br>타인의 정보를 도용하려는 목적으로 사용할 시 <strong>개인정보보호법에 의거하여 처벌</strong>받을 수 있습니다!"
caution = '<p style="color:Red;">{}</p>'.format(contents)
st.markdown(caution, unsafe_allow_html=True)

date = st.date_input("날짜")
gender = st.selectbox("성별은 무엇입니까?", ("남성", "여성", "모름"))
school = st.selectbox("어떤 학교에 다닙니까?", ("초등학교", "중학교", "고등학교"))
if school == "초등학교":
    grade = st.number_input("몇 학년입니까?", 1, 6)
else:
    grade = st.number_input("몇 학년입니까?", 1, 3)
if school == "고등학교":
    record = st.number_input("평균 등급은 무엇입니까?", 1, 9)
else:
    record = st.number_input("평균 성적은 얼마입니까?", 0, 100)
subjects = ("국어", "영어", "수학", "사회", "과학", "기술가정", "정보", "한문", "음악", "미술", "체육", "없음")
option = st.multiselect("선호하는 과목은 무엇입니까? (단, '없음'으로 선택하면 다른 과목은 배제됩니다.)", subjects)
emotion = st.slider("최근 일주일 평균의 기분 상태를 표현하십시오. (단, 수치가 높을수록 기분이 좋은 상태입니다.)", 0.0, 100.0, (0.0, 100.0))

if st.checkbox("로봇이 아닙니다."):
    average = (emotion[0] + emotion[1]) // 2
    if average >= 75:
        emotion = "매우 양호함"
    elif average >= 50:
        emotion = "양호함"
    elif average >= 25:
        emotion = "심각함"
    elif average >= 0:
        emotion = "매우 심각함"
    if '없음' in option:
        option = ['없음']
    if st.button("제출하기"):
        st.write("제출이 성공적으로 완료되었습니다.")
        people = sorted(os.listdir("./people/"), reverse=True)
        if len(people) == 0:
            f = open("./people/person1.txt", 'a', encoding='utf8')
            f.write("{}, {}, {}, {}, {}, {}, {}".format(date, gender, school,
                                                        grade, record, option, emotion))
        else:
            number = int(people[0].strip("person").strip(".txt"))
            f = open("./people/person{}.txt".format(number + 1), 'a', encoding='utf8')
            items = [['날짜', date], ['성별', gender], ['학교', school],
                    ['학년', grade], ['성적', record], ['과목', option], ['기분', emotion]]
            for item in items:
                f.write("{}: {}\n".format(item[0], item[1]))
        f.close()
