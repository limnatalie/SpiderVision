SpiderVision
Amazon review webscrapper and analysis

1. Create virtual environment in folder
https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html 
2. Install all packages in virtual environment


Commands:
	python main.py		runs scraper


Please input ASIN number: [input number]		Product to scrape

Output selection:
Enter output (bargraphs/hw reviews/wordcloud/search phrase): [enter option from bracket]

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