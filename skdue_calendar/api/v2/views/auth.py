from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from skdue_calendar.models import Calendar
from skdue_calendar.serializers import UserSerializer, CalendarSerializer


class DemoView(APIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)             

    def get(self, request):
        content = {'message': 'Hello! This is a Demo'}
        return Response(content)


class GetAuthToken(APIView):

    @csrf_exempt
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user":  UserSerializer(user).data,
                "calendar": CalendarSerializer(Calendar.objects.get(user=user)).data
            })

        return Response({"msg": "something wrong"})