import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY'] 
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('시나리오 써주는 다희봇🥰')
st.subheader('여러분을 환영합니다', divider = 'blue')

keyworld = st.text_input("아무 단어나 입력해보세요!")

if st.button('생성하기'):
    with st.spinner('생성중입니다.'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyworld,
                }, 
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 흥미진진한 시나리오를 300자 이내로 작성해줘",
                }
            ],
            model="gpt-4o",
        )

    result = chat_completion.choices[0].message.content


    st.write(result)
    
    