from flask import Flask, request, jsonify
from google.cloud import vision
from google.cloud.vision_v1 import types
import io

app = Flask(__name__)

# Configuración del cliente de Google Cloud Vision
client = vision.ImageAnnotatorClient()

@app.route('/process-image', methods=['POST'])
def process_image():
    # Verifica si el archivo está en la solicitud
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Si no se ha subido archivo
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Procesa la imagen usando Google Cloud Vision
        content = file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        # Extrae el texto detectado
        detected_text = texts[0].description if texts else "No text detected"
        return jsonify({'detected_text': detected_text})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
