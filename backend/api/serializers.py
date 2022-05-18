from rest_framework import serializers
from blog.models import Articale
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articale
        # fields =(
        #     "title","Slug","author","content","publish","status",
        # )
        # exclude = ['users']
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        #model = User
        model = get_user_model()
        fields = "__all__"