from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from typing import List

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(120), unique=True,  nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[int] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    weather: Mapped[int] = mapped_column(String(120), nullable=False)
    diameter: Mapped[str] = mapped_column(String(120), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="planets")

class Characters(db.Model):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    gender:  Mapped[str] = mapped_column(String(120), nullable=False)
    eyes_color: Mapped[str] = mapped_column(String(120), nullable=False)
    age: Mapped[str] = mapped_column(String(120), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="characters")

class Starships(db.Model):
    __tablename__ = "starships"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(120), nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship(back_populates="starships")

class Favorites(db.Model):
    __tablename__ = "favorites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    characters_id: Mapped[int] = mapped_column(ForeignKey("characters.id"), nullable=True)
    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"), nullable=True)
    starships_id: Mapped[int] = mapped_column(ForeignKey("starships.id"), nullable=True)


    user: Mapped["User"] = relationship(back_populates="favorites")
    planets: Mapped["Planets"] = relationship(back_populates="favorites")
    characters: Mapped["Characters"] = relationship(back_populates="favorites")
    starships: Mapped["Starships"] = relationship(back_populates="favorites")





