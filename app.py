import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from PIL import Image
import os

# Load the saved model and vectorizer
with open('Models/logistic_regression_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('Models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define a dictionary to map dialects to image file paths and full country names
dialect_info = {
    'EG': {'image': 'images/Eg.jpg', 'country': 'Egypt'},
    'LB': {'image': 'images/Lb.jpg', 'country': 'Lebanon'},
    'LY': {'image': 'images/Ly.jpg', 'country': 'Libya'},
    'MA': {'image': 'images/Ma.webp', 'country': 'Morocco'},
    'SD': {'image': 'images/Sd.jpg_large', 'country': 'Sudan'}
}

# Define the Streamlit app
def main():
    st.title("Dialect Classification App")
    
    st.write("""
    This app predicts the dialect of the provided text.
    """)
    
    sample_text = st.text_area("Enter text to classify the dialect:")
    
    if st.button("Predict"):
        if sample_text:
            sample_text_vectorized = vectorizer.transform([sample_text])
            prediction = model.predict(sample_text_vectorized)[0]
            st.write(f"The predicted dialect is: {dialect_info[prediction]['country']}")
            
            # Display the corresponding image
            if prediction in dialect_info:
                image_path = dialect_info[prediction]['image']
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    st.image(image, caption=f'Dialect: {dialect_info[prediction]["country"]}')
                else:
                    st.write("Image not found.")
            else:
                st.write("No corresponding image for the predicted dialect.")
        else:
            st.write("Please enter some text to classify.")

if __name__ == "__main__":
    main()
