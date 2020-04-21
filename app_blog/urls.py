from . import views
from django.urls import path

urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('', views.vw_PostsList, name='index_url'),
    path('article/<slug:prm_post_slug>/', views.vw_PostDetail, name='post_detail_url'),
]
