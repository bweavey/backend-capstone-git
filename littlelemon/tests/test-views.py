from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

client = Client()

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Beer", price=75, inventory=100)

    def test_getall(self):
        response = client.get(reverse('menu-items'))
        # get data from db
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)