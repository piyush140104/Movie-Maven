
import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def fetch_poster(movie_id):
    # This is the API URL to get the movie poster

    url =f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.getenv('API_KEY')}&language=en-US"
    # Hit the URL to fetch data
    response = requests.get(url)
    # Convert to JSON
    data = response.json()
    
    if 'poster_path' in data and data['poster_path'] is not None:
        # Construct the full path of the poster
        full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        return full_path
    return None


def recommend(movie_name):
    # Get the index of the movie from the DataFrame
    index = movies[movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies_name = []
    recommended_movies_poster = []
    
    for i in distances[1:6]:
        # Fetch the movie id and poster for each recommended movie
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_name.append(movies.iloc[i[0]]['title'])
        recommended_movies_poster.append(fetch_poster(movie_id))
    
    return recommended_movies_name, recommended_movies_poster

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function with the correct file name
load_css("style.css")

st.markdown('<div class="title">MOVIE MAVEN</div>', unsafe_allow_html=True)

# Load the movie data and similarity matrix
movies = pickle.load(open('artifiacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifiacts/similarity.pkl', 'rb'))

# Create a select box for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox('Type Or Select to get recommendations', movie_list)

# Display recommendations when button is clicked
if st.button('Show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    
    # Create five columns for displaying movie posters and names
    col1, col2, col3, col4, col5 = st.columns(5)

    if recommended_movies_poster[0]:
        with col1:
            st.text(recommended_movies_name[0])
            st.image(recommended_movies_poster[0])
    if recommended_movies_poster[1]:
        with col2:
            st.text(recommended_movies_name[1])
            st.image(recommended_movies_poster[1])
    if recommended_movies_poster[2]:
        with col3:
            st.text(recommended_movies_name[2])
            st.image(recommended_movies_poster[2])
    if recommended_movies_poster[3]:
        with col4:
            st.text(recommended_movies_name[3])
            st.image(recommended_movies_poster[3])
    if recommended_movies_poster[4]:
        with col5:
            st.text(recommended_movies_name[4])
            st.image(recommended_movies_poster[4])
