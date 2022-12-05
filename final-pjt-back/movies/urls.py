from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:movie_pk>/', views.movie_detail),
    
    path('<int:movie_pk>/review_list_create/', views.review_list_create), # 리뷰 게시글 작성을 위한
    path('review_detail/<int:review_pk>/', views.review_detail),
    path('review/<int:review_pk>/', views.review_update_delete),

    path('review_comments/<int:review_pk>/', views.review_comment_list),
    path('<int:review_pk>/review_comment/', views.create_review_comment),
    path('review_comment/<int:review_pk>/<int:review_comment_pk>/', views.review_comment_delete_update),

    path('recommend/', views.recommend),
    path('<int:my_pk>/<int:movie_id>/like/', views.movie_like),
    path('<int:my_pk>/<int:movie_id>/is_liked/', views.is_liked),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users),
    path('<int:user_pk>/like/review/', views.user_like_movies),

    path('info/', views.users_info),

    path('recommended/', views.recommended, name='recommended'),
    path('current_popularity/', views.current_popularity),

    path('list/', views.MovieListView.as_view())
]
