from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''
    for i in range(0, num):
        output += f"<p>{word}</p>"
    return output

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__ == "__main__":
    app.run(debug=True)