from flask import Flask, request, render_template, jsonify
from ocr import extract_text
from translation import translate_to_swedish

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    file.save('uploaded_image.jpg')

    # Extract text using Tesseract
    extracted_text = extract_text('uploaded_image.jpg')

    # Translate to Swedish
    translated_text = translate_to_swedish(extracted_text)

    return jsonify({"extracted_text": extracted_text, "translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True)