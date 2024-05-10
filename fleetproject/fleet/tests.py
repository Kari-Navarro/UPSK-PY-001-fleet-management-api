'''Testear modelos, llamada http y vistas'''
import json
from django.test import TestCase
from django.urls import reverse
from .models import Taxis #Trajectories

class TestStatusCode(TestCase):
    def test_taxis(self):
        response = self.client.get('/taxis/')
        self.assertEqual(response.status_code, 200)
    
    def test_trajectories(self):
        response = self.client.get('/trajectories/')
        self.assertEqual(response.status_code, 200)
    
    def test_trajectories_id(self):
        response = self.client.get('/trajectories/taxi_id/?taxi_id=9275')
        self.assertEqual(response.status_code,200)

    def test_plate(self):
        response = self.client.get('/plate/?plate=MDEF-7585')
        self.assertEqual(response.status_code, 200)

class Test_paginator(TestCase):
    def setUp(self):
        Taxis.objects.create(plate='ABCD-1234')
        Taxis.objects.create(plate='EFGH-5678')
        Taxis.objects.create(plate='IJKL-9101')
        Taxis.objects.create(plate='MNÑO-1213')
        Taxis.objects.create(plate='PQRS-1415')

    def test_taxi_pagination(self):
        url = reverse('taxi_list')
        response = self.client.get(url)
        data =json.loads(response.content)
        self.assertEqual(data['total_pages'],1)#cantidad de pag. 1 (5regostrps)
        self.assertEqual(data['current_page'],1)
        self.assertEqual(data['next'],False)
        self.assertEqual(data['previous'],False)
        


#class ListTaxisViewTest(TestCase):
#    def setUp(self):
#        Taxis.objects.create(plate='ABCD-1234')

#    def test_list_taxis_view(self):
#        url = reverse('taxi_list')
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)

#        data = json.loads(response.content)
#        self.assertEqual(len(data), 1)  


