#importing libraries
import gradio as gr
from langchain_community.llms.ollama import Ollama

BASE_URL = "http://localhost:11434"
MODEL = "llama3"

def llm_response(query):
    """ Function to pass the prompt to the llm """
    ollama = Ollama(
        base_url = BASE_URL,
        model = MODEL
    )
    return ollama.invoke(query)

demo = gr.Interface(
    fn=llm_response,
    inputs=[gr.Textbox(label="Query",lines=5)],
    outputs=[gr.Textbox(label="Some thoughts!",lines=5)],
)
if __name__ == "__main__":
    demo.launch(share=True)