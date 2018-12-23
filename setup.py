# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 03:59:45 2018

@author: TRAORE Mohamed
"""
#!/usr/bin/python
 
import smtplib
import os
import sys
from email.MIMEText import MIMEText
from apollomanfirst import armstrong
from pandabot import *
from robotchercherDeMail import lazer, predator


def sendTextMail(text):
	fromaddr = "Mohamed TRAORE <root@traore.io>"
    listeMail = "/apollosoldier/home/cvSender/mail/list.json"
	liste_destinataires=[lazer(listMail).getName()'@'lazer(listMail).getdomain()'.com']
    	mail = MIMEText(text)
    	mail['From'] = fromaddr
    	mail['Subject'] = "BUILDAUTO"
    	smtp = smtplib.SMTP()
    	smtp.connect()
    	for d in liste_destinataires:
    		smtp.sendmail(fromaddr,d,mail.as_string())
    	smtp.close()
 
 
def main():
	logfile = sys.argv[1]
	f=open(logfile, "r")
	corps = """\
Bonjour,
        
J'ai vue votre annonce concernant le poste """,inetValue,""" sur Indeed et je tiens à vous dire que ce poste m'interresse enormement. Vous trouverez en pièce jointe une copie de mon CV et de la lettre de motivation.        
"""
	for i in f:
		corps+=i
 
	corps+="""\
        
 PS : Merci de bien vouloir me repondre au mtraore01@icloud.com
"""
 
	f.close()
	sendTextMail(corps)
 
 
if __name__ == '__main__':
	main()