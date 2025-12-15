from .models import Category, Genre, Country,Director, Actor, Movie, MovieVideo
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('full_name','bio',)

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('full_name','bio',)

@register(Movie)
class CountryTranslationOptions(TranslationOptions):
    fields = ('movie_name','slogan','genre','description',)

@register(MovieVideo)
class CountryTranslationOptions(TranslationOptions):
    fields = ('video_name',)

