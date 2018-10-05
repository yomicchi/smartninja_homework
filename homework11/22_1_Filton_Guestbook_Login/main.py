#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Message
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None, address="/"):
        if not params:
            params = {}

        user = users.get_current_user()

        if user:
            logged_in = True
            logging_url = users.create_logout_url(address)

        else:
            logged_in = False
            logging_url = users.create_login_url(address)

        params.update({"logged_in": logged_in, "logging_url": logging_url, "user": user})

        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")


class GuestbookHandler(BaseHandler):
    def get(self):
        messages = Message.query(Message.deleted == False).fetch()

        params = {"messages": messages}

        return self.render_template("guestbook.html", params=params, address="/guestbook")

    def post(self):
        author = self.request.get("name")
        email = self.request.get("email")
        message = self.request.get("message")

        if not author:
            author = "Anonymous"

        msg_object = Message(author_name=author, email=email, message_text=message.replace("<script>", ""))
        msg_object.put()

        return self.redirect_to("guestbook-page")


class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}
        return self.render_template("message_edit.html", params=params, address="/message/<message_id:\d+>/edit")

    def post(self, message_id):
        new_text = self.request.get("edit_mess")
        new_name = self.request.get("edit_name")
        message = Message.get_by_id(int(message_id))
        message.message_text = new_text
        message.author_name = new_name
        message.put()
        return self.redirect_to("guestbook-page")


class DeleteHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))
        params = {"message": message}

        return self.render_template("message_delete.html", params=params, address="/message/<message_id:\d+>/delete")

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))
        message.deleted = True
        message.put()
        return self.redirect_to("guestbook-page")


class DeletedHandler(BaseHandler):
    def get(self):
        messages = Message.query(Message.deleted == True).fetch()

        params = {"messages": messages}

        return self.render_template("deleted_messages.html", params=params, address="/deleted")


class RestoreHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("message_restore.html", params=params, address="/message/<message_id:\d+>/restore")

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))

        message.deleted = False
        message.put()

        return self.redirect_to("guestbook-page")


class CompleteDeleteHandler(BaseHandler):
    def get(self, message_id):
        message = Message.get_by_id(int(message_id))

        params = {"message": message}

        return self.render_template("complete_delete.html", params=params, address="/message/<message_id:\d+>/complete-delete")

    def post(self, message_id):
        message = Message.get_by_id(int(message_id))

        message.key.delete()

        return self.redirect_to("deleted-messages")


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/guestbook', GuestbookHandler, name="guestbook-page"),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteHandler),
    webapp2.Route('/deleted', DeletedHandler, name="deleted-messages"),
    webapp2.Route('/message/<message_id:\d+>/restore', RestoreHandler, name="message-restore"),
    webapp2.Route('/message/<message_id:\d+>/complete-delete', CompleteDeleteHandler, name="message-complete-delete"),
], debug=True)