from django.urls import include, path
from . import views
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'posts', views.PostViewSet)
# router.register(r'post-list', views.postList)

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('post-list/', views.postList, name='post-list'),
    path('post-detail/<str:pk>', views.postDetail, name='post-detail'),
    path('post-create/', views.postCreate, name='post-create'),
    path('post-update/<str:pk>/', views.postUpdate, name='post-update'),
    path('post-delete/<str:pk>/', views.postDelete, name='post-delete'),

    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
