from flask import Flask, request, jsonify
from PIL import Image
import torch
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel

app = Flask(__name__)

# Initialize the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Define transformations for incoming images
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize images to match CLIP input size
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize image pixels
])

@app.route('/get_embedding', methods=['POST'])
def get_embedding():
    # Check if an image file is present in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Read the image file from the request
    image_file = request.files['image']

    # Open the image file using PIL
    image = Image.open(image_file).convert("RGB")

    # Apply transformations to the image
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Generate the embedding for the image using CLIP
    with torch.no_grad():
        # Convert the tensor to a PIL image and then to a numpy array
        image_pil = transforms.ToPILImage()(image_tensor.squeeze()).convert("RGB")
        
        # Preprocess the image
        inputs = processor(images=image_pil, return_tensors="pt")
        
        # Generate embeddings
        outputs = model.get_image_features(**inputs)
        embedding = outputs.cpu().numpy().flatten().tolist()

    # Return the embedding as JSON response
    print(embedding)
    return jsonify({'embedding': embedding})

if __name__ == '__main__':
    app.run(debug=True)