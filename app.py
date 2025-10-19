from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

from langchain.schema import SystemMessage, HumanMessage


load_dotenv()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


st.title("勉強の質問アプリ（英・数）")
english_teacher_mode = "English teacher"
math_teacher_mode = "Math teacher"

selected_item = st.radio(
    "教えてもらう先生の教科を選択してください。",
    [english_teacher_mode, math_teacher_mode]
)

st.divider()

input_message = st.text_input(label="質問を入力してください。")
if st.button("実行"):
    st.divider()
    st.write("### 回答")

    if input_message:
        system_content = "You are an English teacher." if selected_item == english_teacher_mode else "You are a math teacher."
        conversation_history = [SystemMessage(content=system_content)]
        conversation_history.append(HumanMessage(content=input_message))
        result = llm(conversation_history)
        st.write(result.content)
