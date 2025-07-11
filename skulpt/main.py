#!/bin/python

# import sys
# sys.path.insert(0, "/home/rowan/Desktop/CISC/CS1/drafter-skulpt/")

from drafter import route, Page, Button, start_server, __version__, deploy_site, get_main_server, Table
from dataclasses import dataclass

from random import randint

@dataclass
class State:
        counter: int

@route
def index(state: State) -> Page:
        return Page(state, [Table([
                ["Welcome to Drafter!",
                "Click the button below."],
                [Button("Increase the count", increment_counter, (randint(1,100),))],
        ])])

@route
def increment_counter(state: State, offset: int) -> Page:
        raise ValueError("aa")
        state.counter += offset
        return Page(state, [
                "You've clicked the button " + str(state.counter) + " times",
                Button("Click again", increment_counter, (randint(1,100),))
        ])

print(__version__)

# print(get_main_server().configuration.debug)

deploy_site()

get_main_server().configuration.cdn_skulpt = "http://localhost:8080/skulpt.js"
get_main_server().configuration.cdn_skulpt_std = "http://localhost:8080/skulpt-stdlib.js"
get_main_server().configuration.cdn_skulpt_drafter = "http://localhost:8080/skulpt-drafter.js"
get_main_server().configuration.cdn_drafter_setup = "http://localhost:8080/drafter-setup.js"

# get_main_server().configuration.cdn_skulpt = "https://codebodger.github.io/drafter/cdn/skulpt/skulpt.js"
# get_main_server().configuration.cdn_skulpt_std = "https://codebodger.github.io/drafter/cdn/skulpt/skulpt-stdlib.js"
# get_main_server().configuration.cdn_skulpt_drafter = "https://codebodger.github.io/drafter/cdn/skulpt/skulpt-drafter.js"
# get_main_server().configuration.cdn_drafter_setup = "https://codebodger.github.io/drafter/cdn/skulpt/drafter-setup.js"

# with open("out.js", "w") as f:
        # # f.write(bundle_py_into_raw_js("/home/rowan/Desktop/CISC/CS1/example_d"))
        # f.write(bundle_py_into_raw_js("."))

start_server(State(0))

# if int(__version__.split(".")[0]) < 2:
        # start_server(State(0))
#
# # from _HTMLPage import *
# # from server import start_server
# #
# # set_website_title("Drafter 2 Example / Playground")
# # add_website_css("div", "width: fit-content; margin: auto;")
# # add_website_content("<div>HELLO!!</div>")
# #
# # print(MAIN_HTML_PAGE)
# #
# # start_server()
#
# else:
        # # from flask import Flask
        # # app = Flask("/")
        # # @app.route("/")
        # # def index():
                # # with open("index.html") as f:
                        # # return f.read()
        # # app.run(host="localhost", port=8000)
#
        # import http.server as sv
        # sv.test(sv.SimpleHTTPRequestHandler, sv.ThreadingHTTPServer)
