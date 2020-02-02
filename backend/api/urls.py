from django.urls import include, path
from .views import MovieApiView,MovieDetailApiView, RatingApiView, RatingDetailApiView , UserApiView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('movies', MovieApiView)
# router.register('ratings', MovieDetailApiView)

urlpatterns = [
    # path('', include(router.urls)),
    path('movies/', MovieApiView.as_view()),
    path('movies/<int:pk>/', MovieDetailApiView.as_view()),
    path('ratings/', RatingApiView.as_view()),
    path('ratings/<int:pk>/', RatingDetailApiView.as_view()),
    path('users/', UserApiView.as_view()),
]
