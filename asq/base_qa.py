# <description>
#
# Copyright:   (c) Daniel Duma 2016
# Author: Daniel Duma <danielduma@gmail.com>

# For license information, see LICENSE.TXT

class BaseNER(object):
    """
    """

    def __init__(self, elastic_endpoint):
        pass


class BaseQA(object):
    """
        Question Answering class.
    """

    def __init__(self, elastic_endpoint):
        pass

    def answerQuestion(self, question, question_type):
        # Tokenize, analyze, rewrite
        # NER: find known entities
        # Retrieval: find documents
        #
        pass


def main():
    pass

if __name__ == '__main__':
    main()
