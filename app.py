from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
import os
from nsfw_image_detection import detect_nsfw
from PIL import Image, ImageFilter

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def blur_image(image_path):
    with Image.open(image_path) as img:
        blurred = img.filter(ImageFilter.GaussianBlur(radius=15))
        blurred_path = f"{os.path.splitext(image_path)[0]}_blurred{os.path.splitext(image_path)[1]}"
        blurred.save(blurred_path)
    return blurred_path

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Perform NSFW detection
            is_nsfw, confidence = detect_nsfw(filepath)
            
            result = {
                'is_nsfw': 'Yes' if is_nsfw else 'No',
                'confidence': f"{confidence:.2%}",
                'image_url': url_for('static', filename=f'uploads/{filename}')
            }
            
            if is_nsfw:
                blurred_path = blur_image(filepath)
                result['image_url'] = url_for('static', filename=f'uploads/{os.path.basename(blurred_path)}')
            
            return jsonify(result)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)