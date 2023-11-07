from fastapi import FastAPI, Request,HTTPException
from app.code import predict_covid
import cv2
import base64
from tensorflow import keras
import os
from tensorflow.keras import optimizers
from tensorflow.keras.optimizers import RMSprop  
app = FastAPI()


model = keras.models.load_model(os.getcwd() + "/model/modelpredictcovid.h5", compile=False)


@app.get("/")
async def read_root():
    return {"Hello": "World"}



url ='http://172.17.0.1:8080/api/genimage'


@app.post('/api/predict')
async def predict(data: Request):
  
    try:
        print("Received a prediction request")
        json_data = await data.json()
        item_str = json_data.get("img")
        if item_str is not None:
            prediction = predict_covid(model,item_str,url)
            # print("Prediction:", prediction)
            return {'result': prediction}
        else:
            raise HTTPException(status_code=400, detail="Image data 'img' not found in the request.")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")
   



    



