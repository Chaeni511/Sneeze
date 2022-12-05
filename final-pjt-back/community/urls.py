from django.urls import path
from . import views


urlpatterns = [
    path('community_list_create/', views.community_list_create), # 게시글 작성을 위한
    path('detail/<int:community_pk>/', views.community_detail), 
    path('community/<int:community_pk>/', views.community_update_delete),

    path('comments/<int:community_pk>', views.comment_list),
    path('<int:community_pk>/comment/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_delete_update),
]