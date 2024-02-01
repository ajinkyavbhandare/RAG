from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chains import VectorDBQA
from chromadb.api import API
import chainlit as cl
import chromadb


######################################################################################
client = chromadb.PersistentClient(path="/db/")
persist_directory = '/db/'

embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

HUGGINGFACEHUB_API_TOKEN="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"
repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
                     repo_id=repo_id,
                     model_kwargs={"temperature":0.3, "max_new_tokens":200})

vectordbp = Chroma(client=client, embedding_function=embedding)
qa = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=vectordbp)


@cl.on_message
async def main(message: cl.Message):
    # Access the message content using message.content
    response = qa.run(message.content)
    await cl.Message(content=response).send()