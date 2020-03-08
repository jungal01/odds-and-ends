"""
Author: Allen Junge

This script turns valid markdown into html. It is based on this PyPi project:
https://github.com/AumitLeon/markdown_html_converter. This file is licensed
under the MIT license.

The major changes in this file compared to the forked project is that the
typical command line utility stuff has been stripped, making it simpler and
better suited for my needs.
"""


import re
import mistune
from bs4 import BeautifulSoup as bs


def main():
    file = input("Name of Markdown file: ")
    while ('.md' not in file):
        print("that is not a recognized Markdown file.")
        file = input("Name of Markdown file: ")

    fileName = file.split('.')[0]
    html_doc = open(fileName+".html", 'w')

    generated_html = ("<!DOCTYPE html>" +
                      "<!--Converted via md-to-html-->" +
                      "<html><head></head><body>")

    with open(file) as f:
        content = f.readlines()
        for line in content:
            generated_html += mistune.markdown(line)

    generated_html += "</body></html>"

    # make BeautifulSoup
    soup = bs(generated_html, "html.parser")
    # prettify the html
    prettyHTML = soup.prettify()
    # write to the html doc
    html_doc.write(prettyHTML)


if __name__ == "__main__":
    main()
