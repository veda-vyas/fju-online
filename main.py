#!/usr/bin/env python
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers

import os
import urllib
import jinja2
import webapp2
import datetime
import json
import re
import traceback
import logging
import random
import socket
import string

from google.appengine.api import app_identity
from google.appengine.api import mail


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        # populateDates()
        template_values = {"authorized":True}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

def send_approved_mail(sender_address,name,email,phone,comment):
    message = mail.EmailMessage(
        sender=sender_address,
        subject="FJU Contact Us Form")

    message.to = "FJU Team <pg@fju.us>"
    message.body = """Hello Praveen,
A new information request is awaiting your response. The details are:

Name: """+name+"""
Email: """+email+"""
Phone Number: """+phone+"""
Requested For: """+comment+"""

Regards,
FJU Team
"""
    message.send()

    message.to = "FJU Team <vy@fju.us>"
    message.body = """Hello Veda,
A new information request is awaiting your response. The details are:

Name: """+name+"""
Email: """+email+"""
Phone Number: """+phone+"""
Requested For: """+comment+"""

Regards,
FJU Team
"""
    message.send()


class SendMessageHandler(webapp2.RequestHandler):
    def post(self):
    	name = self.request.get('name')
    	email = self.request.get('email').replace('%40','@')
    	phone = self.request.get('phone')
    	comment = self.request.get('comment')
        send_approved_mail('{}@appspot.gserviceaccount.com'.format(
            app_identity.get_application_id()),name,email,phone,comment)
        self.response.content_type = 'text/plain'
        self.response.write('Sent an email message to '+name)

class Navbar(webapp2.RequestHandler):
    def get(self):
        template_values = {"authorized":True}
        template = JINJA_ENVIRONMENT.get_template('navbar_responsive.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    #('/send_message', SendMessageHandler),
    ('/navbar', Navbar)
], debug=True)
