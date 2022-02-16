from app import app
from wsgiref.simple_server import make_server


if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        httpd.serve_forever()
