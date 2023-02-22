import torch

def load_model():
    model = torch.load('saved_model', map_location=torch.device('cpu'))
    return model