import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import requests

# Loads environment variables
load_dotenv('google.env')

api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')

choice = st.sidebar.selectbox("Select your choice", ["Home", "Image Generator"])

if choice == "Home":
    #Logo Image
    image = Image.open(r'C:\Users\ayashaik1\Image generator project\logo.png.png')

    st.image(image, width=100)
    st.title('Image Generation Application')

elif choice == "Image Generator":
    image = Image.open(r'C:\Users\ayashaik1\Image generator project\logo.png.png')
    st.image(image, width=100)
    st.subheader('Image Generator')
    text = st.text_input("Enter your text")
    if text is not None:
        if st.button("Generate Images"):
            # Searches for images using Google Custom Search API
            search_url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'q': text,
                'cx': cx,
                'key': api_key,
                'searchType': 'image',
                'num': 10,
                'fileType': 'jpg|gif|png',
                'imgType': 'photo',
                'imgSize': 'medium',
            }
            response = requests.get(search_url, params=params)
            data = response.json()

            if 'items' in data:
                images = [item['link'] for item in data['items']]
                columns = st.columns(2)

                for i in range(len(images)):
                    with columns[i % 2]:
                        st.image(images[i], use_column_width=True)


            else:
                st.write("No images found.")
