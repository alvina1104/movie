from .serializer import (UserProfileSerializer,CategoryListSerializer,CategoryDetailSerializer,
                         GenreListSerializer,GenreNameSerializer,GenreDetailSerializer,
                         CountrySerializer,DirectorSerializer,ActorSerializer,
                         ActorImageSerializer,MovieListSerializer,MovieDetailSerializer,
                         MovieVideoSerializer,MovieFrameSerializer,
                         ReviewSerializer,ReviewLikeSerializer,HistorySerializer)
from .models import (UserProfile,Category,Genre,Country,Director,Actor,ActorImage,Movie,MovieVideo,
                     MovieFrame,Review,ReviewLike,History)
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets,generics
from django_filters.rest_framework import DjangoFilterBackend
from .filter import MovieFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import MovieListPagination,CategoryListPagination,GenreListPagination


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = CategoryListPagination

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    pagination_class = GenreListPagination

class GenreDetailAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorImageViewSet(viewsets.ModelViewSet):
    queryset = ActorImage.objects.all()
    serializer_class = ActorImageSerializer


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = MovieFilter
    search_fields = ['movie_name']
    ordering_fields= ['year']
    pagination_class = MovieListPagination

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class MovieVideoViewSet(viewsets.ModelViewSet):
    queryset = MovieVideo.objects.all()
    serializer_class = MovieVideoSerializer

class MovieFrameViewSet(viewsets.ModelViewSet):
    queryset = MovieFrame.objects.all()
    serializer_class = MovieFrameSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
