from django.test import TestCase
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