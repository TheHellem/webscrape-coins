# A script for scraping coin data from www.norgesmynter.no

*Work in progess*

In this script I use selenium to collect data about Norwegian coins from the coin catalogue [Norges Mynter](https://norgesmynter.no/).


## How to Run this script yourself

Make sure that you have selenium installed, if you don't:

`pip install selenium`

You also need [chromeDriver](https://chromedriver.chromium.org/) installed. Also be sure to include it in your path or environment.

If you have this sorted out the script is very much plug-and-play, and when you run it it should spit out a JSON file with data about all Norwegian coins,
that have been in circulation since the late 15th century. Enjoy!