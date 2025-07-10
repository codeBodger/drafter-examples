#!/bin/python

# import sys
# sys.path.insert(0, "/home/rowan/Desktop/CISC/CS1/drafter-pyscript/")

from drafter import route, Page, Button, start_server, __version__, deploy_site, get_main_server, Table, add_files
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

add_files(
    "./drafter/__init__.py",
    "./drafter/configuration.py",
    "./drafter/debug.py",
    "./drafter/files.py",
    "./drafter/history.py",
    "./drafter/page.py",
    "./drafter/raw_files.py",
    "./drafter/server.py",
    "./drafter/styling.py",
    "./drafter/urls.py",
    "./drafter/components.py",
    "./drafter/constants.py",
    "./drafter/deploy.py",
    "./drafter/hacks.py",
    "./drafter/image_support.py",
    "./drafter/py.typed",
    "./drafter/routes.py",
    "./drafter/setup.py",
    "./drafter/testing.py"
)

start_server(State(0))
