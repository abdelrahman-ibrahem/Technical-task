from django.test import TestCase
from .models import ListModel
from django.contrib.auth import get_user_model

# create class for test list model
class TestListModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="abdelrahman",
            email="abdo@gmail.com",
            password="pass",
            name="abdelrahman ibrahem",
        )
    

    def test_list_model(self):
        list_model = ListModel.objects.create(
            user=self.user,
            title= 'list1',
            descrption='descrption'
        )
        self.assertEqual(list_model.user , self.user)
        self.assertEqual(list_model.title , 'list1')
        self.assertEqual(list_model.descrption , 'descrption')

