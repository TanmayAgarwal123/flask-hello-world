# import numpy as np
# from flask import Flask, request, jsonify, render_template
# import pickle
# import secrets
#
# # Create flask app
# flask_app = Flask(__name__)
# model = pickle.load(open("model.pkl", "rb"))
#
# # Generate API key
# api_key = secrets.token_hex(16)
#
# @flask_app.route("/")
# def Home():
#     return render_template("index.html")
#
# @flask_app.route("/predict", methods=["POST"])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text="The fertilizer is {}".format(prediction))
#
# @flask_app.route("/get_api_key", methods=["GET"])
# def get_api_key():
#     return jsonify({"api_key": api_key})
#
# if __name__ == "__main__":
#     flask_app.run(debug=True)
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import secrets


# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
#model2 = pickle.load(open("model2.pkl", "rb"))
#model3 = pickle.load(open("model3.pkl", "rb"))
#model4 = pickle.load(open("model4.pkl", "rb"))
#model5 = pickle.load(open("model5.pkl", "rb"))

# Generate API key
api_key = secrets.token_hex(16)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/fertilizer", methods=["POST"])
def predict():
    if request.is_json:
        data = request.get_json()
        float_features = [float(x) for x in data.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        return jsonify({"prediction": prediction.tolist()}), 200
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400


# @app.route("/cropyeild", methods=["POST"])
# def predict2():
#     if request.is_json:
#         data = request.get_json()
#         float_features = [float(x) for x in data.values()]
#         features = [np.array(float_features)]
#         prediction = model2.predict2(features)
#         return jsonify({"prediction": prediction.tolist()}), 200
#     else:
#         return jsonify({"error": "Request must be in JSON format"}), 400


# @flask_app.route("/get_api_key", methods=["GET"])
# def get_api_key():
#     return jsonify({"api_key": api_key})
#
# if __name__ == "__main__":
#     flask_app.run(debug=True,)
if __name__ == "__main__":
    flask_app.run(debug=True, host='192.168.56.1')
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import secrets

# Create flask app
flask_app = Flask(__name__)
model2 = pickle.load(open("model2.pkl", "rb"))

# Generate API key
api_key = secrets.token_hex(16)

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/cropyeild", methods=["POST"])
def predict():
    if request.is_json:
        data = request.get_json()
        float_features = [float(x) for x in data.values()]
        features = [np.array(float_features)]
        prediction = model2.predict(features)
        return jsonify({"prediction": prediction.tolist()}), 200
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400

# Custom endpoint for running the Flask app
if __name__ == "__main__":
    flask_app.run(debug=True)
"""
