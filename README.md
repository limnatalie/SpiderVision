# SpiderVision
Amazon Review webscrapper and analysis.

**Main Functions**
 - Scrapes product reviews of amazon.com using Scrapy
 - Gives rating distribution, issue distribution, overall sentiments of product
 - Allows you to search reviews for related words
- Uses Wordcloud to give easy overview of sentiments and issues visually


# Installation
1. Install Python.
[How to Install Python](https://realpython.com/installing-python/)
	> Note: Add python to PATH when installing
2. Navigate to where SpiderVision has been downloaded using command prompt.
`cd <file location>`
3. Create virtual environment in the file.
	```
	virtualenv venv
	.\venv\Scripts\activate
	```
	>If you need more help,
	[How to create virtual environment](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)

4. Install all packages
Enter the following into the command prompt:
`pip install -r requirements.txt`
5. Run the code
`python main.py`
## After installing once,

1. Activate virtual environment.
`.\venv\Scripts\activate`
2. Run code
`python main.py`

# How to use

## Commands:
```
python main.py		Runs scraper
Please input ASIN number: [input number]	Enter Product to scrape
```
**Output selection:**
```
Enter output (bargraphs/hw reviews/wordcloud/search phrase): [enter option from bracket]```

hw reviews:
Enter option number: 

--[enter option number from bracket]	prints related parts of review to option chosen
--print review #			print selected review
--back					return to output selection
*To change issue buckets, go to 'Issue Buckets.csv' in folder
* # == number


wordcloud:
Select option (all/hardware):

--all		wordcloud of adjectives used by reviews
--hardware 	wordcloud of hardware issues people faced
--back 		return to output selection


search phrase:
Search good or bad reviews (g/b):

--g		searches in good reviews
--b		searches in bad reviews


Type in search word:

--[enter word to search]		prints sections of reviews where searched word is present
--print all				prints all reviews
--print review #			print selected review
*# == number
```
