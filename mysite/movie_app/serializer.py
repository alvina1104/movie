from .models import (UserProfile,Category,Genre,Country,Director,Actor,
                     ActorImage,Movie,MovieVideo,MovieFrame,Review,ReviewLike,History)
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_name']

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    genres = GenreListSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['category_name','genres']

class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorImage
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    country = CountrySerializer(many=True)
    genre = GenreNameSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id','movie_poster','movie_name','year','country','genre','movie_status']

class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = '__all__'

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'