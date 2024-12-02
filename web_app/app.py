from flask import Flask, request, render_template
import os
import easyocr

app = Flask(__name__)

# Initialize the EasyOCR reader with Indonesian language
reader = easyocr.Reader(['id'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        uploads_dir = 'uploads'
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)
        file_path = os.path.join(uploads_dir, file.filename)
        file.save(file_path)

        # Perform OCR using EasyOCR
        result = reader.readtext(file_path, detail=0)
        text = ' '.join(result)

        return text

if __name__ == '__main__':
    app.run(debug=True)
