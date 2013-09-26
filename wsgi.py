#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('/srv/www/lukemallon.com/public_html')


def application(environ, start_response):
    status = '200 OK'
    output = 'Luke Mallon!'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(output)))
    ]
    start_response(status, response_headers)

    return [output]
