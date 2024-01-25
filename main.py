from fastapi import FastAPI, UploadFile
from rembg import remove, new_session
from PIL import Image
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI() 

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# models = {
#   "silueta": "silueta",
#   "general": "u2netp",
#   "general2": "isnet-general-use",
#   "human": "u2net_human_seg"
# }

class Model(BaseModel):
  model: str


@app.get("/remove_background/{model_name}" )
def remove_background(model_name = str):
  session = new_session(model_name)
  input_path = './images/imageUploaded.jpg'
  output_path = './images/output.png'

  input = Image.open(input_path)
  output = remove(input, session=session)
  output.save(output_path)
  output_path = Path(output_path)

  return FileResponse(output_path)

@app.post("/upload_img")
def upload_file(file: UploadFile):
    input = Image.open(file.file)
    input.save("./images/imageUploaded.jpg")
    return "ok"
