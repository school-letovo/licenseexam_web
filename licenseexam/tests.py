from django.test import TestCase, RequestFactory
from licenseexam.models import TestResult
import licenseexam.views
from django.contrib.auth.models import User


class APITestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        User.objects.create(username="unit_test", email='noreply@google.com', password='secure_passw567')

    def testAddSequence(self):
        request_data = {'username':'unit_test', 'password':'secure_passw567'}
        request = self.factory.post('api/auth/', request_data, format='multipart')
        response = licenseexam.views.login(request)
        print(response.data['error'])
        self.assertEqual(response.status_code, 200)

        token = response.data["token"]
        request_data = {'question_count':'12', 'result_time':'123'}
        request = self.factory.post('api/addresult/', request_data, Authorization=token)
        response = licenseexam.views.add_new_result(request)
        self.assertEqual(response.status_code, 200)
