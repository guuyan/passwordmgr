import imaplib
import email

server = imaplib.IMAP4('imap.sina.com')
print dir(server)
server.login("guuyan@sina.com",'guyandelove')
server.select(mailbox='INBOX', readonly=True)
resp, items = server.search(None, "Unseen")
number = 1
for i in items[0].split():
    resp, mailData = server.fetch(i, "(RFC822)")
    mailText = mailData[0][1]
    msg = email.message_from_string(mailText)
    print msg
