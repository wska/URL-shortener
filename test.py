
# William Skagerström - 23-04-2019

import requests
import random
import string
import unittest
#from init import initialize_table, reset_table

from urlshortener import *
from baseconversion import *

from multiprocessing import Pool, Process, cpu_count


class tests(unittest.TestCase):

    '''Status code of a POST request should be 200, OK. '''
    def testPostRequest(self):
        url = "https://en.wikipedia.org/wiki/Representational_state_transfer"
        r = requests.post('http://localhost:8000/', data= {'url': url})
        self.assertEqual(r.status_code, 200)


    
    ''' Stress test. Creates 400 fake urls and spams the server with them on all available processors in parallel.'''
    def testStress(self):
        fakeUrls = ["http://fakeUrl" + str(i) for i in range(0,400)]
        with Pool(cpu_count()) as p:
            result = p.map(makePostRequest, fakeUrls)
    
        for response in result:
            self.assertEqual(response.status_code, 200)
        
    


    ''' 
    Some tests for the base conversion.
    Complete base: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '''
    def testBase62Conversion1(self):
        self.assertEqual(base62(62), '10')
    
    def testBase62Conversion2(self):
        self.assertEqual(base62(61), 'Z')

    def testBase62Conversion3(self):
        self.assertEqual(base62(11),'b')

    def testBase62Conversion4(self):
        self.assertEqual(base62(124),'20')

    def testBase62Conversion5(self):
        self.assertEqual(base62(62*10),'a0')


    def testBase10Conversion1(self):
        self.assertEqual(base10('bb'),(62*11+11))

    def testBase10Conversion2(self):
        self.assertEqual(base10('00005'),(5))

    def testBase10Conversion3(self):
        self.assertEqual(base10('111'),(62**2+62**1+62**0))


def makePostRequest(url):
        return requests.post('http://localhost:8000/', data= {'url': url})

if __name__ == '__main__':
    
    unittest.main()