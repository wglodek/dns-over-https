import pytest
from dns_over_https import SecureDNS, InvalidHostName


@pytest.fixture(scope='module')
def resolver():
    return SecureDNS()


class TestSecureDNS(object):

    def test_prepare_hostname_valid_domain(self, resolver):
        assert resolver.prepare_hostname('www.google.com.') == \
            'www.google.com'.encode('ascii')

    def test_prepare_hostname_invalid_domain(self, resolver):
        with pytest.raises(InvalidHostName):
            resolver.prepare_hostname('www.foo..bar.com')

    def test_prepare_hostname_unicode_domain(self, resolver):
        with pytest.raises(InvalidHostName):
            resolver.prepare_hostname(u"\U0001F44E.com")

    def test_prepare_hostname_invalid_long_domain(self, resolver):
        with pytest.raises(InvalidHostName):
            resolver.prepare_hostname('A' * 254 + '.com')

    def test_generate_padding(self, resolver):
        padding = resolver.generate_padding()
        assert len(padding) >= 10
        assert len(padding) <= 50


@pytest.mark.integration
class TestSecureDNSIntegration(object):

    def test_resolve_with_valid_domain(self, resolver):
        assert resolver.resolve('www.breakpoint-labs.com') == ['37.60.235.49']

    def test_resolve_with_invalid_domain(self, resolver):
        assert resolver.resolve('www.does.not.exist.qaz') is None

    def test_resolve_with_AAAA_request_type(self):
        r = SecureDNS(query_type='AAAA')
        answers = r.resolve('dns.google.com')
        assert len(answers) == 1
        assert answers[0].startswith('2607:f8b0')

    def test_resolve_with_multiple_AAAA_records(self):
        r = SecureDNS(query_type='AAAA')
        answers = r.resolve('www.mit.edu')
        assert len(answers) == 2

    def test_resolve_with_no_AAAA_records(self):
        r = SecureDNS(query_type='AAAA')
        assert r.resolve('www.breakpoint-labs.com') is None

    def test_gethostbyname(self, resolver):
        assert resolver.gethostbyname('www.breakpoint-labs.com') == \
            '37.60.235.49'

    def test_gethostbyname_with_invalid_domain(self, resolver):
        assert resolver.gethostbyname('www.does.not.exist.qaz') is None
