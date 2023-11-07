import requests
import numpy as np
import cv2
categories = ['Covid','Normal','Viral Pneumonia']
url ='http://localhost:8080/api/genimage'



def predict_covid(model, img, url):
    print("predict covid")
    params = {"img": img}
    response = requests.get(url, json=params)
    try:
        print("in try")

        if response.status_code == 200:
            print("200 Ok")
            res = response.json()
            dataList = list(res.values())
            
            print("//////")

            i = np.array(dataList,dtype='float32')
            print("pre predict")
            
            covid_predict = model.predict(i)
            print(i.shape)

            predicted_class_index = np.argmax(covid_predict)
            predicted_class = categories[predicted_class_index]
            print(predicted_class)
            # return covid_predict.tolist()
            return predicted_class
        else:
            return {"error in predict": f"API error code: {response.status_code}"}
    except Exception as ex:
        return {"error in predict": f"An error occurred: {str(ex)}"}


    

