import requests
from Movie.forms import SearchMovie
from Movie.models import Movie
from django.core.mail import send_mail


def connection(type_search , titles):
    api_key = '7466d5ca'
    movie_informations = []
    for title in titles:
        url = 'http://www.omdbapi.com/?{}={}&apikey={}'.format(type_search ,title , api_key)
        data = requests.get(url)
        if data.status_code == 200:
            data_movie = data.json()
            movie_informations.append(data_movie)
    return movie_informations

def save_movies(data_movies):
    for data in data_movies:
        if data['Response'] == 'True':
            info_movies_search = data.get('Search' ,None)
            if info_movies_search is not None:
                pass
            else:
                info_movies_search = []
                info_movies_search.append(data)

            for info_movie_web in info_movies_search:
                movie = Movie()
                movie.title = info_movie_web['Title']
                movie.genere = info_movie_web.get('Genre', 'No register')
                movie.director = info_movie_web.get('Director', 'No register')
                movie.duration = info_movie_web.get('Duration', '2:00')
                movie.save()


def sendmail(email):
    send_mail(
        'Info Movie',
        'movie create succefully',
        'mpacheco@lsv-tech.com',
        [email],
        fail_silently=False,
    )

    return 'Email sended'



