tumblrchecker.py
By Jonathan Chang

--------------------------------------

OVERVIEW
This python script chooses n random words (where n is a user-input number) and
concatenates them together, then appends ".tumblr.com" to generate a random 
tumblr address. It then checks to see if the generated address exists.
Best results come from n=2

USAGE
I suggest running this script from command line:
python tumblrchecker.py <number>
Alternatively you can open the script in idle and run it from there. If you do
so, it will begin by prompting for a number.

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
