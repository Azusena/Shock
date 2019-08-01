import jinja2
import os
import webapp2


class HandleHome(webapp2.RequestHandler):
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render())
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
  ('/', HandleHome),
  ('/send', HandleSend),
  ('/_ah/channel/connected/', HandleConnect),
  ('/_ah/channel/disconnected/', HandleDisconnect),
], debug=True)
