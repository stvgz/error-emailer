# Emailer

Emailer provides

a decorator to send emails on error instead of raise an error

Emails will be constructed as MIMEMultipart contains only simple text.
And sent throught smtp wihtout any authentication, which suitsmost of internal smtp servers.

## Use as Example

    from erroremailer import EmailError

    ee = EmailError(
        from_addr = 'me@example.com',
        to_addr = 'others@example.com',
        smtp_addr = '10.0.0.1@some-smtp.com',
        # set send_email to False for test
        send_email = False
        )

    @ee.email_on_error()
    def make_a_error():

        a = 1
        b = '2'
        print(a + b)

        return a

    make_a_error()

