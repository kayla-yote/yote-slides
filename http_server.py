#! /usr/bin/env python3

# Invoke http.server to host a basic webserver on localhost /without/ caching.
# Files served by http.server are usually cached by browsers, which makes testing and debugging
# buggy.

import http.server
import os
import socket

from functools import partial


SHOW_URLS = True


class NoCacheRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', default='localhost', metavar='ADDRESS',
                        help='Specify alternate bind address (or `all`)'
                             '[default: localhost]')
    parser.add_argument('--directory', default=os.getcwd(),
                        help='Specify alternative directory '
                        '[default:current directory]')
    parser.add_argument('--public', action='store_true',
                        help='Serve to your whole network [default: false]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()

    # -

    if args.public:
        args.bind = 'all'

    if args.bind == 'all':
        args.bind = ''

    # -

    handler_class = partial(NoCacheRequestHandler, directory=args.directory)

    server = http.server.ThreadingHTTPServer((args.bind, args.port), handler_class)
    print('Serving ThreadingHTTPServer for', args)

    if args.bind == 'localhost':
        hostlist = [(args.bind,args.port,'  (valid on this computer only)')]
    else:
        fqdn = socket.getfqdn(args.bind)
        #print('fqdn', fqdn)
        for (_,_,_,_,(addr,port,*_)) in socket.getaddrinfo(fqdn, args.port):
            #print('addr', addr)
            (hostname, aliaslist, ipaddrlist) = socket.gethostbyaddr(addr)
            hostlist = [hostname, *aliaslist, *ipaddrlist]
            hostlist = [(x,args.port,'') for x in hostlist]

    if SHOW_URLS:
        for (host,port,note) in hostlist:
            if port == 80:
                port = ''
            else:
                port = f':{port}'

            host2 = host.removesuffix('.localdomain')
            if host2 != host:
                print(f'   http://{host2}{port}/{note}')

            print(f'   http://{host}{port}/{note}')

    print('')
    server.serve_forever()
