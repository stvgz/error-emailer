import unittest
from erroremailer import EmailError
class TestEmail(unittest.TestCase):


    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()


    def test_email(self):

        ee = EmailError(from_addr='me', 
                        to_addr = 'others@example.com',
                        smtp_addr = '1.2.3.4',
                        email_on_error = False)

        @ee.email_on_error()
        def make_a_error():

            a = 1
            b = '2'
            print(a + b)

            return a


        r = make_a_error()

        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()