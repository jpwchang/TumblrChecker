tumblrchecker.py
By Jonathan Chang

--------------------------------------

OVERVIEW
This python script chooses n random words (where n is a user-input number) and
concatenates them together, then appends ".tumblr.com" to generate a random 
tumblr address. It then checks to see if the generated address exists.
Best results come from n=2

USAGE
Command-line usage: tumblrchecker.py [-h] [-l] [-n N]

optional arguments:
  -h, --help  show this help message and exit
  -l          Loop until a valid address is found. If not enabled, stops after
              the first address (whether successful or not)
  -n N        Number of words to randomly generate. If not specified, program
              will prompt user for number of words.

You may also run from the Python IDLE environment. This will supply no arguments,
so the program will default to asking for a number of words and not looping


REQUIREMENTS
You must have urllib2 and beautifulsoup4 installed. To install them, type the
following into a command line:
pip install urllib3
pip install beautifulsoup4

CREDITS
Thanks to the developers of the beautifulsoup and urllib libraries.
Word lists come from "words" (a unix utility) and the following website:
http://www.englishclub.com/vocabulary/common-words-5000.htm

Questions? Email me at jonathan.chang13@gmail.com
