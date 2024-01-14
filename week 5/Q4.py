'''Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.'''

import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def check_website(url):
    try:
        response = urlopen(url)
        print(f"The website at '{url}' is working.")
    except HTTPError as e:
        print(f"The website at '{url}' is not working. HTTP status code: {e.code}")
    except URLError as e:
        print(f"Error: {e.reason}")

url = sys.argv[1]
check_website(url)