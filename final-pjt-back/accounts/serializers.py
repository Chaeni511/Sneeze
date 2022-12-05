from rest_framework import serializers
# from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     # write_only는 시리얼라이징은 하지만 응답에는 포함시키지 않는다는 의미
#     # 비밀번호를 응답에 표현한다면 보안상의 유출이 되는 것이기 떄문

#     password = serializers.CharField(write_only=True)

#     class Meta : 
#         model = User
#         fields = ('username', 'password','email')


class UserDetailSerializer(serializers.ModelSerializer):
    # write_only는 시리얼라이징은 하지만 응답에는 포함시키지 않는다는 의미
    # 비밀번호를 응답에 표현한다면 보안상의 유출이 되는 것이기 떄문

    # password = serializers.CharField(write_only=True)

    class Meta : 
        model = User
        fields = ('username','email','id')


# class CustomRegisterSerializer(RegisterSerializer):
#     followers = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)    
#     # followers = followersSerializers

#     # class Meta:
#     #     model = User
#     #     fields = [
#     #         'id', 
#     #         'username', 
#     #     ]

#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['followers'] = self.validated_data.get('followers','')
#         return data



class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies', 'password', 'email', 'followings', 'reviews', 'followers',)
        read_only_fields = ('followings', 'reviews', 'like_movies', 'followers',)
