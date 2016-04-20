from __future__ import absolute_import
from wns import WNSClient
import unittest


class WNSTestCase(unittest.TestCase):
    def __init__(self):
        self.wnsclientid = "some id"
        self.wnsclientsecret = "some secret"

    def test_wns_badge(self):
        """Send message on wns for windows 8+"""
        wnsclientid = self.wnsclientid
        wnsclientsecret = self.wnsclientsecret
        if None in (wnsclientid, wnsclientsecret):
            raise AttributeError("WNS cclient id and secrted required.")
        cred_info = {'wnsclientid':  wnsclientid,
                     'wnsclientsecret': wnsclientsecret}

        token = "some token"
        message = {"type": 'badge', "badge": {"value":"12"}}
        if None in (token, message):
            raise AttributeError("Invalid input parameters for WNS.")

        wns = WNSClient(cred_info)
        response = wns.process(token=token, message=message)
        assert response.status_code == 200

    def test_wns_toast(self):
        """Send message on wns for windows 8+"""
        wnsclientid = self.wnsclientid
        wnsclientsecret = self.wnsclientsecret
        if None in (wnsclientid, wnsclientsecret):
            raise AttributeError("WNS cclient id and secrted required.")
        cred_info = {'wnsclientid':  wnsclientid,
                     'wnsclientsecret': wnsclientsecret}

        token = "some token"
        message = {"type": "toast", "text": ["test toast or tile"]}
        if None in (token, message):
            raise AttributeError("Invalid input parameters for WNS.")

        wns = WNSClient(cred_info)
        response = wns.process(token=token, message=message)
        assert response.status_code == 200

    def test_wns_tile(self):
        """Send message on wns for windows 8+"""
        wnsclientid = self.wnsclientid
        wnsclientsecret = self.wnsclientsecret
        if None in (wnsclientid, wnsclientsecret):
            raise AttributeError("WNS cclient id and secrted required.")
        cred_info = {'wnsclientid':  wnsclientid,
                     'wnsclientsecret': wnsclientsecret}

        token = "some token"
        message = {"type": "tile",  "text": ["test toast or tile"], "image": ["image.png"]}
        if None in (token, message):
            raise AttributeError("Invalid input parameters for WNS.")

        wns = WNSClient(cred_info)
        response = wns.process(token=token, message=message)
        assert response.status_code == 200