from django.test import TestCase
from .models import Task , Priority
from lists.models import ListModel
from django.contrib.auth import get_user_model 


# test tasks model 
class TestTask(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="abdelrahman",
            email="abdo@gmail.com",
            password="pass",
            name="abdelrahman ibrahem",
        )
        self.list_model = ListModel.objects.create(
            user=self.user,
            title= 'list1',
            descrption='descrption'
        )
        self.priority = Priority.objects.create(
            name="p1"
        )
    def test_tasks_model(self):
        task = Task.objects.create(
            title="title",
            is_compeleted=True,
            list_id=self.list_model,
            location='location',
            priority=self.priority
        )
        self.assertEqual(task.title , 'title')
        self.assertEqual(task.is_compeleted , True)
        self.assertEqual(task.list_id , self.list_model)
        self.assertEqual(task.location , 'location')
        self.assertEqual(task.priority , self.priority)