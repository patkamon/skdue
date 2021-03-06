import json
from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.status import *
from .utils import convert_response


class RegisterTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(   "Past", 
                                            "past@test.com", 
                                            "past1234")
        self.user1.save()
        self.valid_data = {  "username":"Peem",
                                "email":"peem@test.com",
                                "password":"peem_pong"
                            }
        self.exist_account = {  "username":"Past",
                                "email":"past@test.com",
                                "password":"past1234"
                            }
        
    def test_valid_register(self):
        self.register = User.objects.create_user(
                     "Peem",
                     "peem@test.com",
                     "peem_pong")
        self.register.save()
        self.user = authenticate(self.valid_data,
                            username="Peem",
                            password="peem_pong")
        self.assertNotEqual(None, self.user)

    def test_exist_username(self):
        data = {"status": "failed", "msg": "Account created fail"}
        expect_data = json.dumps(data)
        response = self.client.post(
            reverse('api_v2:register'),
            data = self.exist_account
        )
        response_data = convert_response(response.content)
        self.assertJSONEqual(expect_data, response_data)
        self.assertEqual(HTTP_400_BAD_REQUEST, response.status_code)

    def test_get(self):
        response = self.client.get(reverse('api_v2:register'))
        self.assertEqual(HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

    def test_valid_username(self):
        response = self.client.post(
            reverse('api_v2:register'),
            self.valid_data
        )
        self.assertEqual(HTTP_200_OK, response.status_code)