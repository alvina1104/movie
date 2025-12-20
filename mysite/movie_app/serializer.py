from .models import (UserProfile,Category,Genre,Country,Director,Actor,
                     ActorImage,Movie,MovieVideo,MovieFrame,Review,ReviewLike,History)
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','profile_image']


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


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']

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
        fields = ['video_name','video']

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['image']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileReviewSerializer()

    class Meta:
        model = Review
        fields = ['user','comment','stars','created_date']

class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%d-%m-%Y'))
    country = CountrySerializer(many=True)
    genre = GenreNameSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    videos = MovieVideoSerializer(many=True, read_only=True)
    frames = MovieFrameSerializer(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = Movie
        fields = ['movie_name','slogan','year','country','director','genre','movie_type','movie_time','actor',
                  'movie_poster','description','trailer','movie_status','videos','frames','reviews']



class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['genre_name','movies']


class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'