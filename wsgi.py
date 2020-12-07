import os

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    file = open("C:\\xampp\\htdocs\\hackathonOpenBank\\index.html", "r")
    content = file.read()
    return [content.encode('ascii')]
    