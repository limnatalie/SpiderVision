# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewsSpider(scrapy.Spider):
    name = 'AmazonReview'
    
    def __init__(self, asin):
        self.start_urls = list()
        for i in range(1, 5):
            myBaseUrl = "https://www.amazon.com/product-reviews/{asin_no}/ref=cm_cr_arp_d_viewopt_sr?pageNumber={page_no}".format(asin_no=asin, page_no=i)
            self.start_urls.append(myBaseUrl)    
    
    
        
    def parse(self, response):
        
        
        #Getting the Review list
        data = response.css('#cm_cr-review_list')
        name = response.css (".product-title")
        
        title = data.css('.review-title')
        
        star_rating = data.css('.review-rating')
        comments = data.css('.review-text')
        count = 0
        #Combining data
        for review in star_rating:
             
            dic={
                'Name':''.join(name.xpath('.//text()').extract()),
                  'Title':''.join(title[count].xpath(".//text()").extract()).strip(),
                  'Rating':''.join(review.xpath('.//text()').extract()).replace(' out of 5 stars',''),
                  'Comment': ''.join(comments[count].xpath(".//text()").extract()).strip()
                  }
           
            yield(dic)
            count = count +1    
            
            
