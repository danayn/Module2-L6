# Assignment: Python Strings

'''
1. Product Review Analysis

Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", 
and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords
in uppercase so they stand out.
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  The function should 
return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",


'''
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["good", "excellent", "bad", "poor", "average"]

# Task 1: Keyword Highlighter
def hlit(reviews):
    for review in reviews:
       for keyword in keywords:
            if keyword in review:
                 print(review.replace(keyword, keyword.upper()))
                 print()
            elif(keyword.capitalize() in review):
                print(review.replace(keyword.capitalize(), keyword.upper()))
                print()
    #    z = review.split()
    #    x = len(z)
    #    p = 0
    #    while(p < x):
    #        if(z[p] == "good"):
    #             z[p] = "GOOD"
    #        if(z[p] == "excellent"):
    #             z[p] = "EXCELLENT"
    #        if(z[p] == "bad"):
    #             z[p] = "BAD"
    #        if(z[p] == "poor"):
    #             z[p] = "POOR"
    #        if(z[p] == "average"):
    #             z[p] = "AVERAGE"
    #        p = p + 1
    #    res = " "
       # res.join(z)
    #    print(res.join(z))
    #    print() 
                     

# Task 2: Sentiment Tally
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def postive_count(positive_words):
    pc = 0
    for review in reviews:
        for positive in positive_words:
            if positive in review:
                pc = pc + 1
    print("The total count of Postive words is "+ str(pc) +".") 

def negative_count(negative_words):
    nc = 0
    for review in reviews:
        for negative in negative_words:
            if negative in review:
                nc = nc + 1
    print("The total count of Negative words is "+ str(nc) +".") 


# Task 3: Review Summary

def review(reviews):
    n = 32
    str = " "
    for review in reviews:
        str = review[:n]
        str = str + "..."
        print(str)



hlit(reviews)
postive_count(positive_words)
print()
negative_count(negative_words)
print()
review(reviews)
