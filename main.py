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

class main_handler(webapp2.RequestHandler):
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

        content = build_head() + user + password + verify + email + submit + build_footer
