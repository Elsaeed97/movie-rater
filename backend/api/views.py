from django.shortcuts import render
from .serializer import RatingSerializer, MovieSerializer, UserSerializer
from rest_framework import viewsets , status,authentication, permissions, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Rating, Movie 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated ,AllowAny
# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
class UserApiView(mixins.CreateModelMixin,generics.ListAPIView):
	queryset 				= User.objects.all()
	serializer_class 		= UserSerializer
	authentcation_classes 	= [TokenAuthentication]
	permission_classes 		= [IsAuthenticated]

	def get_queryset(self):
		request = self.request
		qs = User.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content_icontains='q')
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save()

class MovieApiView(mixins.CreateModelMixin,generics.ListAPIView):
	queryset 				= Movie.objects.all()
	serializer_class 		= MovieSerializer
	lookup_field			= 'id'
	authentcation_classes 	= [TokenAuthentication]
	permission_classes 		= [IsAuthenticated]
	# user = request.user

	def get_queryset(self):
		request = self.request
		qs = Movie.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content_icontains='q')
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save()


class MovieDetailApiView(mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.RetrieveAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	# lookup_field			= 'id'
	authentcation_classes 	= [TokenAuthentication]


	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

	def perform_destroy(self, instance):
		if instance is not None:
			return instance.delete()
		return None

class RatingApiView(mixins.CreateModelMixin,generics.ListAPIView):
	queryset = Rating.objects.all()
	serializer_class = RatingSerializer
	lookup_field			= 'id'
	authentcation_classes 	= [TokenAuthentication]
	permission_classes 		= [IsAuthenticated]

	def get_queryset(self):
		request = self.request
		qs = Rating.objects.all()
		query  = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(content_icontains='q')
		return qs 

	def post(self,request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save()

class RatingDetailApiView(mixins.UpdateModelMixin,mixins.DestroyModelMixin ,generics.RetrieveAPIView):
	queryset = Rating.objects.all()
	serializer_class = RatingSerializer
	authentcation_classes 	= [TokenAuthentication]
	# lookup_field			= 'id'


	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

	def perform_destroy(self, instance):
		if instance is not None:
			return instance.delete()
		return None