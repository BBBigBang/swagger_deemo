# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.ner_rel_result import NerRelResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNERandRELController(BaseTestCase):
    """NERandRELController integration test stubs"""

    def test_ner_rel_get(self):
        """Test case for ner_rel_get

        实体识别和关系抽取的返回结果(Get方法)
        """
        query_string = [('content', 'content_example')]
        response = self.client.open(
            '/JkunF_cs/precision_medicine/1.0.0/NER_REL_GET',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ner_rel_post(self):
        """Test case for ner_rel_post

        实体识别和关系抽取的返回结果(Post方法)
        """
        contents = 'contents_example'
        response = self.client.open(
            '/JkunF_cs/precision_medicine/1.0.0/NER_REL_POST',
            method='POST',
            data=json.dumps(contents),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
