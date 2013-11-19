import cgi
import webapp2

from google.appengine.api import mail

class Emailer(webapp2.RequestHandler):
  def post(self):
	 form_name = cgi.escape(self.request.get('name'))
     form_email = cgi.escape(self.request.get('email'))
     form_phone = cgi.escape(self.request.get('phone'))
     form_location = cgi.escape(self.request.get('location'))
     form_details = cgi.escape(self.request.get('details'))
     
     sender_address = 'info@randcphotos.com'
     user_address = 'info@randcphotos.com'
     subject = 'New Photography Inquiry from %s' % form_name
     body = """
     Name: %s
     Email: %s
     Phone: %s
     Location: %s
     Event Details %s
     """ % (form_name, form_email, form_phone, form_location, form_details)
     mail.send_mail(sender_address, user_address, subject, body)
     self.redirect('contact.html?s=1')

application = webapp2.WSGIApplication([
  ('/form-response', Emailer),
], debug=True)