import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY'] 
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('일기 대신써드립니다🥰')
st.subheader('감정 단어를 적으면 일기가 나와요!', divider = 'blue')

keyworld = st.text_input("오늘의 감정을 단어로 입력해보세요!")

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
                    "content": "입력 받은 키워드에 대한 150자 이내의 간단한 일기를 작성해줘",
                }
            ],
            model="gpt-4o",
        )
        response = client.images.generate(
            model="dall-e-3",
            prompt='f{keyworld}, 색연필로 그린듯하게 그려줘',
            size="1024x1024",
            quality="standard",
            n=1,
        )
    result = chat_completion.choices[0].message.content
    image_url = response.data[0].url

    st.write(result)
    st.image(image_url)
    
    