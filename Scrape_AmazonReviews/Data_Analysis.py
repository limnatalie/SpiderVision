# -*- coding: utf-8 -*-
"""
Created on Thu May 21 23:06:42 2020

@author: lim"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.stem import WordNetLemmatizer
from textwrap import wrap
from sentenceprocessor import process_sentence


lemmatizer = WordNetLemmatizer()
dataset = pd.read_csv("output.csv")

stopwords = set(STOPWORDS)
#star rating of all reviews
def bargraph():    
    summarised_results = dataset["Rating"].value_counts()
    plt.figure(1)
    plt.bar(summarised_results.keys(),summarised_results.values) #ALLOW change color,size parameter
    #Check documentation: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html
    plt.xlabel("out of 5 stars")
    plt.ylabel("Number of ratings")
    plt.title("Overall rating")

#Wordcloud of all comments
# def visualize():
#     words = ' '    
#     for msg in dataset["Comment"]:
#         msg = str(msg).lower()
#         words = words + msg +' '
    
#     stopwords.update(['the printer','hp','printer','print','the','find','it'])
    
#     plt.figure(2)
#     wordcloud = WordCloud(width=3000,height=2500,stopwords = stopwords, background_color='white').generate(words)
#     fig_size = plt.rcParams['figure.figsize']
#     fig_size[0]=14
#     fig_size[1]=7
#     plt.imshow(wordcloud)
#     plt.axis("off")

#Selection of top words
# def top():
    
#     words = ' '
#     for msg in dataset["Comment"]:
#         msg = str(msg).lower()
#         words = words + msg +' '  
#     stopwords.update(['','hp','printer','print','the','find','it','a','wa','will','one'])
#     split_words = words.split()
#     table = str.maketrans('','', string.punctuation)
#     stripped =[w.translate(table) for w in split_words]
#     #Counter
#     dic={}
#     for word in stripped:
#         word = (lemmatizer.lemmatize(word))
#         if word in dic:
#             dic[word]+=1
#         else:
#             dic[word]=1
#     main_dic={key:value for key,value in sorted(dic.items(),key = lambda item:item[1]) if key not in stopwords}        
    
#     count = Counter(main_dic)
#     top_3 = count.most_common(3)
#     top_10 = count.most_common(10)
    
#     return(top_3,top_10)

#Top 10 words in a bargraph
# def top10_bargraph():
#     result = top()
#     top_10= result[1]  
#     plt.figure(2)
#     plt.bar(range(len(top_10)),[val[1] for val in top_10])
#     plt.xticks(range(len(top_10)), [val[0] for val in top_10])
#     plt.xticks(rotation = 70)
#     plt.xlabel("Words")
#     plt.ylabel("Number of Occurences")
#     plt.title("Most popular words (All Reviews)")

#Dictionary issue buckets

#Selection of reviews     
# def top3_review(input_word):
    
#     for comment in dataset["Comment"]:
#         if input_word in comment:
#             return(comment)
# #Wordcloud of reviews of selected word            
# def top3_wordcloud(input_word):
    
#     comment = str(top3_review(input_word))
    
#     stopwords.update(['the printer','hp','printer','print','the','find','it'])
    
#     plt.figure(3)
#     wordcloud = WordCloud(width=3000,height=2500,stopwords = stopwords, background_color='white').generate(comment)
#     fig_size = plt.rcParams['figure.figsize']
#     fig_size[0]=14
#     fig_size[1]=7
#     plt.imshow(wordcloud)
#     plt.axis("off")
    
    
# Takes adjectives from reviews and puts into a wordcloud
# Larger word => more often said
def wordcloud():
   dic={} 
   for msg in dataset["Comment"]:
       for sentence in msg.split("."):
           text = nltk.word_tokenize(sentence)
           tagged=nltk.pos_tag(text)
           
           for x in tagged:
            tag = x[1][0].upper()
            if tag == "J":
                if x[0] in dic:
                    dic[x[0]]+=1
                else:
                    dic[x[0]]=1
   dictionary = dic
   wc = WordCloud(background_color="white",width=1000,height=1000,max_words=15,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dictionary)
   #ABLE TO CHANGE BACKGROUND_COLOR
   plt.imshow(wc)
   plt.axis("off")
   
#FILTER BAD REVIEWS: RATINGS WITH LESS THAN 3 STARS
def bad_review_filter():
    bad_reviews=dataset.loc[dataset["Rating"]< 3]
    bad_reviews=bad_reviews["Comment"]
    return bad_reviews
def good_review_filter():
    good_reviews=dataset.loc[dataset["Rating"]>2]
    good_reviews=good_reviews["Comment"]
    return good_reviews


# def bad_review_top():
#     bad_reviews=review_filter()
#     words = ' '
#     for msg in bad_reviews:
#         msg = str(msg).lower()
#         words = words + msg +' '  
#     stopwords.update(['','hp','printer','print','the','find','it','a','wa','will','one'])
#     split_words = words.split()
#     table = str.maketrans('','', string.punctuation)
#     stripped =[w.translate(table) for w in split_words]
#     #Counter
#     dic={}
#     for word in stripped:
#         word = (lemmatizer.lemmatize(word))
#         if word in dic:
#             dic[word]+=1
#         else:
#             dic[word]=1
#     main_dic={key:value for key,value in sorted(dic.items(),key = lambda item:item[1]) if key not in stopwords}        
    
#     count = Counter(main_dic)
#     top_10 = count.most_common(10)
#     return top_10
# def bad_top10_bargraph():
#     top_10 = bad_review_top()
    
#     plt.figure(4)
#     plt.bar(range(len(top_10)),[val[1] for val in top_10])
#     plt.xticks(range(len(top_10)), [val[0] for val in top_10])
#     plt.xticks(rotation = 70)
#     plt.xlabel("Words")
#     plt.ylabel("Number of Occurences")
#     plt.title("Most popular words (Poor Reviews)")

def review_filter():
    while True:
     
        r_input = input("Search good or bad reviews (g/b):")
        if r_input.lower()=="g":
            
            review=good_review_filter()
            key_phrase(review)
        elif r_input.lower() =="b":
            review=bad_review_filter()
            key_phrase(review)
            
        elif r_input.lower()=='back':
            break
        else:
            print("Invalid input.")
            
#Returns sentence in which word is found in review
def key_phrase(review):
    counter_2=0 #No. of invalid inputs
    
    while True:
        y = input("Type in search word:")
        option = process_sentence(y)[len(process_sentence(y))-1]
        text= ''
        labelled_review=''
        review_counter2=1
        for msg in review: 
            msg = str(msg).lower()
            text= msg + text 
            labelled_review = labelled_review +'Review {}'.format(review_counter2)+'\n'+ msg +'\n\n'
            review_counter2+=1
        
        
        if y.lower() == 'back': #To exit to output selection
            break
        
        elif y.lower() == 'print all': #prints all reviews
            print(labelled_review)
                
        elif "print review" in y.lower(): #enter "print review [number]"
            number= int(y.lower().replace("print review ",''))
            review_counter3=1
            if number in range(len(review)+1):
                for msg in review:
                    if number == review_counter3:
                        print('Review {}'.format(review_counter3)+'\n'+ msg)
                    review_counter3+=1
            else:
                print("Review does not exist")
                    

        elif option in process_sentence(text): #Checks if word is present
            review_counter=1        #Gives review number for further reference
            total_count=0
            for msg in review:

                if option in process_sentence(msg): #Check for search word in review
                    print('Review {}'.format(review_counter))
                    total_count+=1
                    counter = 1
                    for sentence in msg.split("."):
                        if option in process_sentence(sentence): #Checks for word in sentence
                            print(str(counter) + '. ' + sentence)
                            counter += 1
                    print("\n")
                review_counter+=1 
            print("{} related reviews".format(total_count))
        else: #after invalid input 2 consecutive times, user prompt to return to output selection
            print('Search word does not exist. Please input another value.')
            if counter_2 >=1:
                print("To exit to output selection, type 'back'")
            counter_2 +=1

#issue Bucket list
def issue_bucket():
    
    issues = pd.read_csv("Issue Buckets.csv")
    
    level_1 = []
    for x in issues["Level 1"]:
        if x not in level_1 and str(x) != 'nan':
            level_1.append(x)
            
    level_2=[]
    for x in range(len(level_1)):
        f3 = issues["Level 1"]==level_1[x]
        level_2a = []
        for y in issues.loc[f3,"Level 2"]:
            if y not in level_2a and str(y) != 'nan':
                level_2a.append(y)
        level_2.append(level_2a)
    level_2b=[]
    for x in issues["Level 2"]:
        if x not in level_2b and str(x) != 'nan':
            level_2b.append(x)
            
    return level_1,level_2
#issue bucket counter
def issue_bucket_dict():
    issues = pd.read_csv("Issue Buckets.csv")
    bad_reviews=bad_review_filter()
    level_1=issue_bucket()[0]    
    dic = {}
    for word in level_1:
        f3 = issues["Level 1"]== word
        related_words=list(issues.loc[f3,"Related words"])
        review_counter=0
        review_counter1=0
        
        for msg in bad_reviews: 
            msg=str(msg).lower()
            
            
            if any(word in process_sentence(msg) for word in related_words):
                
                review_counter+=1
            else:
                review_counter1+=1
        dic[word]=review_counter
    dic['Others']=review_counter1
    return dic
    
#hardware review counter
def hardware_bucket():
    issues = pd.read_csv("Issue Buckets.csv")
    bad_reviews=bad_review_filter()
    level_2=issue_bucket()[1]
    dic2={}
    for y in level_2[2]:
        f3 = issues["Level 2"]== y
        related_words=list(issues.loc[f3,"Related words"])
        review_counter=0
        for msg in bad_reviews: 
            msg=str(msg).lower()
            
            
            if any(word in process_sentence(msg) for word in related_words):
                review_counter+=1
                
        dic2[y]=review_counter
    return dic2

#Show related reviews to chosen hardware topic
def hardware_reviews():
    while True:
        issues = pd.read_csv("Issue Buckets.csv")
        bad_reviews=bad_review_filter()
        level_2=issue_bucket()[1]
        hardware_dict={}
        counter = 1
        for x in level_2[2]:
            if x not in hardware_dict and str(x) != 'nan':
                hardware_dict[str(counter)]=x
                counter +=1
        print(hardware_dict) #prints options to choose from
        option = input("Enter option number:")
        
        text=''
        for msg in bad_reviews:
            msg=str(msg).lower()
            text=text + msg
            
        if option.lower() == 'back':
                break  
        
        elif option in hardware_dict:
            y=hardware_dict[option]
            print(y)
            f3 = issues["Level 2"]== y
            related_words=list(issues.loc[f3,"Related words"])
            if any(word in process_sentence(text) for word in related_words): #checks if word is present at all
                review_counter=1
                total_count=0
                for msg in bad_reviews: 
                        msg=str(msg).lower()
                        
                        counter =1
                        if any(word in process_sentence(msg) for word in related_words):#check if word in review
                              print('\n Review {}'.format(review_counter))
                              for sentence in msg.split('.'): 
                                    if any(word in process_sentence(sentence) for word in related_words):#checks if word in sentence
                                        print("{}. ".format(counter)+sentence)
                                        counter+=1
                              total_count += 1
                        
                        review_counter+=1
                print("\n{} related reviews\n".format(total_count) ) #Total related issues
            
            else:
                print("No related reviews")
        elif 'print review' in option.lower(): #Allows you to search for entire review
            number= int(option.lower().replace("print review ",''))
            review_counter3=1
            review=bad_review_filter()
            if number in range(len(review)+1):
                for msg in review:
                    if number == review_counter3:
                        print('Review {}'.format(review_counter3)+'\n'+ msg)
                    review_counter3+=1
            else:
                print("Review does not exist")
        else:
            print("Invalid option. Please enter another value or enter 'back' to return.\n")

##What hardware issues being faced (Wordcloud)           
def hardware_wordcloud():
    issues = pd.read_csv("Issue Buckets.csv")
    bad_reviews=bad_review_filter()
    
    f1 = issues["Level 1"]=="Hardware"
    related_words=list(issues.loc[f1,"Related words"])
    dic={}
    counter = 0
    for msg in bad_reviews:
        msg=str(msg).lower()
        
        for word in process_sentence(msg):
            if word in related_words:
            
        # if any(word in process_sentence(msg) for word in related_words):
                counter+=1
                dic[word]=counter
    
    dictionary = dic
    wc = WordCloud(background_color="white",width=1000,height=1000,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dictionary)
    plt.imshow(wc)
    plt.axis("off")


#Issue bucket bargraphs                  
def issue_bucket_bargraph():
    
    dic =issue_bucket_dict()

    
    plt.figure(5)
    ylabels=list(dic.keys())
    ylabels = [ '\n'.join(wrap(l, 20)) for l in ylabels ]
    plt.barh(ylabels,dic.values())
    
    plt.yticks(wrap=True)
    plt.ylabel("Issue Buckets",{"fontsize":15})
    plt.xlabel("Number of Reviews",{"fontsize":15})
    plt.title("Issue Buckets",{"fontsize":20})
#hardware issues bargraph    
def hardware_bucket_bargraph():
    dic2=hardware_bucket()
    
    plt.figure(6)
    ylabels=list(dic2.keys())
    ylabels = [ '\n'.join(wrap(l, 20)) for l in ylabels ]
    plt.barh(ylabels,dic2.values())
    
    plt.yticks(wrap=True)
    plt.ylabel("Issue Buckets",{"fontsize":15})
    plt.xlabel("Number of Reviews",{"fontsize":15})
    plt.title("Issue Bucket: Hardware",{"fontsize":20})


#main program
if __name__ =="__main__":
    counter_2=0
    review_count=0
    for msg in dataset["Comment"]:
        review_count+=1
    print('Total {} product reviews scraped'.format(review_count))
    
    while True:
        user=input("Enter output (bargraphs/hw reviews/wordcloud/search phrase):")
        #Bargraphs
        if user.lower() =="bargraphs":
            print("Loading...")
            bargraph()   #Ratings 
            issue_bucket_bargraph()  #Main issue bucket
            hardware_bucket_bargraph()  #Hardware issue bucket
            plt.show()
            print("Finished")
        #Filter hardware issues
        elif user.lower() == "hw reviews":
            hardware_reviews() 
        #Wordclouds
        elif user.lower() == "wordcloud":
            counter_3=0
            while True:      
                input_word=input("Select option (all/hardware):")
                if input_word.lower() == 'back':
                    break
                
                elif input_word.lower() == 'all': #What people think of product
                    print("Loading...")
                    wordcloud()
                    plt.show()
                    print("Finished")
                elif input_word.lower()=='hardware': #What hardware issues being faced
                    print("Loading...") 
                    hardware_wordcloud()
                    plt.show()
                    print("Finished")

                else:
                    print("Please key in valid input.")
                    if counter_3 >=1:
                        print("To exit to output selection, type 'back'.")
                    counter_3 +=1
        #Sentences with search word present  
        elif user.lower() == "search phrase":
            review_filter()
        #Ends data analysis program   
        elif user.lower() == "end":
            break
        #for invalid input, user is prompted to enter a valid one.
        #if more than 2 consecutive invalid input, end prompt is printed
        else:
            print("Please key in a valid input.")
            if counter_2 >=1:
                print("To exit, type 'end'.")
            counter_2 +=1

