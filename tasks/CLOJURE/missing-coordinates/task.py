from languages.clojure import ClojureTask
import os

# Description
# Write a function 'coordinates' that calculates coordinates of vertices given their neighbours relations.


def test_methods():
    dirname = os.path.dirname(os.path.abspath(__file__))
    test = open(os.path.join(dirname, 'test.clj'), 'r')
    return test.read()

class MissingCoordinatesTask(ClojureTask):
    precode = ["(ns user)"]
    postcode = [test_methods()]


task = MissingCoordinatesTask()
