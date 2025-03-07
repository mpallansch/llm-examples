from openai import AzureOpenAI
import streamlit as st

with st.sidebar:
    st.text_input("OpenAI API Endpoint", key="chatbot_api_endpoint", type="password")
    st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

st.title("Press Release")
st.caption("Takes the content of an article written for a technical audience and rewrites it as a press release.")

prompt = st.text_area(
    "Article contents...",
)

if st.button("Rewrite"):
    if not st.session_state["chatbot_api_key"] or not  st.session_state["chatbot_api_endpoint"]:
            st.info("Please add your OpenAI API endpoint and key to continue.")
            st.stop()

    client = AzureOpenAI(
        api_key = st.session_state["chatbot_api_key"],
        api_version = "2024-02-01",
        azure_endpoint = st.session_state["chatbot_api_endpoint"]
    )

    response = client.chat.completions.create(model="gpt-4o", messages=[
        {"role": "system", "content": "The following is an article written for a technical audience. Rewrite it as a press release."},
        {"role": "user", "content": prompt}
    ])
    msg = response.choices[0].message.content
    st.write(msg)
