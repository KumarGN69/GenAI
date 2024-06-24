#importing Gradio library
import gradio as gr


def greet(name, intensity):
    """ Importing gradio for demop app """
    return "Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()