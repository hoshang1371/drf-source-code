from rest_framework import serializers
from blog.models import Articale
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# class AuthorSerializers(serializers.ModelSerializer):
#     class Meta:
#         #model = User
#         model = get_user_model()
#         fields = ["id", "username", "first_name", "last_name"]


class AuthorUserNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username + " " + ":" + value.last_name + value.first_name


class ArticleSerializers(serializers.ModelSerializer):
    # author =AuthorSerializers()
    # author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')
    # author = AuthorUserNameField(read_only='True')
    # author = serializers.CharField(source="author.username", read_only ='True')
    def get_author(self, obj):
        return obj.author.username

    author = serializers.SerializerMethodField("get_author")
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