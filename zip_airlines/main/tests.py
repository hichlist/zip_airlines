from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Airplane

class AirplaneTestCase(TestCase):
    def setUp(self):
        Airplane.objects.create(airplane_id=2, passengers=10)
        Airplane.objects.create(airplane_id=4, passengers=14)

    def test_airplane_consumption(self):
        airplane1 = Airplane.objects.get(airplane_id=2)
        airplane2 = Airplane.objects.get(airplane_id=4)
        self.assertEqual(airplane1.consumption, 0.5745177444479562)
        self.assertEqual(airplane2.consumption, 1.1370354888959124)

    def test_airplane_fuel_tank(self):
        airplane1 = Airplane.objects.get(airplane_id=2)
        airplane2 = Airplane.objects.get(airplane_id=4)
        self.assertEqual(airplane1.fuel_tank, 400)
        self.assertEqual(airplane2.fuel_tank, 800)

    def test_airplane_minutes_to_fly(self):
        airplane1 = Airplane.objects.get(airplane_id=2)
        airplane2 = Airplane.objects.get(airplane_id=4)
        self.assertEqual(airplane1.minutes_to_fly, 696)
        self.assertEqual(airplane2.minutes_to_fly, 703)


class APIAirplaneTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', is_staff=True, password='test')
        self.user.save()
        self.client.login(username='test', password='test')
        self.client.post('/airplanes/', {'passengers': 12, 'airplane_id': 3})

    def test_serializer(self):
        self.client.login(username='test', password='test')
        response = self.client.get('/airplanes/')
        self.data = dict(response.data[0])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.data['fuel_tank'], 600)
        self.assertEqual(self.data['consumption'], 0.9028898309344879)
        self.assertEqual(self.data['minutes_to_fly'], 664)
