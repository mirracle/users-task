import json
import requests
import re
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from googletrans import Translator
from .models import User, UserLogin, UserId, UserName, UserLocation, UserPicture, LocationCoordinates, LocationTimezone
from .serializer import UserSerializer, DigitsFromHashSerializer, UserShortInfoSerializer
from string import printable, ascii_letters, ascii_lowercase
from rest_framework.response import Response
from rest_framework import generics, status

translator = Translator()


class UserGetAndCreateView(APIView):
    @staticmethod
    def get(request):
        request_data = requests.get('https://randomuser.me/api/').json()
        data = request_data['results'][0]
        # creating user
        for letter in data['name']['first']:
            if letter not in ascii_lowercase:
                text = translator.translate(data['name']['first'])
                data['name']['first'] = text.text.lower()
                break
        for letter in data['name']['last']:
            if letter not in ascii_lowercase:
                text = translator.translate(data['name']['last'])
                data['name']['last'] = text.text.lower()
                break
        for letter in data['location']['city']:
            if letter not in ascii_lowercase:
                text = translator.translate(data['location']['city'])
                data['location']['city'] = text.text.lower()
                break
        mail = data['name']['first'][:2] + data['name']['last'] + '@' + data['location']['city'] + '.' + data[
            'nat'].lower()
        user_instance = User.objects.create(gender=data['gender'], email=mail, dob=data['dob']['date'],
                                            registered=data['registered']['date'], phone=data['phone'],
                                            cell=data['cell'], nat=data['nat'])
        user_instance.save()
        # creating user login
        login_data = data['login']
        md5_digit = ''.join(re.findall(r'\d', login_data['md5']))
        md5_chars = ''.join(re.findall(r'[a-z]', login_data['md5']))
        sha1_digit = ''.join(re.findall(r'\d', login_data['sha1']))
        sha1_chars = ''.join(re.findall(r'[a-z]', login_data['sha1']))
        sha256_digit = ''.join(re.findall(r'\d', login_data['sha256']))
        sha256_chars = ''.join(re.findall(r'[a-z]', login_data['sha256']))
        user_login_instance = UserLogin.objects.create(user=user_instance, uuid=login_data['uuid'],
                                                       username=login_data['username'], password=login_data['password'],
                                                       salt=login_data['salt'], md5=login_data['md5'],
                                                       md5_digit=md5_digit, sha1=login_data['sha1'],
                                                       md5_chars=md5_chars, sha1_digit=sha1_digit,
                                                       sha1_chars=sha1_chars, sha256_digit=sha256_digit,
                                                       sha256=login_data['sha256'], sha256_chars=sha256_chars)
        user_login_instance.save()
        # creating user id
        id_data = data['id']
        user_id_instance = UserId.objects.create(name=id_data['name'], value=id_data['value'], user=user_instance)
        user_id_instance.save()
        # crating user name
        name_data = data['name']
        user_name_instance = UserName.objects.create(user=user_instance, title=name_data['title'],
                                                     first=name_data['first'], last=name_data['last'])
        user_name_instance.save()
        # creating user location
        location_data = data['location']
        for letter in location_data['street']:
            if letter not in printable:
                text = translator.translate(location_data['street'])
                location_data['street'] = text.text.lower()
                break
        for letter in location_data['state']:
            if letter not in printable:
                text = translator.translate(location_data['state'])
                location_data['state'] = text.text.lower()
                break
        user_location_instance = UserLocation.objects.create(user=user_instance, street=location_data['street'],
                                                             city=location_data['city'], state=location_data['state'],
                                                             postcode=location_data['postcode'])
        user_location_instance.save()
        # creating user picture
        picture_data = data['picture']
        user_picture_instance = UserPicture.objects.create(user=user_instance, large=picture_data['large'],
                                                           medium=picture_data['medium'],
                                                           thumbnail=picture_data['thumbnail'])
        user_picture_instance.save()
        # creating user LocationCoordinates
        coordinates_data = location_data['coordinates']
        user_coordinates_instance = LocationCoordinates.objects.create(location=user_location_instance,
                                                                       latitude=coordinates_data['latitude'],
                                                                       longitude=coordinates_data['longitude'])
        user_coordinates_instance.save()
        # creating user timezone
        timezone_data = location_data['timezone']
        user_timezone_instance = LocationTimezone.objects.create(location=user_location_instance,
                                                                 offset=timezone_data['offset'],
                                                                 description=timezone_data['description'])
        user_timezone_instance.save()
        serializer = UserSerializer(instance=user_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DigitsFromHashView(APIView):
    @staticmethod
    def get(request):
        serializer = DigitsFromHashSerializer(instance=UserLogin.objects.all().last())
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserShortInfoView(APIView):
    @staticmethod
    def get(request):
        serializer = UserShortInfoSerializer(instance=User.objects.all().last())
        return Response(serializer.data, status=status.HTTP_200_OK)


class Pagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 200


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    pagination_class = Pagination
