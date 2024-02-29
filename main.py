##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##GemmaChat
#######################################################################################################
#Importing dependecies
#######################################################################################################
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
import chainlit as cl
#######################################################################################################
@cl.on_chat_start
async def on_chat_start():
    
    # Sending an image with the local file path
    elements = [
    cl.Image(name="image1", display="inline", path="gemma.jpeg")
    ]
    await cl.Message(content="Hello there, I am GemmaChat by Tushar Aggarwal. I am running locally on Ollama How can I help you ?", elements=elements).send()
    model = Ollama(model="gemma:2b")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """Please act as an expert in providing smart chat responses.
                Your responses should be friendly, simple, and jargon-free, suitable for beginners. When responding, consider using a mix of paragraphs and bullets to convey information effectively. Topics to cover include
                - Introduction to smart chat responses
                - Importance of tone in chat interactions
                - Tips for maintaining a friendly demeanor
                - Examples of beginner-friendly responses
                - Strategies for engaging users effectively
                - Handling common challenges in chat conversations
                - Include examples of tone variations (e.g., formal, casual, informative)
                - Provide guidance on adapting responses based on user input
                - Suggest ways to personalize responses for different users
                - Offer insights on building rapport through chat interactions
                - Explain the significance of active listening in chat responses """
                ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
























































