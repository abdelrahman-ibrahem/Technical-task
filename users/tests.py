from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse 


# create class for test user 

class TestUser(TestCase):
    def test_user_model(self):
        user = get_user_model().objects.create(
            username="abdelrahman",
            email="abdo@gmail.com",
            password="pass",
            name="abdelrahman ibrahem",
        )
        self.assertEqual(user.username , 'abdelrahman')
        self.assertEqual(user.email , 'abdo@gmail.com')
        self.assertEqual(user.name , 'abdelrahman ibrahem')