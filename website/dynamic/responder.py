import cgi
import webapp2

class Emailer(webapp2.RequestHandler):
  def post(self):
    self.response.write('<html><body>')
    self.response.write('Name: ' + cgi.escape(self.request.get('name')))
    self.response.write('Email: ' + cgi.escape(self.request.get('email')))
    self.response.write('Phone: ' + cgi.escape(self.request.get('phone')))
    self.response.write('Location: ' + cgi.escape(self.request.get('location')))
    self.response.write('Event Details: ' + cgi.escape(self.request.get('details')))
    self.response.write('</body></html>')


application = webapp2.WSGIApplication([
  ('/form-response', Emailer),
], debug=True)