from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

app = Flask(__name__)

# Initialize MediaPipe Image Embedder
base_options = python.BaseOptions(model_asset_path='efficientnet_lite0_fp32.tflite')
options = vision.ImageEmbedderOptions(base_options=base_options)
embedder = vision.ImageEmbedder.create_from_options(options)

def get_image_embedding(image):
    # Convert PIL Image to MediaPipe Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.array(image))
    
    # Generate embedding
    embedding_result = embedder.embed(mp_image)
    
    # Get the embeddings (using quantized embeddings for efficiency)
    return embedding_result.quantized_embeddings[0].tolist()

@app.route('/get_embedding', methods=['POST'])
def get_embedding():
    # Check if an image file is present in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Read the image file from the request
    image_file = request.files['image']

    # Open the image using PIL
    image = Image.open(image_file).convert('RGB')

    # Generate the embedding for the image using MediaPipe
    embedding = get_image_embedding(image)

    # Return the embedding as JSON response
    return jsonify({'embedding': embedding})

if __name__ == '__main__':
    app.run(debug=True)
