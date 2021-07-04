# Send email through simple smtp

from email.mime.multipart import MIMEMultipart
import sys
import traceback

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr,parseaddr

from typing import List

class EmailError():

    def __init__(self, from_addr: str = None, to_addr : str or List = None, smtp_addr : str = None, 
                error_msg_title = 'Error', 
                error_msg_content = 'Error occurred',
                raise_on_error = False, print_on_error = False, send_email_on_error = True, 
                verbose = False ) -> None:
        """
        Email error message, tracebacks when error occurs
        Email sent through simple smtp withou any authentication process. 
        Suits most of internal smtp service

        Input
        ----- 
        from_addr: str represents email address
        to_addr: str represnets email address or list of address

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


    def make_email(self, error_msg = None):
        """
        Make email
        """
        msg = MIMEMultipart('mixed')

        msg['From'] = self._format_addr("From <{}>".format(self.from_addr))
        msg['To'] = self._format_addr("To <{}>".format(self.from_addr))
        msg['Subject'] = Header(self.error_msg_title, 'utf-8').encode()

        if error_msg is None:
            # replace default email 
            msg.attach(MIMEText(self.error_msg_content, 'plain', 'utf-8'))
        else:
            msg.attach(MIMEText(error_msg, 'plain', 'utf-8'))

        self.msg = msg

        return msg


    def send_email(self):
        
        assert self.smtp_addr is not None, "Please Privide SMTP Addr"
        
        s = smtplib.SMTP(self.smtp_addr)
        s.sendmail(self.from_addr, self.to_addr, self.msg.as_string())
        s.quit()

        print('Sent Email from {} to {} address. '.format(self.from_addr, len(self.to_addr)))

    def send_error_email(self,error_msg = None):
        """
        Make and send email
        """
        self.make_email(error_msg = error_msg)
        self.send_email()

    

    def email_on_error(self):

        def wrapper(func):

            def deco(*args, **kwargs):
                
                try:

                    func(*args,**kwargs)

                except:

                    type, value, traceback = sys.exc_info()

                    if self.print_on_error:
                        print("Catched Error During executing", type, value, traceback)
                    
                    if self.send_email_on_error:
                        

                        self.make_email()

                        self.send_email()

                        if not self.verbose:
                            
                            print('Sent email')
                    else:
                        if not self.verbose:
                            print('Skipped emailing. send email set to False')
                        

                    

                
            return deco
        
        return wrapper

