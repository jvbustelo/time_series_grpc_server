# __main__.py
# Run this file to start running the server
from server_app.app import Server

if __name__ == '__main__':
    print('Setting up server.')
    Server.run()
