import unittest
import sys
import random
from mostFrequent import mF
from haveSumWillAdd import hswa

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.mfclass = mF()
        self.hswaclass = hswa()

    ###############################################################
    # Testing mostFrequent

    def test_mostFrequent1(self):
        #self.seq.
        self.seq = [1]
        self.assertEqual(mF.mostFrequent(self.mfclass, self.seq), 1)
    
    def test_mostFrequent_2(self):
        self.seq = [1,1,2]
        self.assertEqual(mF.mostFrequent(self.mfclass, self.seq), 1)

    def test_mF_2(self):
        self.seq = [1,2,2]
        self.assertEqual(mF.mostFrequent(self.mfclass, self.seq), 2)

    def test_mF_backwards2(self):
        self.seq = [2,2,1,3]
        self.assertEqual(mF.mostFrequent(self.mfclass, self.seq), 2)

    def test_mF_empty(self):   
        self.seq = []
        self.assertEqual(mF.mostFrequent(self.mfclass, self.seq), [])

    def test_mF_None(self):
        #(not None) == false
        self.seq = None
        self.assertEqual(mF.mostFrequent(self.mfclass, self.seq), [])

    ####################################################################3
    # Testing haveSumWillAdd

    def test_hswa_10functionality(self):
        self.seq = [1,9]
        self.assertEqual(hswa.haveSumWAnaive(self.hswaclass, self.seq), [(1,9)])

    def test_hswa_10functionality_0(self):
        self.seq = [10,0]
        self.assertEqual(hswa.haveSumWAnaive(self.hswaclass, self.seq), [(10,0)])

    def test_hswa_10functionality_10alone(self):
        #should return 10 by itself
        self.seq = [10]
        self.assertEqual(hswa.haveSumWAnaive(self.hswaclass, self.seq), [])

    def test_hswa_10functionality_Duplicates(self):
        #judgement call: should return one instance of each duplicate
        self.seq = [1,9,1,9]
        self.assertEqual(hswa.haveSumWAnaive(self.hswaclass, self.seq), [(1,9)])

    #def test_hswa_10functionality_ordering(self):

    #def test_hswa_



if __name__ == '__main__':
    unittest.main()