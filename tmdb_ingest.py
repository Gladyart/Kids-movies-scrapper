import os
import requests
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Movie, Genre, movie_genres, Cinema, Showtime


