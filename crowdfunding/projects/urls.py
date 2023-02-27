# All below added by me
from django.urls import path
from . import views

urlpatterns = [
	path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'), #Added
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'), #added from DRF doc 2
    path('comments/', views.CommentList.as_view(), name='comment-list'), #added
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment'), #added
]
