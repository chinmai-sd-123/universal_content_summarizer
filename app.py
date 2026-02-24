import gradio as gr
from gradio import interface
from summarizer import summarize_text
from utils import fetch_website_contents
from utils import extract_text
def run_summary(input_type, user_input, pdf_file, style, depth, audience):
    if input_type== "URL":
        content= fetch_website_contents(user_input)
    elif input_type=="PDF":
        if pdf_file is None:
            return "please upload a pdf file."
        content= extract_text(pdf_file.name)
    else:
        content=user_input

    word_count= len(content.split())
    summary= summarize_text(content, style, depth, audience)


    return f"**Word Count:** {word_count}\n\n{summary}"

interface= gr.Interface(fn=run_summary, inputs=[
    gr.Radio(["Text","URL","PDF"],label="Input Type"),
    gr.Textbox(label="paste text here"),
    gr.File(label="Upload PDF",file_types=[".pdf"]),
    gr.Dropdown(["bullet","paragraph"],label="style"),
    gr.Dropdown(["short","detailed"],label="Depth"),
    gr.Dropdown(["general","technical","beginner"],label="Audience")
],
outputs=gr.Markdown()
)   
interface.launch()