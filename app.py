from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Папка для загрузки файлов
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Максимум 16 MB

# Разрешенные расширения файлов
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

# Проверка расширения файла
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Убедитесь, что папка для загрузки существует
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'Нет файла', 400
        file = request.files['photo']
        if file.filename == '':
            return 'Файл не выбран', 400
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                file.save(filename)
                return redirect(url_for('uploaded_file', filename=file.filename))
            except Exception as e:
                return f'Ошибка при сохранении файла: {e}', 500
    return render_template('Register.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('card.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
