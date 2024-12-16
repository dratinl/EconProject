from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route('/')
def index():
	return rendeer_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	data = request.json
	print(data)
	return jsonify({"message": "Submission received!"}), 200

if __name__ == '__main__':
	app.run(debug=True)