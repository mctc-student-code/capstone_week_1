import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):
    
    def test_camelcase_sentence(self):
        
        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))
        self.assertEqual(None, camelCase.camel_case('$hello world'))
        self.assertEqual(None, camelCase.camel_case('1apple Day'))
        self.assertEqual('', camelCase.camel_case(''))