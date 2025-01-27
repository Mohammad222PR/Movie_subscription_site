from django.urls import path
from . import views

app_name = 'panel'
urlpatterns = [
    path('profile', views.Profile.as_view(), name="profile"),
    path('article-list', views.ArticleList.as_view(), name='article-list'),
    path("article-create",views.ArticleCreate.as_view(),name="article-create"),
    path('update/article/<int:pk>', views.ArticleUpdate.as_view(), name="article-update"),
    path('delete/article/<int:pk>', views.ArticleDelete.as_view(), name="article-delete"),

]