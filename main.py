from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import shutil

app = FastAPI()

@app.post("/generate-footprint/")
async def generate(file: UploadFile):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"script": "output.pas", "data": {"status": "prototype"}}

@app.get("/download/{filename}")
def download(filename: str):
    return FileResponse(path=filename, filename=filename)
