from fastapi import FastAPI, UploadFile
from ocr_pipeline import extract_text_from_image
from llm_summarizer import summarize_document

app = FastAPI(title="DocuVisionAI")

@app.post("/analyze/")
async def analyze_document(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_image(file.filename)
    summary = summarize_document(text)
    return {"summary": summary}
