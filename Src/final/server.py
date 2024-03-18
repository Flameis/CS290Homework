from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import webbrowser

# Sample username and password (replace with your actual credentials)
USERNAME = 'user'
PASSWORD = 'password'

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        if parsed_path.path == '/login':
            # Check if username and password are provided as query parameters
            if 'username' in query_params and 'password' in query_params:
                username = query_params['username'][0]
                password = query_params['password'][0]
                
                # Verify username and password
                if username == USERNAME and password == PASSWORD:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'Login successful')
                else:
                    self.send_response(401)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'Invalid username or password')
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'Missing username or password')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Page not found')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    if __name__ == '__main__':
        webbrowser.open('http://localhost:8080/documentation.html')
        run()
