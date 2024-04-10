from flask import Flask, render_template, request
import os
import ksp
import wikipedia
from wikipedia.exceptions import PageError, DisambiguationError

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    file_path = 'uploads/' + file.filename
    file.save(file_path)
    
    filename=os.path.basename(file_path)
    ksp.copy_file("uploads/","static/img/",filename)
    
    text=ksp.read_text(filename)
    
    return render_template('result.html', filename=filename,text=text)



@app.route('/', methods=['POST'])
def search():
    search_query = request.form['search2']
    
    try:
        text = wikipedia.summary(search_query)
    except PageError:
        text = "Sorry, no page found for your search query."
    except DisambiguationError as e:
        # If the search query is ambiguous, suggest some options
        text = f"Your search query is ambiguous. Options: {', '.join(e.options)}"
    
    return render_template('index.html', text=text)


    
if __name__ == '__main__':
    app.run(debug=True)
