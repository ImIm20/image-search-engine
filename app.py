import pickle
import numpy as np
import pandas as pd
from PIL import Image
import tensorflow.keras as keras
from datetime import datetime
from flask import Flask, request, render_template
import io
from pathlib import Path

app = Flask(__name__, template_folder='template')
features = pd.read_pickle(r'feature.pkl')
model = keras.models.load_model("model.h5", compile = False)
img_path = pd.read_pickle(r'images_dir.pkl')

def transform_image(img):
    img_arr = []
    imgs = np.array(img.resize((224, 224)))
    img_arr.append(imgs)
    return np.array(img_arr)/255.0

def euclidean(a, b):
    return np.linalg.norm(a - b)

def perform_search(queryFeatures, index, maxResults=10):
    results = []
    for i in range(0, len(index)):
        d = euclidean(queryFeatures, index[i])
        results.append((d, i))
    results = sorted(results)[:maxResults]
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']
        # Save query image
        img = Image.open(file.stream) #PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)

        #image_bytes = file.read(uploaded_img_path)
        pillow_img = Image.open(uploaded_img_path)
        feature = model.predict(transform_image(pillow_img))
        feature.resize((1280))
        result = perform_search(feature, features, 16)

        dist = []
        indexes = []
        for a, b in result:
                indexes.append(b)
                dist.append(a)        
        print(result)
        scores = [(dist[indexes.index(idx)], Path("static/dataset/"+img_path[idx])) for idx in indexes]
        
        return render_template('index.html',
                               query_path=uploaded_img_path,
                               scores=scores[1:])
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run("0.0.0.0")
