from django.test import TestCase, RequestFactory
from licenseexam.models import TestResult
import licenseexam.views
from django.contrib.auth.models import User


class APITestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        User.objects.create(username="unit_test", email='noreply@google.com', password='secure_passw567')

    def testAddSequence(self):
        request_data = {'user':'unit_test', 'password':'secure_passw567'}
        request = self.factory.post('api/auth/', request_data, format='multipart')
        response = licenseexam.views.login(request)
        self.assertEqual(response.status_code, 200)

        token = response.data["token"]
        request_data = {'question_count':'12', 'result_time':'123'}
        request = self.factory.post('api/addresult/', request_data, Authorization=token)
        response = licenseexam.views.add_new_result(request)
        self.assertEqual(response.status_code, 200)

class ResultDataTestCase (TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        User.objects.create(username="unit_test", email='noreply@google.com', password='secure_passw567')

    def testTakeResults(self):
        request_data = {'user': 'unit_test', 'password': 'secure_passw567'}
        request = self.factory.post('api/auth/', request_data, format='multipart')
        response = licenseexam.views.login(request)

        token = response.data["token"]
        request_data = {'question_count': '12', 'result_time': '123'}
        request = self.factory.post('api/addresult/', request_data, Authorization=token)
        response = licenseexam.views.add_new_result(request)

        result_data = TestResult.objects.all().filter(user='unit_test')
        self.assertEqual(len(result_data), 1)
        for result in result_data:
            self.assertEqual(result.result_time, 123)
            self.assertEqual(result.question_count, 12)
