from django.urls import path,include
from .views import (UserProfileViewSet,CategoryListAPIView,GenreListAPIView,
                    GenreDetailAPIView,CategoryDetailAPIView,
                    CountryViewSet,DirectorViewSet,ActorViewSet,
                    ActorImageViewSet,MovieListAPIView,MovieVideoViewSet,MovieFrameViewSet,
                    ReviewViewSet,ReviewLikeViewSet,HistoryViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user',UserProfileViewSet)
router.register(r'country',CountryViewSet)
router.register(r'director',DirectorViewSet)
router.register(r'actor',ActorViewSet)
router.register(r'actor_image',ActorImageViewSet)
router.register(r'movie_video',MovieVideoViewSet)
router.register(r'movie_frame',MovieFrameViewSet)
router.register(r'review',ReviewViewSet)
router.register(r'review_like',ReviewLikeViewSet)
router.register(r'history',HistoryViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('category/',CategoryListAPIView.as_view(),name='category_list'),
    path('category/<int:pk>/',CategoryDetailAPIView.as_view(),name='category_detail'),
    path('genre/',GenreListAPIView.as_view(),name='genre_list'),
    path('genre/<int:pk>/',GenreDetailAPIView.as_view(),name='genre_detail'),
    path('movie/',MovieListAPIView.as_view(),name='movie_list')
]