#!/usr/bin/env python3

"""Library to work with IPv7 addresses."""

from re import split

class InvalidIPv7Address(Exception):
    """Raised when an invalid string is used to initiat."""
    pass

class IPv7Address(object):
    """Handles IPv7 Addresses."""
    def __init__(self, address_string):
        self.supernets = []
        self.hypernets = []
        try:
            parts = split(r'[\[\]]', address_string)
        except:
            raise InvalidIPv7Address
        for i, part in enumerate(parts):
            if i % 2 == 0:
                self.supernets.append(part)
            else:
                self.hypernets.append(part)

    def __repr__(self):
        return "IPv4Address('{}')".format(self._format_address())

    def __str__(self):
        return "{}".format(self._format_address())

    def _format_address(self):
        combined = zip(self.supernets, self.hypernets)
        address_string = ""
        for pair in combined:
            address_string += "{}[{}]".format(*pair)
        address_string += self.supernets[-1]
        return address_string

    @classmethod
    def _reverse(cls, string):
        return string[1] + string[0] + string[1]

    @classmethod
    def _hasabba(cls, string):
        """Checks for Autonomous Bridge Bypass Annotation."""
        for i, _ in enumerate(string):
            if (i < len(string) - 3 and
                    string[i] != string[i + 1] and
                    string[i + 1] == string[i + 2] and
                    string[i + 3] == string[i]):
                return True
        return False

    @classmethod
    def _getaba(cls, string):
        """Checks for Area-Broadcast Accessor."""
        for i, _ in enumerate(string):
            if (i < len(string) - 2 and
                    string[i] != string[i + 1] and
                    string[i + 2] == string[i]):
                yield string[i:i+3]

    def supports_tls(self):
        """Returns True if ABBA in address, but not in hypernet."""
        return (any([self._hasabba(addr) for addr in self.supernets]) and
                not any([self._hasabba(net) for net in self.hypernets]))

    def supports_ssl(self):
        """Returns True if ABA in supernet, and BAB in hypernet."""
        for part in self.supernets:
            for aba in self._getaba(part):
                bab = self._reverse(aba)
                if bab in "".join(self.hypernets):
                    return True
        return False
