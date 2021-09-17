"""A basic FTP server which uses a DummyAuthorizer for managing 'virtual
users', setting a limit for incoming connections.
"""

import os, sys, inspect, logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def main():
    port = 21
    user = ''
    password = ''
    l = sys.argv

    if (len(l) > 1 and l[1]):
        user = l[1]

    if (len(l) > 2 and l[2]):
        password = l[2]

    if (len(l) > 3 and l[3]):
        port = int(l[3])


    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, os.getcwd(), perm='elradfmwM')
    #authorizer.add_anonymous("/home/nobody")

    handler = FTPHandler
    handler.authorizer = authorizer

    logging.basicConfig(level=logging.DEBUG)
    print("port",port)
    server = FTPServer(("127.0.0.1", port), handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
