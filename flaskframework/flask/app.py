import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return '''Welcome to the Flask Framework. 
    An amazing framework for web development.
    '''


@app.route('/index')
def index():
    return "Welcome to the Flask Framework Index."


def run():
    app.run(debug=True)


if __name__ == '__main__':
    run()
