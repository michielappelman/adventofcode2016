#!/usr/bin/env python

import unittest
import ipv7

class TestIPv7Addresses(unittest.TestCase):
    tls_support = ('abba[mnop]qrsti',
                   'aaaa[qwer]tyauua[qwer]tyui',
                   'ioxxoj[asdfgh]zxcvbn')
    tls_no_support = ('aaa[op]kslei',
                      'abcd[bddb]xyyx',
                      'jekl[iua]oepl')
    ssl_support = ('zazbz[bzb]cdb',
                   'aaa[kek]eke',
                   'aba[bab]xyz')
    ssl_no_support = ('xyx[xyx]xyx')

    def test_valid_addresses(self):
        for address in self.tls_support:
            host = ipv7.IPv7Address(address)
            self.assertEqual(address, str(host))

    def test_tls_support(self):
        for address in self.tls_support:
            self.assertTrue(ipv7.IPv7Address(address).supports_tls())

    def test_tls_no_support(self):
        for address in self.tls_no_support:
            self.assertFalse(ipv7.IPv7Address(address).supports_tls())

    def test_ssl_support(self):
        for address in self.ssl_support:
            self.assertTrue(ipv7.IPv7Address(address).supports_ssl())

    def test_ssl_no_support(self):
        for address in self.ssl_no_support:
            self.assertFalse(ipv7.IPv7Address(address).supports_ssl())

if __name__ == "__main__":
    unittest.main()
