# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Articale
from .serializers import ArticleSerializers, UserSerializers
from django.shortcuts import  render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
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
    serializer_class = UserSerializers
    #permission_classes = (IsSuperUser,)
    permission_classes = (IsSuperuserOrStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    #permission_classes = (IsSuperUser,)
    permission_classes = (IsSuperuserOrStaffReadOnly,)



def about_page(request):
    contex = {
    }
    return render(request, 'about_page.html',contex)

