from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import shutil
import os

from pdf_processor import pdf_to_images
from ocr import extract_text
from vision_ai import extract_dimensions
from extractor import merge_data
from footprint import generate_footprint
from altium import generate_script

app = FastAPI()

@app.post("/generate-footprint/")
async def generate(file: UploadFile):
path = f"temp_{file.filename}"

```
with open(path, "wb") as buffer:
    shutil.copyfileobj(file.file, buffer)

images = pdf_to_images(path)

ocr_text = extract_text(images[0])
ai_json = extract_dimensions(images[0])

data = merge_data(ocr_text, ai_json)

pads = generate_footprint(data)
script_file = generate_script(pads)

return {"script": script_file, "data": data}
```

@app.get("/download/{filename}")
def download(filename: str):
return FileResponse(path=filename, filename=filename)
