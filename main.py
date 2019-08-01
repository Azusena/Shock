from google.appengine.ext import ndb
import jinja2
import os
import webapp2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('index.html')
        self.response.out.write(template.render())

class Vision(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('index.html')
        self.response.out.write(template.render())
app = webapp2.WSGIApplication([
  ('/', Home),
  ('/vision', Vision),
], debug=True)
