from djoser.conf import settings
from djoser.serializers import UserCreateSerializer, UserSerializer, User


class AppUserSerializer(UserSerializer):
	class Meta(UserSerializer.Meta):
		model = User
		fields = tuple(User.REQUIRED_FIELDS) + (
			settings.USER_ID_FIELD,
			settings.LOGIN_FIELD,
			'first_name',
		)


class CreateAppUserSerializer(UserCreateSerializer):
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = tuple(User.REQUIRED_FIELDS) + (
			settings.LOGIN_FIELD,
			settings.USER_ID_FIELD,
			"password",
			'first_name',
		)
