#!/usr/bin/env python
import os
import jinja2
import webapp2
import random
import random

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


class LotteryHandler(BaseHandler):
    def get(self):
        zahlen = lottozahl_gen(6)

        params = {"zahlen": zahlen}

        return self.render_template("lottery.html", params=params)


def lottozahl_gen(anzahl):
        zahlenliste = []

        while True:
            if len(zahlenliste) == anzahl:
                break

            zahl = random.randint(1, 46)

            if zahl not in zahlenliste:
                zahlenliste.append(zahl)

        return zahlenliste


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/lottery', LotteryHandler),
], debug=True)
