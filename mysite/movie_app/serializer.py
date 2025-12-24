from .models import (UserProfile,Category,Genre,Country,Director,Actor,
                     ActorImage,Movie,MovieVideo,MovieFrame,Review,ReviewLike,History)
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name','username','password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','profile_image','username','status']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    data_registered = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username','email','age',
                  'phone_number','profile_image','status','data_registered']


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


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%Y'))
    country = CountryListSerializer(many=True),
    genre = GenreNameSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id','movie_poster','movie_name','year','country','genre','movie_status']

class CountryDetailSerializer(serializers.ModelSerializer):
    country_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name','country_movies']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','full_name']

class DirectorDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format('%d-%m-%Y'))
    director_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Director
        fields = ['director_photo','full_name','bio','birth_date','director_movies']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields =['id','full_name']

class ActorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorImage
        fields = ['image']

class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movies = MovieListSerializer(many=True, read_only=True)
    actor_images = ActorImageSerializer(many=True, read_only=True)
    birth_date = serializers.DateField(format('%d-%m-%Y'))
    class Meta:
        model = Actor
        fields = ['full_name','bio','birth_date','actor_movies','actor_images']


class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = ['video_name','video']

class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['image']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileReviewSerializer()

    class Meta:
        model = Review
        fields = ['user','comment','stars','created_date']

class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%d-%m-%Y'))
    country = CountryListSerializer(many=True)
    genre = GenreNameSerializer(many=True)
    director = DirectorListSerializer(many=True)
    actor = ActorSerializer(many=True)
    videos = MovieVideoSerializer(many=True, read_only=True)
    frames = MovieFrameSerializer(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_name','slogan','year','country','director','genre','movie_type','movie_time','actor',
                  'movie_poster','description','trailer','movie_status','videos','frames','get_avg_rating',
                  'get_count_rating','reviews']

    def get_avg_rating(self,obj):
        return obj.get_avg_rating

    def get_count_rating(self,obj):
        return obj.get_count_rating()



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