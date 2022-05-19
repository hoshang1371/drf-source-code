from rest_framework import serializers
from blog.models import Articale
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        #model = User
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


class ArticleSerializers(serializers.ModelSerializer):
    author =AuthorSerializers()
    class Meta:
        model = Articale
        # fields =(
        #     "title","Slug","author","content","publish","status",
        # )
        # exclude = ['users']
        fields = "__all__"

        def validate_title(self, value):
            # filter_list = ["javascript","laravel","PHP"]
            # print("_____________________________")
            # for i in filter_list:
            #     print("_____________________________")
            #     if i in value:
            #         raise serializers.ValidationError("Dont use bad words{}".format(i))
            # return value

            if 'javascript' not in value.lower():
                raise serializers.ValidationError("Blog post is not about Django")
            return value


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        #model = User
        model = get_user_model()
        fields = "__all__"