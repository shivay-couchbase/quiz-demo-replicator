from flask import Flask, request, jsonify
from PIL import Image
import io
import os

from google.cloud import aiplatform
from vertexai.vision_models import Image as VertexImage
from vertexai.vision_models import MultiModalEmbeddingModel

app = Flask(__name__)

# Initialize Vertex AI
aiplatform.init(project=os.getenv("GOOGLE_CLOUD_PROJECT"))

# Initialize the MultiModal Embedding Model
mm_embedding_model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding@001")

def get_image_embedding(image_bytes, dimension=1408):
    image = VertexImage(image_bytes)
    embedding = mm_embedding_model.get_embeddings(
        image=image,
        dimension=dimension,
    )
    return embedding.image_embedding

@app.route('/get_embedding', methods=['POST'])
def get_embedding():
    # Check if an image file is present in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Read the image file from the request
    image_file = request.files['image']

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image = Image.open(image_file)
    image.save(image_bytes, format=image.format)
    image_bytes = image_bytes.getvalue()

    # Generate the embedding for the image using Vertex AI
    embedding = get_image_embedding(image_bytes)

    # Return the embedding as JSON response
    return jsonify({'embedding': embedding})

if __name__ == '__main__':
    app.run(debug=True)
