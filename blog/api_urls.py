from django.urls import path

# from .api import PostListCreateApiView,PostRetrieveUpdateDestroyApiView,CommentListCreateApiView,CommentRetrieveUpdateDestroyApiView
from .api import PostViewSets, CommentViewSets

from rest_framework.routers import DefaultRouter




router= DefaultRouter()

router.register('posts', PostViewSets)
router.register('comments', CommentViewSets)

urlpatterns = router.urls

# urlpatterns=[

#     path('posts/', PostListCreateApiView.as_view()),
#     path('posts/<int:pk>/', PostRetrieveUpdateDestroyApiView.as_view()),

#     path('comments/', CommentListCreateApiView.as_view()),
#     path('comments/<int:pk>/', CommentRetrieveUpdateDestroyApiView.as_view()),
# ]