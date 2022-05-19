# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import RetrieveAPIView
from blog.models import Articale
from .serializers import (
    ArticleSerializers,
     UserSerializers,
    #   AuthorSerializers,
    )
from django.shortcuts import  render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser ,IsAuthenticated
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperuserOrStaffReadOnly

# from rest_framework import filters


# class ArticleList(ListCreateAPIView):
#     queryset = Articale.objects.all()
#     serializer_class = ArticleSerializers

# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Articale.objects.all()
#     serializer_class = ArticleSerializers
#     permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


class ArticleViewSet(ModelViewSet):
    queryset = Articale.objects.all()
    serializer_class = ArticleSerializers

    def validate(self, value):
        print("OK")
    # filterset_fields = ['status', 'author__username']
    # search_fields = ["title","content","author__username","author__first_name","author__last_name"]
    # ordering_fields = ['publish', 'status']
    # ordering = ['-publish']

    # def get_queryset(self):
    #     queryset = Articale.objects.all()

    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status= status)

    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         #queryset = queryset.filter(author= author)
    #         queryset = queryset.filter(author__username= author)
            
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsAuthorOrReadOnly, IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]  


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     # def get_queryset(self):
#     #     print("__________________________")
#     #     print(self.request.user)
#     #     print(self.request.auth)
#     #     print("__________________________")
#         # return User.objects.all()
#     serializer_class = UserSerializers
#     #permission_classes = (IsSuperUser,)
#     permission_classes = (IsSuperuserOrStaffReadOnly,)

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#     #permission_classes = (IsSuperUser,)
#     permission_classes = (IsSuperuserOrStaffReadOnly,)


class UserViewSet(ModelViewSet):
    #queryset = User.objects.all()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperuserOrStaffReadOnly,)


# class AuthorRetrieve(RetrieveAPIView):
#     # queryset = get_user_model().objects.all()
#     queryset = get_user_model().objects.filter(is_staff=True)
#     serializer_class = AuthorSerializers


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     # def get(self,request):
#     #     return Response({"method": "get"})

#     # def post(self,request):
#     #     return Response({"method": "post"})

#     # def put(self,request):
#     #     return Response({"method": "put"})

#     # def delete(self,request):
#     #     return Response({"method": "delet"})

#     def delete(self,request):
#         request.auth.delete()
#         #return Response({"msg": "Token revoke"})
#         return Response(status=204)


def about_page(request):
    contex = {
    }
    return render(request, 'about_page.html',contex)

