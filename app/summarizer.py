
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(override=True)
gemini_api_key=os.getenv("GOOGLE_API_KEY")
client= OpenAI(api_key=gemini_api_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def summarize_text(text,style= "bullet",depth="short",audience="general"):
    system_prompt=f"""
    you are a professional summarization assistant.
    style:{style}
    Depth: {depth}
    audience: {audience}
    Follow the instructions clearly and makes sure u give in a clean text.
    """

    user_prompt=f"summarize the following content:\n\n{text}"

    response=client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"system","content":system_prompt},
        {"role":"user","content":user_prompt}
        ],temperature=0.3
    )

    return response.choices[0].message.content