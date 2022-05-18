from django.urls import include, path
# from .views import ArticleList, ArticleDetail, about_page, UserList, UserDetail
from .views import UserViewSet,ArticleViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'/articles', ArticleViewSet, basename="articles")
router.register(r'/users', UserViewSet, basename="users")

app_name = "api"

# urlpatterns = router.urls

urlpatterns = [
    path("",include(router.urls))
]
# urlpatterns = [
#     path("", ArticleList.as_view(), name= "list"),
#     path("/<int:pk>", ArticleDetail.as_view(), name= "detail"),

#     path("/users", UserList.as_view(), name= "user-list"),
#     path("/users/<int:pk>", UserDetail.as_view(), name= "user-detail"),

#     path("/about", about_page),

# ]
