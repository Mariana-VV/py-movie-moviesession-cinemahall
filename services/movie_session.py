import datetime
from xmlrpc.client import DateTime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(movie_show_time: DateTime,
                         movie_id: int,
                         cinema_hall_id: int) -> MovieSession:
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie = Movie.objects.get(id=movie_id)

    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall,
        movie=movie
    )

    return new_movie_session


def get_movies_sessions(session_date: str = None) -> (
        QuerySet | MovieSession):
    movie_sessions = MovieSession.objects.all()

    if session_date:
        year = int(session_date.split("-")[0])
        month = int(session_date.split("-")[1])
        day = int(session_date.split("-")[2])
        date_obj = datetime.date(year, month, day)
        movie_sessions = MovieSession.objects.filter(show_time__date=date_obj)

    return movie_sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(session_id: int,
                         show_time: DateTime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ):
    session = MovieSession.objects.get(id=session_id)

    if show_time:
        session.show_time = show_time
    if movie_id:
        session.movie_id = movie_id
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall

    session.save()


def delete_movie_session_by_id(session_id: int) -> None:
    session_to_delete = MovieSession.objects.get(id=session_id)
    session_to_delete.delete()
