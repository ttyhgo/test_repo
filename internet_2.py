import urllib2
import gmaillib
import time
import socket
import os
import smtplib

#change email to your email
fromaddr = 'ttyhgo@gmail.com'
toaddr = 'ttyhgo@kookmin.ac.kr'
user = 'ttyhgo@gmail.com' 
pwd = 'push the password'


while True:
	os.system('ifconfig wlan0 > ip.txt')
	fp = open('ip.txt','r')
	data = fp.read().split()
	if 'inet' in data:
		num = data.index('inet')
		ip = data[num+1]
		break

server= smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(user,pwd)

msg = '\r\n'.join([
	'From: ttyhgo@gmail.com',
	'To: ttyhgo@kookmin.ac.kr',
	'Subject :' +ip,
	'',
	ip
	])


server.sendmail(fromaddr,toaddr,msg)
server.quit()
		

