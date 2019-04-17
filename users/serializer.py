from rest_framework import serializers
from .models import User, UserLogin, UserId, UserName, UserLocation, UserPicture, LocationCoordinates, LocationTimezone
from datetime import datetime
from dateutil.relativedelta import relativedelta


class LocationTimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationTimezone
        fields = ('offset', 'description')


class LocationCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCoordinates
        fields = ('latitude', 'longitude')


class UserLocationSerializer(serializers.ModelSerializer):
    coordinates = LocationCoordinatesSerializer(many=False)
    timezone = LocationTimezoneSerializer(many=False)

    class Meta:
        model = UserLocation
        fields = ('street', 'city', 'state', 'postcode', 'coordinates', 'timezone')


class UserPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPicture
        fields = ('large', 'medium', 'thumbnail')


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = ('title', 'first', 'last')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ('uuid', 'username', 'password', 'salt', 'md5', 'sha1', 'sha256', 'md5_chars', 'md5_digit',
                  'sha1_chars', 'sha1_digit', 'sha256_chars', 'sha256_digit')


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserId
        fields = ('name', 'value')


class UserSerializer(serializers.ModelSerializer):
    dob = serializers.SerializerMethodField()
    registered = serializers.SerializerMethodField()
    location = UserLocationSerializer(many=False)
    name = UserNameSerializer(many=False)
    picture = UserPictureSerializer(many=False)
    id_user = UserIdSerializer(many=False)
    login = UserLoginSerializer(many=False)

    class Meta:
        model = User
        fields = ('gender', 'email', 'phone', 'cell', 'nat', 'dob', 'registered', 'location', 'name', 'picture',
                  'id_user', 'login')

    @staticmethod
    def get_dob(self):
        if self.dob == str:
            date = datetime.strptime(self.dob, '%Y-%m-%dT%H:%M:%SZ')
        else:
            date = self.dob.replace(tzinfo=None)
        age = relativedelta(datetime.now(), date).years
        return {'date': date, 'age': age}

    @staticmethod
    def get_registered(self):
        if self.registered == str:
            date = datetime.strptime(self.registered, '%Y-%m-%dT%H:%M:%SZ')
        else:
            date = self.registered.replace(tzinfo=None)
        age = relativedelta(datetime.now(), date).years
        return {'date': date, 'age': age}


class DigitsFromHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ('md5_digit', 'sha1_digit', 'sha256_digit')


class NameShort(serializers.ModelSerializer):
    class Meta:
        model = UserName
        fields = ('first', 'last')


class LocationCity(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = ('city',)


class UserShortInfoSerializer(serializers.ModelSerializer):
    name = NameShort(many=False)
    location = LocationCity(many=False)

    class Meta:
        model = User
        fields = ('name', 'email', 'location', 'nat')
