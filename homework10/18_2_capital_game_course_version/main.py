#!/usr/bin/env python
import os
import jinja2
import webapp2
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    capitals = {
        "Austria": "Vienna",
        "Bulgaria": "Sofia",
        "Japan": "Tokyo",
        "Italia": "Rome"
    }

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


class QuizHandler(BaseHandler):
    def get(self):
        country = random.choice(self.capitals.keys())
        return self.render_template("quiz.html", params={"country": country})


class AnswerHandler(BaseHandler):
    def post(self):
        answer = self.request.get("answer")
        country = self.request.get("country")

        if answer == self.capitals[country]:
            result = "right"
        else:
            result = "wrong"

        return self.render_template("result.html", params={"result": result})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/quiz', QuizHandler),
    webapp2.Route('/answer', AnswerHandler)
], debug=True)
