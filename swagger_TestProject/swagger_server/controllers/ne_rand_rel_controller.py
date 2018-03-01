import connexion
import six

from swagger_server.models.ner_rel_result import NerRelResult  # noqa: E501
from swagger_server import util

import os, sys
sys.path.append('./src')

from src.mainClass import Spider

print("Ready")

def run(query):
    spider = Spider()
    result = spider.start(query)

    return result

def ner_rel_get(content):  # noqa: E501
    """实体识别和关系抽取的返回结果(Get方法)

    Returns a list containing named entity recoginize and relation extraction result. # noqa: E501

    :param content: you can only input one sentence at one time
    :type content: str

    :rtype: NerRelResult
    """

    result = run(content)

    return result

def ner_rel_post(contents):  # noqa: E501
    """实体识别和关系抽取的返回结果(Post方法)

    Returns a list containing named entity recoginize and relation extraction result. # noqa: E501

    :param contents: one sentence at once
    :type contents: str

    :rtype: NerRelResult
    """

    result = run(contents)

    return result