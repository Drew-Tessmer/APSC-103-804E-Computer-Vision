from flask import Blueprint, render_template, request, redirect
import os

views = Blueprint('views', __name__)
bp = Blueprint('my_blueprint', __name__, static_folder='static', template_folder='templates')

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    # Ensure that the 'uploads' directory exists
    os.makedirs('uploads', exist_ok=True)

    # Save the file with its original name in the 'uploads' directory
    file.save(os.path.join('uploads', file.filename))

    return redirect('/')