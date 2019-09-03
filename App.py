from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask er flottast</h1><a href="sida1">Sida1</a>'


@app.route('/sida1')
def sida1():
        return "Síða 1"







if __name__ == "__main__":
	app.run()
