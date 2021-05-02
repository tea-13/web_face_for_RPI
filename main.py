from http.server import BaseHTTPRequestHandler, HTTPServer
from picamera import PiCamera
from time import sleep

html = "<!doctype html><html lang=\"ru\"><head><title>Document</title><meta http-equiv=\"refresh\" content=\"0.5\"></head><body><img src=\"/home/pi/Desktop/image.jpg\"></body></html>"

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

def web_img(camera):
    camera.start_preview()
    sleep(1)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()

    pass
if __name__ == '__main__':
    camera = PiCamera()

    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)
