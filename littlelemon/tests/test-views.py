from django.test import TestCase

from restaurant.models import MenuItem

#TestCase class
# class MenuViewTest(TestCase):
#     def setUp(self):
#         MenuItem.objects.create(title="IceCream", price=80, inventory=100)
#         MenuItem.objects.create(title="Beer", price=75, inventory=100)

#     def test_getall(self):
#         response = client.get(reverse('get_post_puppies'))
#         # get data from db
#         puppies = Puppy.objects.all()
#         serializer = PuppySerializer(puppies, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)