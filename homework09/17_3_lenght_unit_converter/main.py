#!/usr/bin/env python
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")

    def post(self):
        first_num = float((self.request.get("zahl")).replace(",", "."))
        sel_unit = self.request.get("einheit")

        second_num = None
        second_unit = None

        if sel_unit == "Kilometer":
            second_num = round(first_num * 1.60934, 2)
            second_unit = "Meilen"
        elif sel_unit == "Meilen":
            second_num = round(first_num * 0.621371, 2)
            second_unit = "Kilometer"

        params = {"first_num": first_num, "first_unit": sel_unit, "second_num": second_num,
                  "second_unit": second_unit}

        return self.render_template("main.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
