from google.appengine.ext import ndb
import jinja2
import webapp2

the_jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)


class RegisterHandler(webapp2.RequestHandler):
   def get(self):
       donation_template = the_jinja_env.get_template('htc.html')
       self.response.out.write(donation_template.render())
   def post(self):
       template1 = the_jinja_env.get_template('donation.html')
       Name = self.request.get('name')
       Email = self.request.get('email')
       Phone = self.request.get('phone')
       Item description = self.request.get('item description')
       User = NewUser(Name=Name, Email=Email, Phone=Phone, Item description=Item description)
       User.put()
       self.response.out.write(donation_template.render())



app = webapp2.WSGIApplication([
 ('/', HandleHome),
], debug=True)
