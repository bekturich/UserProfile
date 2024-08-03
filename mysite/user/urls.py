from django.urls import path
from .views import *

urlpatterns = [
    path('', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name= 'UserProfile_list'),
    path('<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='UserProfile_detail'),

    path('follow', FollowViewSet.as_view({'get': 'list', 'post': 'create'}), name='Follow_list'),
    path('follow/<int:pk>/', FollowViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='Follow_detail'),

    path('post', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='Post_list'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve',
                                                'put': 'update',
                                                'delete': 'destroy'}), name='Post_detail'),

    path('comment', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='Comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='Comment_detail')
]