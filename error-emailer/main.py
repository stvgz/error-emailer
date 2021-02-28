from send_email import *



if __name__ == '__main__':

    ee = EmailError(from_addr='me')

    @ee.email_on_error()
    def make_a_error():

        a = 1
        b = '2'
        print(a + b)

        return a


    make_a_error()