import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
st.set_page_config(page_title="SLOGAN MACHINE")
st.title('SLOGAN MACHINE')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
def generate_response(topic):
  llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
  template = """Act as a head of the advertising department.
            Create 10 slogan for {Topic}
            List of 10 suggestions in table, one suggestion per row.
            Each row should have 2 columns:
            - "slogan" - what the slogan is
            - "reason" - explain why the slogan is proper for the product
            """
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  response = llm(prompt_query)
  return st.info(response)
with st.form('myform'):
  topic_text = st.text_input('Enter products with details on its uses and branding:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(topic_text)