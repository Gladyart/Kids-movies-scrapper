from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from os import path

base = declarative_base()

class Movie(base):
    __tablename__ = 'movies'
    
    movie_id = Column(Integer, primary_key=True)
    tmdb_id = Column(Integer)
    title = Column(String, nullable = False)
    original_title = Column(String)
    age_rating = Column(String)
    run_time = Column(Integer)
    release_date = Column(Date)
    poster_url = Column(String)
    overview = Column(Text)
    
    genres = relationship('Genre', secondary='movie_genres', back_populates='movies')

class Cinema(base):
    __tablename__ = 'cinemas'
    
    cinema_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String) 
    city = Column(String, default='Kraków')
    
    showtimes = relationship('Showtime', back_populates='cinema')

class Showtime(base):
    __tablename__ = 'showtimes'
    
    showtime_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.movie_id'))
    cinema_id = Column(Integer, ForeignKey('cinemas.cinema_id'))
    start_time = Column(DateTime, nullable=False) 
    language_version = Column(String)
    auditorium = Column(String)
    scrapped_at = Column(DateTime, nullable=False)

    movie = relationship('Movie')
    cinema = relationship('Cinema', back_populates='showtimes')

class Genre(base):
    __tablename__ = 'genres'
    
    genre_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    movies = relationship('Movie', secondary='movie_genres', back_populates='genres')

movie_genres = Table('movie_genres', base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.movie_id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.genre_id'), primary_key=True)
)

def create_database(db_path='sqlite:///movies.db'):
    engine = create_engine(db_path)
    base.metadata.create_all(engine)
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database() if not path.exists('movies.db') else print("Database already exists.")
        
