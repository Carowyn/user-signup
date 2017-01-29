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
        pass

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user_label = "<form method='post'><label>Username: </label>"
        user_input = "<input type='text' name='user'/></form>"
        user = "<p>" + user_label + user_input + "</p>"

        password_label = "<form method='post'><label>Password: </label>"
        password_input = "<input type='password' name='password'/></form>"
        password = "<p>" + password_label + password_input + "</p>"

        verify_label = "<form method='post'><label>Verify Password: </label>"
        verify_input = "<input type='password' name'verify'/></form>"
        verify ="<p>" + verify_label + verify_input + "</p>"

        email_label = "<form method='post'><label>Email (optional): </label>"
        email_input = "<input type='text' name='email'/></form>"
        email = "<p>" + email_label + email_input + "</p>"

        submit = "<p><form><input type='submit' value='submit'/></form></p>"

        content = page_header + user + password + verify + email + submit + page_footer
        self.response.write(content)




class SignUp(webapp2.RequestHandler):
    """ Handles requests coming in to '/sign-up'"""
    def post(self):
        username = self.request.get("user_input")

        # USE THE FOLLOWING TO HELP BUILD
        if new_movie == "" or new_movie == " ":
            nomovie = "Please enter the name of the movie you want to watch.".format(new_movie)
            nomovie_escaped = cgi.escape(nomovie, quote=True)

            self.redirect("/?nomovie=" + nomovie_escaped)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
