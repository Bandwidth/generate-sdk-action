"""
    Messaging

    Bandwidth's HTTP Messaging platform ## Base Path <code>https://messaging.bandwidth.com/api/v2</code>  # noqa: E501

    The version of the OpenAPI document: 4.2.8
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bandwidth-test
from bandwidth-test.model.bandwidth_message_item import BandwidthMessageItem
from bandwidth-test.model.page_info import PageInfo
globals()['BandwidthMessageItem'] = BandwidthMessageItem
globals()['PageInfo'] = PageInfo
from bandwidth-test.model.bandwidth_messages_list import BandwidthMessagesList


class TestBandwidthMessagesList(unittest.TestCase):
    """BandwidthMessagesList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBandwidthMessagesList(self):
        """Test BandwidthMessagesList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BandwidthMessagesList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()