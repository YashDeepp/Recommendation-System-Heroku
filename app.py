import pandas as pd
import streamlit as st
import pickle
import requests

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(get_poster(movie_id))
    return recommended_movies,posters

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=50364441ccf7b80e5f008c4997fd27de&language=en-US".format(movie_id)
    response = requests.get(url)
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+ data["poster_path"]

similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title("Movie Recommender System")
option = st.selectbox('Select a movie ',movies['title'].values)
if st.button('Recommend'):
    recommendation,poster=recommend(option)
    col1, col2, col3, col4,col5= st.columns(5)
    with col1:
        st.text(recommendation[0])
        st.image(poster[0])
    with col2:
        st.text(recommendation[1])
        st.image(poster[1])
    with col3:
        st.text(recommendation[2])
        st.image(poster[2])
    with col4:
        st.text(recommendation[3])
        st.image(poster[3])
    with col5:
        st.text(recommendation[4])
        st.image(poster[4])