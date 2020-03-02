from django.test import TestCase, RequestFactory
from licenseexam.models import TestResult
import licenseexam.views
from django.contrib.auth.models import User


class APITestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        User.objects.create_user(username="unittest", password='securepassw567')

    def testAddSequence(self):
        request_data = {'username': 'unittest', 'password': 'securepassw567'}
        request = self.factory.post('api/auth/', request_data, format='multipart')
        response = licenseexam.views.login(request)
        self.assertEqual(response.status_code, 200)

        token = response.data["token"]
        request_data = {'question_count': '12', 'result_time': '123'}
        request = self.factory.post('api/addresult/', request_data, format='multipart',
                                    HTTP_AUTHORIZATION='Token ' + token)
        response = licenseexam.views.add_new_result(request)
        self.assertEqual(response.status_code, 200)

        result_data = TestResult.objects.filter(user=request.user)
        self.assertEqual(len(result_data), 1)
        self.assertEqual(result_data[0].result_time, 123)
        self.assertEqual(result_data[0].question_count, 12)



