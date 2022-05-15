from django.urls import include, path
from .views import ArticleList, ArticleDetail, about_page, UserList, UserDetail

app_name = "api"

urlpatterns = [
    path("", ArticleList.as_view(), name= "list"),
    path("/<int:pk>", ArticleDetail.as_view(), name= "detail"),

    path("/users", UserList.as_view(), name= "user-list"),
    path("/users/<int:pk>", UserDetail.as_view(), name= "user-detail"),

    path("/about", about_page),

]