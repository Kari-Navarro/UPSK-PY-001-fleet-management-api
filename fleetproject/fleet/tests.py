'''Testear modelos, llamada http y vistas'''
import json
from django.test import TestCase
from django.urls import reverse
from .models import Taxis #Trajectories

class ListTaxisViewTest(TestCase):
    def setUp(self):
        Taxis.objects.create(plate='ABCD-1234')

    def test_list_taxis_view(self):
        url = reverse('taxi_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(len(data), 1)  

#class ListTrajectoriesViewTest(TestCase):
 #   def setUp(self):
