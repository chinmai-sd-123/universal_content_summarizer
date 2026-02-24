import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
def fetch_website_contents(url):
    """
    Return the title and contents of the website at the given url;
    truncate to 2,000 characters as a sensible limit
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]
MAX_CHARS= 12000
def extract_text(file_path):
    
    try:
        reader= PdfReader(file_path)
        text= ""
        for page in reader.pages:
            text+=page.extract_text()or""
        if not text.strip():
            return "NO readable text found in pdf" 
        if len(text)> MAX_CHARS:
            text= text[:MAX_CHARS]  
        
        return text.strip()
    except Exception as e:
        return f"error reading pdf:{e}"    
