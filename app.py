import streamlit as st 
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), key=lambda x:x[1], reverse=True)[1:6]
    
    recommend_movies = []
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

# Retriving the dictionary from new_df
movie_dict = pickle.load(open('movie_dict.pkl','rb')) 
movies = pd.DataFrame(movie_dict) 

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')     


selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values) # for displaying all the movie titles in search box for selecting a specific movie from list

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)