import http.server
import socketserver
import os

# Set the port number
PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):  
        rootdir = os.path.dirname(os.path.abspath(__file__)) #file location
        print(rootdir)
        try:  
            print(self.path)
            # separate the path from the query string
            my_path = self.path.split('?')[0]
            if my_path.endswith('.html'):  
                # Display the HTML file
                f = open(rootdir + my_path)
                # Send the html message
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(f.read().encode())
                f.close()
                return  
            if my_path.endswith('.css'):
                # Display the CSS file
                f = open(rootdir + my_path)
                # Send the css message
                self.send_response(200)
                self.send_header('Content-type','text/css')
                self.end_headers()
                self.wfile.write(f.read().encode())
                f.close()
                return
        except IOError:  
          self.send_error(404, 'file not found')

    def do_POST(self):
        # Take the path and split it from the query string
        my_path = self.path.split('?')[0]

        # Password validation
        if my_path == "/login.html":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            print (post_data)
            # Split the data to get the password and the page to redirect to
            password = post_data.decode('utf-8').split('&')[0]
            password = password.split('=')[1]

            page = post_data.decode('utf-8').split('&')[1]
            page = page.split('=')[1] + ".html"

            if password == "password":
                # Redirect to the given page
                self.send_response(301)
                self.send_header('Location', page)
                # Set local cookie to logged in for the next 5 minutes
                self.send_header('Set-Cookie', 'loggedIn=true; Max-Age=300')
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                # Redirect back to the login page after 5 seconds
                self.send_header('Refresh', '5; url=/')
                self.end_headers()
                self.wfile.write("Password is incorrect".encode())

if __name__ == '__main__':   
    Handler = MyHttpRequestHandler

    # Set up the server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        # Start the server
        httpd.serve_forever()