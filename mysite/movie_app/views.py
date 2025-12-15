from .serializer import (UserProfileSerializer,CategoryListSerializer,
                         CategoryDetailSerializer,GenreListSerializer,
                         GenreDetailSerializer,
                         CountrySerializer,DirectorSerializer,ActorSerializer,ActorImageSerializer,
                         MovieListSerializer,MovieVideoSerializer,MovieFrameSerializer,
                         ReviewSerializer,ReviewLikeSerializer,HistorySerializer)
from .models import (UserProfile,Category,Genre,Country,Director,
                     Actor,ActorImage,Movie,MovieVideo,MovieFrame,
                     Review,ReviewLike,History)
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets,generics


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

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