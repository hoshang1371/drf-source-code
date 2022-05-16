# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Articale
from .serializers import ArticleSerializers, UserSerializers
from django.shortcuts import  render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser ,IsAuthenticated
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperuserOrStaffReadOnly

class ArticleList(ListCreateAPIView):
    queryset = Articale.objects.all()
    serializer_class = ArticleSerializers

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Articale.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    # def get_queryset(self):
    #     print("__________________________")
    #     print(self.request.user)
    #     print(self.request.auth)
    #     print("__________________________")
        # return User.objects.all()
    serializer_class = UserSerializers
    #permission_classes = (IsSuperUser,)
    permission_classes = (IsSuperuserOrStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    #permission_classes = (IsSuperUser,)
    permission_classes = (IsSuperuserOrStaffReadOnly,)


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

