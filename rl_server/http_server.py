import SimpleHTTPServer
import SocketServer
import sys
import os

PORT = 8000

def run(port=PORT, server_addr='0.0.0.0'):
    # Set the directory you want to serve
    root_directory = "../video_server/"
    os.chdir(root_directory)
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer((server_addr, port), Handler)
    print "HTTP server ip=" + server_addr + ", port=" + str(port)
    httpd.serve_forever()

def main():
    if len(sys.argv) == 2:
        server_addr = sys.argv[1]
        run(server_addr=server_addr)
    else:
        run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
