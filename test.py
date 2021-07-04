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
                        send_email_on_error = False)

        @ee.email_on_error()
        def make_a_error():

            a = 1
            b = '2'
            print(a + b)

            return a


        r = make_a_error()

        self.assertEqual(1,1)


    def test_send_email(self):
        ee = EmailError(
            from_addr = 'me@example.com',
            to_addr = 'others@example.com',
            smtp_addr = '10.0.0.1@some-smtp.com',
            # set send_email to False for test
            send_email_on_error = False,
            error_msg_title = 'Error occured in my best script',
            error_msg_content = 'Error occured in my best script'
            )

        def make_a_error():

            a = 1
            b = '2'
            print(a + b)

            return a

        try:
            make_a_error()
        except:
            ee.send_error_email()
            print('Sent email')

        finally:
            pass



if __name__ == '__main__':

    unittest.main()