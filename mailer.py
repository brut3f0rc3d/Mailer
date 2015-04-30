#	Python Mailer Script
#	Script by : Palash Chatterjee

import sys
import smtplib
from urllib import urlencode

def customLogin(userName, password):
	session = smtplib.SMTP('smtp.gmail.com', 587);
	session.ehlo()
	session.starttls()
	try:
		session.login(userName, password)
	except:
		print "Login failed. Authentication failure"
		sys.exit()
	print "Logged in successfully"
	return session

def customComposeEmail(userName, mailToEmail):
	mailFrom = userName
	mailTo = mailToEmail.strip()
	subject = raw_input("Enter subject of email : ")
	headers = "\r\n".join(["from: "+mailFrom, "subject: "+subject, "to: "+mailTo,"mime-version: 1.0", "content-type: text/html"])
	body = raw_input("Enter body of email (in HTML format) : ")
	content = headers+"\r\n\r\n"+body
	return content

def customSendMail(userName, session, mailToEmail, content):
	try:
		session.sendmail(userName, mailToEmail, content)
		print "Email to "+mailToEmail+"sent."
	except:
		#print "There was some error in sending the email. Please try after some time"
		print "Email not sent to "+mailToEmail


def main():
	userName = raw_input("Enter your username : ")
	password = raw_input("Enter your password : ")
	session = customLogin(userName, password)
	fileName = sys.argv[1]
	with open(fileName, 'r') as f:
		lines = f.readlines()
		for line in lines:
			content = customComposeEmail(userName, line)
			customSendMail(userName, session, line, content)


if __name__ == '__main__':
	main()
