from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[int] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)



    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    weather: Mapped[int] = mapped_column(String(120), nullable=False)
    diameter: Mapped[str] = mapped_column(String(120), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    gender:  Mapped[str] = mapped_column(String(120), nullable=False)
    eyes_color: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[str] = mapped_column(String(120), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

class Starships(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(120), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    characters_id: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=True)
    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=True)
    starships_id: Mapped[int] = mapped_column(ForeignKey("starships.id"), nullable=True)




