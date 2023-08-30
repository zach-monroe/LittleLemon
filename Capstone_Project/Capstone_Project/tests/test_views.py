from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from LittleLemon.models import Menu  # Import your Menu model

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=150, inventory=50)

    def test_getall(self):
        url = reverse("menu") 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = response.data
        expected_data = [
            {
                "title": "IceCream",
                "price": "80.00",
                "inventory": 100
            },
            {
                "title": "Pizza",
                "price": "150.00",
                "inventory": 50
            }
        ]
        self.assertEqual(serialized_data, expected_data)
