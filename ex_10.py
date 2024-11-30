# df_final = df_final.drop(columns='Index_text')
# df_final = df_final.rename(columns={df_final.columns[0]: 'spoken_words'})
# df_final.to_csv("ex_10.csv")

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from langchain_google_genai import ChatGoogleGenerativeAI

df = pd.read_csv("ex_10.csv")
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyDUm58IAr5Ufp6kTw-HWRKnIoU0hBBI-qc")

prompt_start = f"""
You are a data scientist specialized in analysing entertainment content. You are working on the show series
"The Simpsons", investigating patterns in the series and the most importance things is understand the columns and give an anylises based on anylise of sentiment:
Generate a string with anylises, the labels must be, positive, neutral and negative
Columns:
{df.columns}

Full data:
{df}
"""
resposta_1 = llm.invoke(prompt_start).content

prompt_code = f"""
Based on this anylises you must generate a code in python that read the sentiment analysis result and create a pie chart showing the proportion of speech categories in the episode in a apliccation streamlit only using matplotlib.
only generate the code ready to execute, no need explanations!
The analyses is:
{resposta_1}
"""
resposta_2 = llm.invoke(prompt_code).content

prompt_code_validation = f"""
Based on this code this must be ready to execute in streamlit, transform this in only code! and exclude the imports and exclude the ``` and ```pyton :
{resposta_2}
"""
resposta_3 = llm.invoke(prompt_code_validation).content

print(f"ultimo: {resposta_3}")

def code_llm():
    st.title("Código advindo da LLM")
    resposta_3


def Main():
    code_llm()

if __name__ == "__main__":
    Main()