from openai import AsyncOpenAI
import chainlit as cl
import pandas as pd
from backend.personal import utils


client = AsyncOpenAI()
cl.instrument_openai()

settings = {
    "model": "gpt-4o-mini",
    "temperature": 0.5,
}
messages = None


@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")
    file_content = utils.read_file("./prompts/carasso.txt")
    data = pd.read_csv("./prompts/merged_dt.csv")
    df_string = utils.dataframe_to_string(data)
    global messages
    messages = [utils.create_prompt(file_content, df_string)]


@cl.on_message
async def on_message(message: cl.Message):
    messages.append({"content": message.content, "role": "user"})
    response = await client.chat.completions.create(
        messages=messages,
        **settings,
    )
    messages.append({"content": response.choices[0].message.content, "role": "system"})
    await cl.Message(content=response.choices[0].message.content).send()
