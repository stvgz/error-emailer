# Emailer

Emailer provides

a decorator to send emails on error instead of raise an error

Emails will be constructed as MIMEMultipart contains only simple text.
And sent throught smtp wihtout any authentication, which suitsmost of internal smtp servers.


## Installation

Install with pip

> pip install error-emailer

## Email construct

Email constructed as MIMEMultipart with default

> error_msg_title = 'Error'

> error_msg_content = 'Error occurred'



## Example: Use decorator

    from erroremailer import EmailError

    ee = EmailError(
        from_addr = 'me@example.com',
        to_addr = 'others@example.com',
        smtp_addr = '10.0.0.1@some-smtp.com',
        # set send_email to False for test
        send_email = False,
        error_msg_title = 'Error occured in my best script"
        error_msg_content = 'Error occured in my best script"
        )

    @ee.email_on_error()
    def make_a_error():

        a = 1
        b = '2'
        print(a + b)

        return a

    make_a_error()


## Example: Use send email directly

    from erroremailer import EmailError

    ee = EmailError(
        from_addr = 'me@example.com',
        to_addr = 'others@example.com',
        smtp_addr = '10.0.0.1@some-smtp.com',
        # set send_email to False for test
        send_email = False,
        error_msg_title = 'Error occured in my best script"
        error_msg_content = 'Error occured in my best script"
        )

    def make_a_error():

        a = 1
        b = '2'
        print(a + b)

        return a


    if __name__ == '__main__':
        
        try:
            make_a_error()
        except:
            ee.send_error_email()
        finally:
            pass

        

    