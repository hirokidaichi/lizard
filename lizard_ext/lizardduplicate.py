'''
Get Duplicated parameter lists
'''
from collections import Counter
from .extension_base import ExtensionBase


class Duplicate(object):
    def __init__(self, start_line):
        self.start_line = start_line

class LizardExtension(ExtensionBase):

    def __init__(self, context=None):
        self.duplicates = []
        super(LizardExtension, self).__init__(context)

    def __call__(self, tokens, reader):
        for token in tokens:
            self.duplicates =[[Duplicate(1), 1]]
            yield token
