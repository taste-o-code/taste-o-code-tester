from languages.clojure import ClojureTask
import os

# Description
# Write a function 'get-links' that extracts all links from parsed google search results.

test_code = """
(let [content (read)
      links (get-links content)]
  (doseq [link links]
    (println link)))
"""

task = ClojureTask()
task.postcode = [test_code]
