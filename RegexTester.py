
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import unittest

import re

class NumberRegex(unittest.TestCase):
    def setUp(self):
        self.pattern = r"[-+]?[.\d]*[\d]+[:,/.\d]*"
        self.replace = "<number>"
    
    def test_numberInSentence(self):
        text = "We were seeing 124 alpha"
        expected = "We were seeing <number> alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_fractionInSentence(self):
        text = "We were seeing 1/2 alpha"
        expected = "We were seeing <number> alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_decimalInSentence(self):
        text = "We were seeing 0.452 alpha"
        expected = "We were seeing <number> alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
                
    def test_decimalWithoutLeadingZeroInSentence(self):
        text = "We were seeing .452 alpha"
        expected = "We were seeing <number> alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_withPositiveSign(self):
        text = "We were seeing +1/3 alpha"
        expected = "We were seeing <number> alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))

    def test_withNegativeSign(self):
        text = "We were seeing -1/10 alpha"
        expected = "We were seeing <number> alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_timeStamp(self):
        text = "We were seeing 1:00:00pm alpha"
        expected = "We were seeing <number>pm alpha" #do we want a separate time tag?
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_currency(self):
        text = "We were seeing $1,200.23 alpha"
        expected = "We were seeing $<number> alpha" #should we eliminate currency symbols as part of number tag or have own tag?
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))

class RepeatedPunctuationRegex(unittest.TestCase):
    def setUp(self):
        self.pattern = r"([!?.]){2,}"
        self.replace = r"\1"
    
    def test_questionMark(self):
        text = "We were seeing .!?.?? alpha"
        expected = "We were seeing ? alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_exclamation(self):
        text = "We were seeing .!?.!! alpha"
        expected = "We were seeing ! alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))
        
    def test_ellipsis(self):
        text = "We were seeing ... alpha"
        expected = "We were seeing . alpha" #should we handle the ellipsis differently?
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))

class HyphenRegex(unittest.TestCase):
    def setUp(self):
        self.pattern = '-'
        self.replace = ' '
    
    def test_hyphen(self):
        text = "We were seeing anti-aircraft alpha"
        expected = "We were seeing anti aircraft alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text))        
        
class AbbreviationRegex(unittest.TestCase):
    def setUp(self):
        self.pattern = r'(?<!\w)([a-zA-Z])\.'
        self.replace = r'\1'
    
    def test_abbrev(self):
        text = "We were seeing N.B.A. alpha"
        expected = "We were seeing NBA alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) 
    
    def test_newSentence(self):
        text = "We saw them yesterday. N.B.A. alpha"
        expected = "We saw them yesterday. NBA alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) 
        
    def test_newSentenceNoSpace(self):
        text = "We saw them yesterday.N.B.A. alpha"
        expected = "We saw them yesterday.NBA alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) 
        
    def test_newSentenceNoSpaceLowerCase(self):
        text = "We saw them yesterday.n.b.a. alpha"
        expected = "We saw them yesterday.nba alpha"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) 

class PunctuationRemovalRegex(unittest.TestCase):
    def setUp(self):
        self.pattern = '[^\w\s\.\<>\?\!]' #Ditch anything other than a letter, number, underscore, space, <>?!.
        self.replace = ''
    
    def test_punctuation(self):
        text = "<s> There were <digit> Number of /\\;:~ looming in the distance?!."
        expected = "<s> There were <digit> Number of  looming in the distance?!."
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) 
    def test_french(self):
        text = "Her name was Reneé"
        expected = "Her name was Reneé"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) 
    def test_underscore(self):
        text = "Her name was _Reneé"
        expected = "Her name was _Reneé"
        self.assertEqual(expected, re.sub(self.pattern, self.replace, text)) #Should we remove underscores?
            
if __name__ == '__main__':
    unittest.main()
