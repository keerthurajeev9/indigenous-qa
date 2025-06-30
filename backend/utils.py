import fitz  # PyMuPDF

async def save_and_extract_text(file):
    contents = await file.read()
    path = f"temp_{file.filename}"
    with open(path, "wb") as f:
        f.write(contents)
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text
