# Emailer

Emailer provides

1. a decorator to send emails on error instead of raise an error

## Example

    

    ee = EmailError(
        from_addr = 'me@example.com',
        to_addr = 'others@example.com',
        smtp_addr = '10.0.0.1@some-smtp.com')

    @ee.email_on_error()
    def make_a_error():

        a = 1
        b = '2'
        print(a + b)

        return a

    make_a_error()

