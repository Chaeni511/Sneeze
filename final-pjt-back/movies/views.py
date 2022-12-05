from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from random import sample

from .models import Movie, Review, ReviewComment, Genre
from .serializers import MovieSerializer, ReviewListSerializer, ReviewCommentSerializer, ReviewCommentReadSerializer, ReviewReadSerializer
from accounts.serializers import UserSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


class MovieListView(ListAPIView):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  pagination_class = PageNumberPagination
  

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
  # print(movie_pk)
  # print(request)
  if request.method == 'GET':
    movie = get_object_or_404(Movie, movie_id=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

  
### review

@api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewReadSerializer(reviews, many=True)
    return Response(serializer.data)
  else:
    serializer = ReviewListSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))

      pre_point = movie.vote_average * movie.vote_count
      pre_count = movie.vote_count

      point = pre_point + int(request.data.get('rank'))
      count = movie.vote_count + 1
      new_vote_average = round(point/count, 2)

      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
        
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_comment_list(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comments = review.reviewcomment_set.all()
  serializer = ReviewCommentReadSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  serializer = ReviewCommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user, review=review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, id=review_pk)
    serializer = ReviewReadSerializer(review)
    return Response(serializer.data)



@api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if not request.user.reviews.filter(pk=review_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewListSerializer(review, data=request.data)
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      pre_point = movie.vote_average * (movie.vote_count - 1)
      pre_count = movie.vote_count - 1
      point = pre_point+ float(request.data.get('rank'))
      count = movie.vote_count
      new_vote_average = round(point/count, 2)
      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)

  else:
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=review.movie_id)
    pre_point = movie.vote_average * (movie.vote_count)
    pre_count = movie.vote_count
    point = pre_point - review.rank
    count = movie.vote_count-1
    new_vote_average = round(point/count, 2)
    movie.vote_average = new_vote_average
    movie.vote_count = count
    movie.save()
    review.delete()
    return Response({ 'id': review_pk })


@api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_delete_update(request, review_pk, review_comment_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comment = review.reviewcomment_set.get(pk=review_comment_pk)
  
  if not request.user.review_comments.filter(pk=review_comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewCommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
  else:
    comment.delete()
    return Response({ 'id': review_comment_pk })


@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request):
  favorite_movies = Movie.objects.all().order_by('-vote_average')[:30]
  serializer1 = MovieSerializer(favorite_movies, many=True)
  shortest_movies = Movie.objects.all().order_by('runtime')[30:60]
  serializer2 = MovieSerializer(shortest_movies, many=True)
  # 리뷰 기반 장르 추천
  users_movies = set()

  like_movies = request.data.get('like_movies')
  
  movies = get_list_or_404(Movie)
  len_movies = len(movies)
  reviews = Review.objects.all()
  for review in reviews:
    movie = Movie.objects.get(pk=review.movie_id)
    if not movie in users_movies and movie.pk not in like_movies:
      users_movies.add(movie)
  if users_movies:
    users_movies = list(users_movies)
    serializer = MovieSerializer(users_movies[0])
    genre = serializer.data.get('genres')[0]
    # genre_name = Genre.objects.get(id=genre)
    
    idx = 1
    users_movies = set(users_movies)
    while len(users_movies) < 30 and idx <= len_movies:
      try:
        movie = Movie.objects.get(pk=idx)
        ser = MovieSerializer(movie)
        if ser.data.get('genres', False):
          if ser.data.get('genres')[0] == genre and movie.pk not in users_movies:
            users_movies.add(movie)
        idx += 1
      except:
        idx += 1
      if idx == len_movies:
        latest_movies = Movie.objects.all().order_by('vote_count')
        while len(users_movies) < 30:
           users_movies.add(latest_movies.pop())
        users_movies = list(users_movies)
  else:
    users_movies = Movie.objects.all().order_by('-vote_count')[:30]

  # 좋아요 기반
  my_movies = []
  User = request.user
  my_genres = {}
  my_movies = User.like_movies.all()
  
  if my_movies:
    for movie in my_movies:
        genres = movie.genres.all()
        for genre in genres:
            if genre.pk in my_genres:
                my_genres[genre.pk] += 1
            else:
                my_genres[genre.pk] = 1

    my_genres = sorted(my_genres, key=lambda x: my_genres[x])[:3]

    movies = get_list_or_404(Movie)
    recommendations_list = set()
    for my_genre in my_genres:
        for movie in movies:
            genres = movie.genres.all()
            for genre in genres:
                if genre.pk == my_genre:
                    recommendations_list.add(movie)
                    break
    
    recommendations_list = list(recommendations_list)
    recommendations = sorted(recommendations_list, key=lambda x: x.popularity, reverse=True)[:30]

    serializer4 = MovieSerializer(recommendations, many=True)
    serializer3 = MovieSerializer(users_movies, many=True)
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data])
  else:
    serializer3 = MovieSerializer(users_movies, many=True)
    return Response([serializer1.data, serializer2.data, serializer3.data, []])


