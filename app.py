import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY'] 
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('후킹한 홍보글 써드려요🥰')
st.subheader('키워드를 입력하면 후킹한 홍보글을 써드립니다!', divider = 'blue')

keyworld = st.text_input("단어를 하나만 입력하세요!")

if st.button('생성하기'):
    with st.spinner('글과 이미지를 생성중입니다.'):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyworld,
                }, 
                {
                    "role": "system",
                    "content": "입력 받은 키워드에 대한 150자 이내의 흥미진진하고 마음을 사로잡는 홍보글을 써줘",
                }
            ],
            model="gpt-4o",
        )
        response = client.images.generate(
            model="dall-e-3",
            prompt=keyworld,
            size="1024x1024",
            quality="standard",
            n=1,
        )
    result = chat_completion.choices[0].message.content
    image_url = response.data[0].url

    st.write(result)
    st.image(image_url)
    
    
