# A script for scraping coin data from www.norgesmynter.no

> :warning: **This has nothing to do with crypto currency**: It's about those shiny metal things!

_Work in progress_

In this script I use selenium and beautifulsoup to collect data about Norwegian coins, from the coin catalogue [Norges Mynter](https://norgesmynter.no/), for personal use. 
The purpose of making this public is solely to demonstrate an example of webscraping. 

## How to Run this script

Make sure that you have selenium installed, if you don't:

> pip install selenium

You also need [chromeDriver](https://chromedriver.chromium.org/) installed. Also be sure to include it in your path or environment.

After this you will have to create an account on [norgesmynter.no](https://norgesmynter.no/). It is easier to do this if you speak Norwegian. If not try to make an Norwegian friend, or just learning the language. I recomend [Dualingo](https://www.duolingo.com/).

Then you'll need to set up a config.ini file with the following:


```
[credentials]
username = <your-username>
password = <your-password>
```

If you have this sorted out, then the script is very much plug-and-play. When you run it it should spit out a JSON file with data about all Norwegian coins
that have been in circulation since the late 15th century. Enjoy!

> :warning: **Scrape at own risk** When this script was made, [norgesmynter.no](https://norgesmynter.no/) had no disclaimer or terms of conditions against the use of their data. This might change.
