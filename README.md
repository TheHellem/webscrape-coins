# A script for scraping coin data from www.norgesmynter.no

> :warning: **This has nothing to do with cryptocurrency**: It's about those shiny metal things.

_Work in progress! Sort of, at least... The JSON file that this code produces is not very useful. If I decide to do another project that requires this data, it will have to change._

In this script, I use Selenium and BeautifulSoup to collect data about Norwegian coins from the coin catalogue [Norges Mynter](https://norgesmynter.no/). This is solely for personal use in this and other personal projects. The purpose of making this public is only to demonstrate an example of web scraping. I have no rights to the data collected by this script, and if you intend to use it for anything, I recommend that you check out the [terms and conditions](https://norgesmynter.no/personvern/) of norgesmynter.no.

## How to Run this script

Make sure that you have Selenium installed. If you don't, run:

> pip install selenium

The same goes for [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).

You also need [ChromeDriver](https://chromedriver.chromium.org/) installed. Also, be sure to include it in your path or environment.

After this, you will have to create an account on [norgesmynter.no](https://norgesmynter.no/). It is easier to do this if you speak Norwegian. If not, try to make a Norwegian friend, or just learn the language. I recommend [Duolingo](https://www.duolingo.com/).

Then, you'll need to set up a `config.ini` file with the following:


```
[credentials]
username = <your-username>
password = <your-password>
```

If you have this sorted out, then the script is very much plug-and-play. When you run it it should spit out a very confusing JSON file with data about all Norwegian coins
that have been in circulation since aproximately 1819. Enjoy!

