"""
-Link: https://app.codesignal.com/challenge/HHKmRM9PLczxAFFTy
"""


def findEmailDomain(address):

    for i in range(len(address)-1, -1, -1):
        if address[i] == '@':
            return address[i +1 : len(address)]