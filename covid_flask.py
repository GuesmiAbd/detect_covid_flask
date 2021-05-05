import base64
import numpy as np
import io
from PIL import Image
import keras

from keras import backend as K
from keras.models import Sequential
from tensorflow.keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
#app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
#app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/predict": {"origins": "http://localhost:5000"}})

def get_model():
    global model
    model = load_model('CNN.h5')
    print("model loaded!!!!")


def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image= image.resize(target_size)
    image= img_to_array(image)
    image= np.expand_dims(image, axis=0)
    return image

print(" loading keras model ....")
get_model()

@app.route("/")
def hello():
    return "Hello"

@app.route("/predict", methods=["POST"])
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def predict():
    message = request.get_json(force=True)
    
    encoded = message['image']
    #print("encoded",encoded)
    decoded = base64.b64decode(encoded)
    #print("decoded",decoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))

    prediction = model.predict(processed_image).tolist()
    print(prediction)
    response = {
        'prediction': {
            'covide': prediction[0][0]
        }
    }
    return jsonify(response)
if __name__ == '__main__':
      app.run(debug=True)