@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_id):
  movie = get_object_or_404(Movie, movie_id=movie_id)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)


@api_view(['POST'])
def is_liked(request, my_pk, movie_id):
  movie = get_object_or_404(Movie, movie_id=movie_id)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      liking = True
  else:
      liking = False
  return Response(liking)


@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  data = []
  movies = me.like_movies.all()
  # print('=====================')
  # print(movies)
  # print('=====================')
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie.id)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  
  return Response(data)


@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def like_movie_users(request, my_pk):
  users = []
  user = get_object_or_404(get_user_model(), pk=my_pk)
  movies = user.like_movies.all()
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie.pk)
    serializer = MovieSerializer(movie)
    # print(serializer.data)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)

  return Response(users)


@api_view(['post'])
def user_like_movies(request, user_pk):
  like_movies_id = request.data.get('like_movies')
  review_ids = request.data.get('reviews')
  movies = Movie.objects.all()

  review_movie_id = []
  for review_id in review_ids:
    review = Review.objects.get(pk=review_id)
    review_movie_id.append(review.movie_id)

  review_movies = []
  like_movies = []
  for movie in movies:
    if movie.pk in like_movies_id:
      like_movies.append(movie)
    if movie.pk in review_movie_id:
      review_movies.append(movie)
  serializers = MovieSerializer(like_movies, many=True)
  review_serializers = MovieSerializer(review_movies, many=True)
  return Response([serializers.data, review_serializers.data])



@api_view(['POST'])
def users_info(request):
  users = request.data.get('users')
  movies = []
  for user in users:
      user = get_object_or_404(get_user_model(), pk=user)
      serializer = UserSerializer(user)
      # print(serializer.data)
      like_movies = serializer.data.get('like_movies')
      for movie in like_movies:
          if movie not in movies:
              movies.append(movie)
  
  return Response(movies)




@api_view(['GET'])
def recommended(request):
  if request.user.is_authenticated:
    movies = get_list_or_404(Movie)
    User = request.user
    my_genres = {}
    my_movies = User.like_movies.all()
    
    if my_movies:
      for movie in my_movies:
          genres = movie.genres.all()
          for genre in genres:
              if genre.pk in my_genres:
                  my_genres[genre.pk] += 1
              else:
                  my_genres[genre.pk] = 1

      my_genres = sorted(my_genres, key=lambda x: my_genres[x])[:3]

      recommendations_list = set()
      for my_genre in my_genres:
          for movie in movies:
              genres = movie.genres.all()
              for genre in genres:
                  if genre.pk == my_genre:
                      recommendations_list.add(movie)
                      break
      recommendations = sample(recommendations_list, 20)
      serializer = MovieSerializer(recommendations)
      # liked = True
    else:
        movies = get_list_or_404(Movie)
        recommendations = sample(movies, 20)
        serializer = MovieSerializer(recommendations, many=True)
        # print('============================')
        # liked = False

    # context = {
    #     'my_movies': my_movies,
    #     'my_genres': my_genres,
    #     'recommendations': recommendations,
    #     'liked': liked
    # }
    return Response(serializer.data)
    # return render(request, 'movies/recommended.html', context)
  else:
    movies = get_list_or_404(Movie)
    recommendations = sample(movies, 10)
    serializer = MovieSerializer(recommendations)
  # return redirect('accounts:login')


@api_view(['GET'])
def current_popularity(request):
  if request.method == 'GET':
    movies = Movie.objects.order_by('-popularity')[:30]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)