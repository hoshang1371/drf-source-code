from rest_framework import serializers
from blog.models import Articale
from django.contrib.auth.models import User


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
        model = User
        fields = "__all__"