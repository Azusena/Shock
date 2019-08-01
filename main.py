import jinja2
import os
import webapp2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('index.html')
        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([
  ('/', EnterInfoHandler),
], debug=True)
