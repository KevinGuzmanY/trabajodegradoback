from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# User model
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    country = db.Column(db.String(100))

# User Preferences model
class UserPreference(db.Model):
    __tablename__ = 'user_preferences'

    preference_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    watch_frequence_by_week = db.Column(db.Integer)
    netflix_favorite_platform = db.Column(db.Integer)
    amazon_prime_favorite_platform = db.Column(db.Integer)
    disney_prime_favorite_platform = db.Column(db.Integer)
    hbo_prime_favorite_platform = db.Column(db.Integer)
    like_accion_genre = db.Column(db.Integer)
    like_aventura_genre = db.Column(db.Integer)
    like_animacion_genre = db.Column(db.Integer)
    like_comedia_genre = db.Column(db.Integer)
    like_crimen_genre = db.Column(db.Integer)
    like_documental_genre = db.Column(db.Integer)
    like_drama_genre = db.Column(db.Integer)
    like_familiar_genre = db.Column(db.Integer)
    like_fantasia_genre = db.Column(db.Integer)
    like_historia_genre = db.Column(db.Integer)
    like_horror_genre = db.Column(db.Integer)
    like_musica_genre = db.Column(db.Integer)
    like_misterio_genre = db.Column(db.Integer)
    like_romance_genre = db.Column(db.Integer)
    like_ciencia_ficcion_genre = db.Column(db.Integer)
    like_guerra_genre = db.Column(db.Integer)
    favorite_actor = db.Column(db.String(100))

    def update_genre_count(self, genre, increment=True):
        if genre == "Acción":
            self.like_accion_genre = max(0, self.like_accion_genre + (1 if increment else -1))
        elif genre == "Aventura":
            self.like_aventura_genre = max(0, self.like_aventura_genre + (1 if increment else -1))
        elif genre == "Animacion":
            self.like_animacion_genre = max(0, self.like_animacion_genre + (1 if increment else -1))
        elif genre == "Comedia":
            self.like_comedia_genre = max(0, self.like_comedia_genre + (1 if increment else -1))
        elif genre == "Crimen":
            self.like_crimen_genre = max(0, self.like_crimen_genre + (1 if increment else -1))
        elif genre == "Documental":
            self.like_documental_genre = max(0, self.like_documental_genre + (1 if increment else -1))
        elif genre == "Drama":
            self.like_drama_genre = max(0, self.like_drama_genre + (1 if increment else -1))
        elif genre == "Familiar":
            self.like_familiar_genre = max(0, self.like_familiar_genre + (1 if increment else -1))
        elif genre == "Fantasia":
            self.like_fantasia_genre = max(0, self.like_fantasia_genre + (1 if increment else -1))
        elif genre == "Historia":
            self.like_historia_genre = max(0, self.like_historia_genre + (1 if increment else -1))
        elif genre in ["Terror", "Horror"]:
            self.like_horror_genre = max(0, self.like_horror_genre + (1 if increment else -1))
        elif genre == "Musica":
            self.like_musica_genre = max(0, self.like_musica_genre + (1 if increment else -1))
        elif genre == "Misterio":
            self.like_misterio_genre = max(0, self.like_misterio_genre + (1 if increment else -1))
        elif genre == "Romance":
            self.like_romance_genre = max(0, self.like_romance_genre + (1 if increment else -1))
        elif genre == "Ciencia ficción":
            self.like_ciencia_ficcion_genre = max(0, self.like_ciencia_ficcion_genre + (1 if increment else -1))
        elif genre == "Guerra":
            self.like_guerra_genre = max(0, self.like_guerra_genre + (1 if increment else -1))

    # Relación inversa con el modelo User
    user = db.relationship('User', backref=db.backref('user_preferences', lazy=False))

class UserInteraction(db.Model):
    __tablename__ = 'user_interactions'

    interaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content_id = db.Column(db.Integer, nullable=False)
    content_type = db.Column(db.String(50), nullable=False)
    liked = db.Column(db.Boolean, default=False)
    interaction_date = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('interactions', lazy=True))

class Recommendation(db.Model):
    __tablename__ = 'recommendations'

    recommendation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    accion = db.Column(db.Integer, nullable=False)
    aventura = db.Column(db.Integer, nullable=False)
    animacion = db.Column(db.Integer, nullable=False)
    comedia = db.Column(db.Integer, nullable=False)
    crimen = db.Column(db.Integer, nullable=False)
    documental = db.Column(db.Integer, nullable=False)
    drama = db.Column(db.Integer, nullable=False)
    familiar = db.Column(db.Integer, nullable=False)
    fantasia = db.Column(db.Integer, nullable=False)
    historia = db.Column(db.Integer, nullable=False)
    horror = db.Column(db.Integer, nullable=False)
    musica = db.Column(db.Integer, nullable=False)
    misterio = db.Column(db.Integer, nullable=False)
    romance = db.Column(db.Integer, nullable=False)
    ciencia = db.Column(db.Integer, nullable=False)
    guerra = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('recommendations', lazy=True))