from rest_framework import serializers
from .models import Movie , Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password',)
        extra_kwargs = {'password':{'write_only':True ,'required':True}}

        def create(self, validated_date):
            user = User.objects.create_user(**validated_date)
            Token.objects.create(user=user)
            return user 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # lookup_fields = 'id'
        fields = [
            'id',
            'title',
            'description',
            'no_of_ratings',
            'avg_ratings'
        ]
        # read_only_fields = ('no_of_ratings','avg_ratings')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        # lookup_fields = 'id'
        fields = [
            'id',
            'movie',
            'user',
            'stars',
        ]