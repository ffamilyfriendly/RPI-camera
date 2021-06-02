from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver

handler = SimpleHTTPRequestHandler

def runServer(port):
    print("running server on {}".format(str(port)))
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("server started at localhost:{}".format(port))
        httpd.serve_forever()
runServer(3000);