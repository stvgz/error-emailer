# Provide a decorator for error-handling
# Send email through simple smtp to alert instead of raise an error
# Mainly used in cases requires
# 1. low importance, not critical
# 1. requires some alerts and doesn't have to break the code
# 1. some part of the code still need to be executed even some code before already failed
# 1. etc

from email.mime.multipart import MIMEMultipart
import sys
import traceback
import datetime

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr,parseaddr

from typing import List

class EmailError():

    def __init__(self, from_addr: str = None, 
                to_addr : str or List = None, 
                smtp_addr : str = None, 
                error_msg_title = 'Error Occurred During Executing', 
                error_msg_content = 'type+value+traceback',
                raise_on_error = False,
                print_on_error = False, 
                send_email_on_error = True,
                send_email_timeout = 10,
                send_email_error = 'raise',
                verbose = False ) -> None:
        """
        Email error message, tracebacks when error occurs
        Email sent through simple smtp withou any authentication process. 
        Suits most of internal smtp service

        Input
        ----- 
        from_addr: str represents email address
        to_addr: str represnets email address or list of address
        verbose: boolean

        """

        self.from_addr = from_addr

        if type(to_addr) is str:
            self.to_addr = [to_addr]
        else:
            self.to_addr = to_addr

        self.smtp_addr = smtp_addr
        self.error_msg_title = error_msg_title
        self.error_msg_content = error_msg_content
        self.raise_on_error = raise_on_error,
        self.print_on_error = print_on_error,
        self.send_email_on_error = send_email_on_error
        self.verbose = verbose

        self.msg = None
        
    
    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))


    def make_email(self, content):
        """
        Compose email content with plain text
        Content contains type, value, traceback

        """
        msg = MIMEMultipart('mixed')

        msg['From'] = self._format_addr("Error-Emailer <{}>".format(self.from_addr))
        msg['To'] = self._format_addr("<{}>".format(self.to_addr))
        msg['Subject'] = Header(self.error_msg_title, 'utf-8').encode()

        # attach content as plain text
        time_fmt = datetime.datetime.utcnow()
        time_message = """Time(UTC): {} """.format(time_fmt)

        msg.attach(MIMEText(time_message, 'plain', 'utf-8'))

        # attach error tracebacks
        error_msg = content
        msg.attach(MIMEText(error_msg, 'plain', 'utf-8'))

        self.msg = msg


    def send_email(self):
        
        assert self.smtp_addr is not None, "Please Privide SMTP Addr"
        
        s = smtplib.SMTP(self.smtp_addr)
        s.sendmail(self.from_addr, self.to_addr, self.msg.as_string())
        s.quit()

        print('Sent Email from {} to {} address. '.format(self.from_addr, len(self.to_addr)))

    def email_on_error(self):

        def wrapper(func):

            def deco(*args, **kwargs):
                
                try:

                    func(*args,**kwargs)

                except:

                    type, value, tb = sys.exc_info()

                    if self.print_on_error:
                        print("Catched error during executing ", type, value, traceback)
                    
                    if self.send_email:
                        
                        self.make_email(content = traceback.format_exc())
                        
                        self.send_email()

                        if not self.verbose:
                            
                            print('Sent email')
                    else:
                        if not self.verbose:
                            print('Skipped emailing. send email set to False')
                        

                    

                
            return deco
        
        return wrapper

