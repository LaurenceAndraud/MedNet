import torch
from flask import Flask, render_template, request, redirect
from model import load_model
from PIL import Image
from torchvision import transforms
from MedNet import MedNet
import numpy as np

app = Flask(__name__)
model = load_model()
app.config['UPLOAD_FOLDER'] = './upload'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        img = Image.open(file.stream)

        # Prétraiter l'image
        transform = transforms.Compose([
            transforms.Resize(64),
            #transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=(0.485),
                std=(0.229))
        ])
        img_tensor = transform(img).unsqueeze(0)

        # faire la prédiction
        model.eval()
        with torch.no_grad():
            output = model(img_tensor)
            _, predicted = torch.max(output.data, 1)
            prediction = predicted.item()
            label_names = ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']
            names_org = label_names[prediction]
            print(names_org)
        
        # avoir le résultat de la prédiction
        return render_template('result.html', names_org=names_org)

        # rediriger vers les résultats


if __name__ == "__main__":
    app.run()
