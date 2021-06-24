from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi import templating
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from PIL import Image
from io import BytesIO

import shutil
import json 
import base64
import requests
import cv2
import numpy as np

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

url = "https://"

def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))

# get index page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# get result page
@app.post("/result")
async def upload_image(request: Request, image: UploadFile = File(...)):
    # with open("./static/images/destination.jpg", "wb") as buffer:
    #     shutil.copyfileobj(image.file, buffer)

    image = load_image_into_numpy_array(await image.read())
    retval, buffer_img= cv2.imencode('.jpg', image)
    data = base64.b64encode(buffer_img)
    
    send_data = {'base64': data}
    # response = requests.post(url, info = send_data)

    #test
    f = open('result.json')
    result = json.load(f)

    ###
    # wait result
    ###

    # result will be store in a variable named result
    # f = open('result.json')
    # result = json.load(f)

    return templates.TemplateResponse("result.html", {"request": request, "result": result})


# get test_image_1 page
@app.get("/test_image_1", response_class=HTMLResponse)
async def test_image_1(request: Request):
    shutil.copy('./static/images/test_image/ocr-1.jpg', "./static/images/destination.jpg")

    #Edit Recognition Code Here

    #Edit Recognition Code Here

    # result will be store in a variable named result
    f = open('result.json')
    result = json.load(f)

    return templates.TemplateResponse("result.html", {"request": request, "result": result })


# get test_image_2 page
@app.get("/test_image_2", response_class=HTMLResponse)
async def test_image_2(request: Request):
    shutil.copy('./static/images/test_image/ocr-2.jpg', "./static/images/destination.jpg")

    #Edit Recognition Code Here

    #Edit Recognition Code Here

    # result will be store in a variable named result
    f = open('result.json')
    result = json.load(f)

    return templates.TemplateResponse("result.html", {"request": request, "result": result })


# get test_image_3 page
@app.get("/test_image_3", response_class=HTMLResponse)
async def test_image_3(request: Request):
    shutil.copy('./static/images/test_image/ocr-3.jpg', "./static/images/destination.jpg")

    #Edit Recognition Code Here

    #Edit Recognition Code Here

    # result will be store in a variable named result
    f = open('result.json')
    result = json.load(f)

    return templates.TemplateResponse("result.html", {"request": request, "result": result })