from fastapi import FastAPI, UploadFile, File, HTTPException
from pdf2image import convert_from_bytes
from pytesseract import image_to_string

app = FastAPI()

@app.get("/")
def welcome():
    return "welcome"

@app.post("/upload")
async def parse_pdf(file: UploadFile = File(...)):
    pages_text = []
    pdf_content = await file.read()

    images = convert_from_bytes(pdf_content)
    for image in images:
        page_text = image_to_string(image)
        print(page_text)
        pages_text.append(page_text)
    return pages_text