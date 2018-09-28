#!/usr/bin/env python
# coding=utf-8
import os
import jinja2
import webapp2
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


class Hauptstadt:
    def __init__(self, stadt, land, img):
        self.stadt = stadt
        self.land = land
        self.img = img

def capital_list():
    w = Hauptstadt(stadt="Wien", land="Oesterreich", img="/assets/img/city1.jpg") #Ö can't be encoded
    s = Hauptstadt(stadt="Sofia", land="Bulgarien", img="/assets/img/city2.jpg")
    tk = Hauptstadt(stadt="Tokyo", land="Japan", img="/assets/img/city3.jpg")
    r = Hauptstadt(stadt="Rom", land="Italien", img="/assets/img/city4.jpg")
    am = Hauptstadt(stadt="Amsterdam", land=" den Niederlanden", img="/assets/img/city5.jpg")

    return [w, s, tk, r, am]


class MainHandler(BaseHandler):
    def get(self):
        capital = capital_list()[random.randint(0, 4)]

        return self.render_template("main.html", params={"capital": capital})


class ResultHandler(BaseHandler):
    def post(self):
        answer = self.request.get("answer")
        country = self.request.get("country")

        capitals = capital_list()
        for item in capitals:
            if item.land == country:
                if item.stadt.lower() == answer.lower():
                    result = True
                else:
                    result = False

                return self.render_template("answer.html", params={"result": result, "item": item})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/answer', ResultHandler),
], debug=True)