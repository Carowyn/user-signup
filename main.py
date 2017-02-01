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

def build_head():  # Change style type in head to css when doing finish work
    """Creates the html header for the page."""
    page_header = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
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
    return page_header

def build_footer():
    """Creates the html footer for the page."""
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
    return page_footer

def valid_username(user_input):
    """Checks if the username input is valid."""
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(user_input)

def valid_password(password_input):
    """Checks if the password input is valid."""
    password_re = re.compile(r"^.{3,20}$")
    return password_re.match(password_input)

def valid_email(email_input):
    """Checks if ther is email input. If there is, checks if it is valid."""
    if email_input == "":
        pass
    else:
        email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return email_re.match(email_input)

def password_verified(password_input, verify_input):
    """Checks if the Password and Verify Password fields match."""
    if password_input == verify_input:
        pass
    else:
        return False

class MainHandler(webapp2.RequestHandler):
    def get(self):
        """First page that the user comes to. Handles the first GET request."""
        # sets up the Username field
        user_label = "<form action='sign-up' method='post'><label>Username: </label>"
        user_input = "<input type='text' name='user'>" + user_content + "</input>"
        user = "<p>" + user_label + user_input + "</p>"

        # sets up the password field
        password_label = "label>Password: </label>"
        password_input = "<input type='password' name='password'/>"
        password = "<p>" + password_label + password_input + "</p>"

        # sets up the verify password field
        verify_label = "<label>Verify Password: </label>"
        verify_input = "<input type='password' name='verify'/>"
        verify = "<p>" + verify_label + verify_input + "</p>"

        # sets up the optional email field
        email_label = "<label>Email (optional): </label>"
        email_input = "<input type='text' name='email'>" + email_content + "</input>"
        email = "<p>" + email_label + email_input + "</p>"

        # sets up the submit button
        submit = "<p><input type='submit' value='submit'/></form></p>"

        #ERRORS GO HERE
        error1 = self.request.get("no_username_error")
        error1_element = "<span class='error'>" + error1 + "</span>" if error1 else ""

        error2 = self.request.get("space_error")
        error2_element = "<span class='error'>" + error1 + "</span>" if error2 else ""

        error3 = self.request.get("invalid_user")
        error3_element = "<span class='error'>" + error3 + "</span>" if error3 else ""

        error4 = self.request.get("no_password_error")
        error4_element = "<span class='error'>" + error4 + "</span>" if error4 else ""

        error5 = self.request.get("invalid_password")
        error5_element = "<span class='error'>" + error5 + "</span>" if error5 else ""

        error6 = self.request.get("pass_not_verified")
        error6_element = "<span class='error'>" + error6 + "</span>" if error6 else ""

        error7 = self.request.get("space_in_email")
        error7_element = "<span class='error'>" + error7 + "</span>" if error7 else ""

        error8 = self.request.get("invalid_email")
        error8_element = "<span class='error'>" + error8 + "</span>" if error8 else ""

        content = build_head() + user + error1_element + error2_element + error3_element + password + error4_element + error5_element + verify + error6_element + email + error7_element + error8_element + submit + build_footer

class SignUp(webapp2.RequestHandler):
    """Handles requests coming into '/sign-up'."""
    def post(self):
        # set the validity values to False
        user_valid = False
        pass_valid = False
        email_valid = False

        # pull in username
        username = self.request.get("user_input")
        user_escape = cgi.escape(username, quote=True)
        # check username validity
        if user_escape == "":#error1
            no_username_error = "A username is required.".format(user_escape)
            self.redirect("/sign-up" + no_username_error)
        elif " " in user_escape:#error2
            space_error = "Username cannot contain spaces.".format(user_escape)
            self.redirect("/sign-up" + space_error)
        elif not valid_username(user_escape):#error3
            invalid_user = "Username must contain between 3 and 20 characters (Upper, lower, _, -).".format(user_escape)
            self.redirect("/sign-up" + invalid_user)
        else:#valid
            user_valid = True

        # pull in password
        password = self.request.get("password_input")
        # check password validity
        if password == "":#error4
            no_password_error = "A password is required.".format(password)
            self.redirect("/sign-up)
        elif not valid_password(password):#error5
            invalid_password = "Password contains invalid characters. Please try again."
            self.redirect("/sign-up")
        elif not password_verified(password):#error6
            pass_not_verified = "The password fields do not match."
            self.redirect("/sign-up")
        else:#valid
            pass_valid = True

        # pull in email
        email = self.request.get("email_input")
        # check email validity
        if " " in email:#error7
            space_in_email = "Email cannot contain spaces."
            self.redirect("/sign-up")
        elif not valid_email(email):#error8
            invalid_email = "email is not valid, it must be in this form:  abc@something.com...Please try again."
            self.redirect("/sign-up")
        else:#valid
            email_valid = True

        if user_valid and pass_valid and email_valid:#if all valid
            self.redirect("/welcome")

class Welcome(webapp2.RequestHandler):
    """Handles requests coming into '/welcome'."""
    def post(self):
        user = self.request.get(user_input)
        email = self.request.get(email_input)
        welcome = "Hello %s, thank you for signing up! We've added your email address as %s. Thank you!" % (user, email)
        welcome_element = "<p class='welcome'>" + welcome + "</p>"
        content = build_head() + welcome_element + build_footer()

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/sign-up', SignUp),
    ('/welcome', Welcome)
    ])
