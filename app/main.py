from app.summarizer import summarize_text
from app.utils import fetch_website_contents
from app.utils import extract_text
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods= ["*"],
    allow_headers=["*"],
)

@app.post("/summarize")
async def summarize(
    input_type: str= Form(...),
    text: str =Form(None) ,
    url: str = Form(None),
    file:UploadFile=File(None),
    style: str = Form("paragraph"),
    depth: str = Form("short"),
    audience: str = Form("general"),
):
    content= ""

    if input_type=="text":
        content= text
    elif input_type=="url":
        content=fetch_website_contents(url)
    elif input_type=="pdf":
        if file is None:
            return {"summary": "Please upload a PDF file."}
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            content = extract_text(tmp.name)
    summary= summarize_text(content, style, depth, audience)
    return {"summary":summary}