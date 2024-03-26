from django.contrib.auth.models import User
from .models import Seecret
from rest_framework import status
from rest_framework.test import APITestCase


class SeecretListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='alekos', password='password')

    def test_can_list_posts(self):
        adam = User.objects.get(username='alekos')
        Seecret.objects.create(owner=adam, title='a title')
        response = self.client.get('/seecrets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='alekos', password='password')
        response = self.client.post('/seecrets/', {'title': 'a title'})
        count = Seecret.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/seecrets/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)