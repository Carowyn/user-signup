#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import re

# html boilerplate for the top of this page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link type="text/css" rel="stylesheet" href="normalize.css">
    <link type="text/css" rel="stylesheet" href="styles.css">
    <title>User Sign-Up</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">User Sign-Up</a>
    </h1>
"""

# html boilerplate for the bottom of this page
page_footer = """
</body>
<footer>
    <address>
        <p><br>Contents written by: <b>Brittani Luce</b></p>
        <p>Written for: LaunchCode 101 -- User Sign-Up
        <p>Thank you for visiting!</p>
    </address>
        <p>&#169;Brittani Luce, 2017
        <br><br></p>
</footer>
</html>
"""

def valid_username(user_input):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(user_input)

def valid_password(password_input):
    password_re = re.compile(r"^.{3,20}$")
    return password_re.match(password_input)

def valid_email(email_input):
    email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
    return email_re.match(email_input)

def password_verified(password_input, verify_input):
    if password_input == verify_input:
        pass
    else:
        return False

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_label = "<form action='/sign-up' method='post'><label>Username: </label>"
        user_input = "<input type='text' name='user'/>"
        user = "<p>" + user_label + user_input + "</p>"

        password_label = "<label>Password: </label>"
        password_input = "<input type='password' name='password'/>"
        password = "<p>" + password_label + password_input + "</p>"

        verify_label = "<label>Verify Password: </label>"
        verify_input = "<input type='password' name'verify'/>"
        verify ="<p>" + verify_label + verify_input + "</p>"

        email_label = "<label>Email (optional): </label>"
        email_input = "<input type='text' name='email'/>"
        email = "<p>" + email_label + email_input + "</p>"

        submit = "<p><input type='submit' value='submit'/></form></p>"

        space_error = self.request.get("space_error")
        space_error_element = "<span class='error'> " + space_error + "</span>"

        invalid_user = self.request.get("invalid_user")
        invalid_user_element = "<span class='error'> " + invalid_user + "</span>"

        invalid_password = self.request.get("invalid_password")
        invalid_password_element = "<span class='error'> " + invalid_password + "</span>"

        pass_not_verified = self.request.get("pass_not_verified")
        pass_not_verified_element = "<span class'error'> " + pass_not_verified + "</span>"

        invalid_email = self.request.get("invalid_email")
        invalid_email_element = "<span class='error'> " + invalid_email + "</span>"

        content = page_header + user + space_error_element + invalid_user_element + password + invalid_password_element + verify + pass_not_verified_element+ email + invalid_email_element + submit + page_footer
        self.response.write(content)


class SignUp(webapp2.RequestHandler):
    """ Handles requests coming in to '/sign-up'"""
    def post(self):
        user_valid = False
        username = self.request.get("user_input")
        if " " in username:
            space_error = "Username cannot contain spaces.".format(username)
            space_error_escaped = cgi.escape(space_error, quote=True)
            self.redirect("/?space_error=" + space_error_escaped)
        elif not valid_username(username):
            invalid_user = "Username must contain between 3 and 20 characters. It can contain lower and uppercase, numbers _ and -, no period.".format(username)
            self.redirect("/?invalid_user=" + invalid_user)
        else:
            user_valid = True

        pass_valid = False
        password = self.request.get("password_input")
        if not valid_password(password):
            invalid_password = "Password contains invalid characters. Please try again."
            self.redirect("/?invalid_password=" + invalid_password)
        elif not password_verified(password):
            pass_not_verified = "The password fields do not match."
            self. redirect("/?pass_not_verified=" + pass_not_verified)
        else:
            pass_valid = True
            
        email_valid = False
        email = self.request.get("email_input")
        if not valid_email(email):
            invalid_email = "Email is not valid, it must be in this form:  abc@something.com...Please try again."
            self.redirect("/?invalid_email=" + invalid_email)
        else:
            email_valid = True
            #return email_valid

        if user_valid and pass_valid and email_valid:
            self.redirect("/welcome")

class Welcome(webapp2.RequestHandler):
    def post(self):
        user = self.request.get(user_input)
        email = self.request.get(email_input)
        welcome = "Hello %s, thank you for signing up! We've added your email address as %s. Thank you!" % (user, email)
        welcome_element = "<p class='wecome'>" + welcome + "</p>"
        content = page_header + welcome_element + page_footer




app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign-up', SignUp),
    ('/welcome', Welcome)
], debug=True)
