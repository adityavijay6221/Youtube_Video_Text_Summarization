import streamlit as st




st.title('Youtube video Summarization App using Langchain and GROQ LLM')
st.subheader('Summarize youtube url')

#GROQ API KEY
with st.sidebar:
    api_key = st.text_input("Enter your GROQ API key", type="password")
    
#LLM
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant", api_key=api_key, temperature=0.7)   

#TEMPLATE
from langchain_classic.prompts import PromptTemplate
template="""Summarize the following text in a concise manner:
{text}"""
prompt=PromptTemplate(input_variables=["text"], template=template)

#DOCUMENT LOADER
url=st.text_input("Enter YouTube Video URL")

if st.button("Summarize"):
    from langchain_community.document_loaders.youtube import YoutubeLoader
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    docs=loader.load()

    #SUMMARIZATION CHAIN
    from langchain_classic.chains.summarize import load_summarize_chain
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt,verbose=True)
    summary = chain.run(docs)

    st.subheader("Summary:")
    st.write(summary) 