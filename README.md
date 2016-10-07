
# Unofficial Python Client for Google's Public DNS-over-HTTPs
Simple Python client for Google's Public [DNS-over-HTTPS](https://developers.google.com/speed/public-dns/docs/dns-over-https) service


[![Build Status](https://travis-ci.org/wglodek/dns-over-https.svg?branch=master)](https://travis-ci.org/wglodek/dns-over-https)
[![Code Climate](https://codeclimate.com/github/wglodek/dns-over-https/badges/gpa.svg)](https://codeclimate.com/github/wglodek/dns-over-https)
[![Test Coverage](https://codeclimate.com/github/wglodek/dns-over-https/badges/coverage.svg)](https://codeclimate.com/github/wglodek/dns-over-https/coverage)


## Quickstart

```python
>>> from dns_over_https import SecureDNS
>>> r = SecureDNS()
>>> r.gethostbyname('www.breakpoint-labs.com')
u'37.60.235.49'
>>> r = SecureDNS(query_type='AAAA')
>>> r.gethostbyname('www.google.com')
u'2607:f8b0:400d:c02::6a'
>>> r.resolve('www.mit.edu')
[u'2001:590:100b:182::255e', u'2001:590:100b:18b::255e']
>>>
```

## Documentation
Coming soon.

## License

MIT
