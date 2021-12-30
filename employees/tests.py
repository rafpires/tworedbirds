

from rest_framework.test import APIRequestFactory, APITestCase


# Create your tests here.
class DepartmentTest(APITestCase):

    def test_list(self):
        factory = APIRequestFactory()
        request = factory.get('/departments/')
        response = view(request)