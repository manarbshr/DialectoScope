from flask import Flask, request, jsonify
import pickle

# Load logistic regression model
model = pickle.load(open('Models/logistic_regression_model.pkl', 'rb'))

# Load TF-IDF vectorizer
vectorizer = pickle.load(open('Models/tfidf_vectorizer.pkl', 'rb'))

# Create a Flask app
app = Flask(__name__)


# Define a route for the default URL, which loads the form
@app.route('/')
def home():
    return '''
        <h1>ML Model Prediction</h1>
        <form action="/predict" method="post">
            <textarea name="text" rows="10" cols="30"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    '''
    
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Convert data into the format model expects
    input_text = data['text']

    sample_text_vectorized = vectorizer.transform(input_text)

    # Make prediction using the model
    prediction = model.predict(sample_text_vectorized)

    probabilities = model.predict_proba(sample_text_vectorized)
    probabilities = [[round(prob, 2) for prob in row] for row in probabilities]

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0], 'probability': probabilities})



if __name__ == '__main__':
    app.run(debug=True)