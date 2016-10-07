#!/usr/bin/env python

import random
import requests


__version__ = '0.0.1'


# Resource Record Types
A = 1
AAAA = 28


# DNS status codes
NOERROR = 0


UNRESERVED_CHARS = 'abcdefghijklmnopqrstuvwxyz' \
                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                   '0123456789-._~'


class InvalidHostName(Exception):
    pass


class SecureDNS(object):
    '''Resolve domains using Google's Public DNS-over-HTTPS API'''

    def __init__(
        self,
        query_type=1,
        cd=False,
        edns_client_subnet='0.0.0.0/0',
        random_padding=True,
    ):
        self.url = 'https://dns.google.com/resolve'
        self.params = {
            'type': query_type,
            'cd': cd,
            'edns_client_subnet': edns_client_subnet,
            'random_padding': random_padding,
        }

    def gethostbyname(self, hostname):
        '''mimic functionality of socket.gethostbyname'''
        answers = self.resolve(hostname)
        if answers is not None:
            return answers[0]
        return None

    def resolve(self, hostname):
        '''return ip address(es) of hostname'''
        hostname = self.prepare_hostname(hostname)
        self.params.update({'name': hostname})

        if self.params['random_padding']:
            padding = self.generate_padding()
            self.params.update({'random_padding': padding})

        r = requests.get(self.url, params=self.params)
        if r.status_code == 200:
            response = r.json()

            if response['Status'] == NOERROR:
                answers = []
                for answer in response['Answer']:
                    name, response_type, ttl, data = \
                        map(answer.get, ('name', 'type', 'ttl', 'data'))
                    if response_type in (A, AAAA):
                        answers.append(data)
                if answers == []:
                    return None
                return answers
        return None

    def prepare_hostname(self, hostname):
        '''verify the hostname is well-formed'''
        hostname = hostname.rstrip('.')  # strip trailing dot if present

        if not(1 <= len(hostname) <= 253):  # test length of hostname
            raise InvalidHostName

        for label in hostname.split('.'):  # test length of each label
            if not(1 <= len(label) <= 63):
                raise InvalidHostName
        try:
            return hostname.encode('ascii')
        except UnicodeEncodeError:
            raise InvalidHostName

    def generate_padding(self):
        '''generate a pad using unreserved chars'''
        pad_len = random.randint(10, 50)
        return ''.join(random.choice(UNRESERVED_CHARS) for _ in range(pad_len))
