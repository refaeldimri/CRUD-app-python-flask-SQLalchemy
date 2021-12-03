from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)

# the class Movie will inherit the db.Model of SQLAlchemy
class Movie(db.Model):
    # creating a table name 
    __tablename__ = 'movies' 
    # this is the primary key
    id = db.Column(db.Integer, primary_key=True)
    # nullable is false so the column can't be empty    
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    
    
    def json(self):
        return {'id': self.id, 'title': self.title,'year': self.year, 'genre': self.genre}
        # this method we are defining will convert our output to json
        
        
    def add_movie(_title, _year, _genre):
        '''function to add movie to database using _title, _year, _genre
        as parameters'''
        # creating an instance of our Movie constructor
        new_movie = Movie(title=_title, year=_year, genre=_genre)
        # add new movie to database session
        db.session.add(new_movie)  
        # commit changes to session
        db.session.commit()
        

    def get_all_movies():
        '''function to get all movies in our database'''
        return [Movie.json(movie) for movie in Movie.query.all()]
        

    def get_movie(_id):
        '''function to get movie using the id of the movie as parameter'''
        return [Movie.json(Movie.query.filter_by(id=_id).first())]
        # Movie.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned
        

    def update_movie(_id, _title, _year, _genre):
        '''function to update the details of a movie using the id, title,
        year and genre as parameters'''
        movie_to_update = Movie.query.filter_by(id=_id).first()
        movie_to_update.title = _title
        movie_to_update.year = _year
        movie_to_update.genre = _genre
        db.session.commit()
        

    def delete_movie(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Movie.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database        