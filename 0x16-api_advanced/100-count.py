#!/usr/bin/python3
"""
100-count
"""
import requests
import json
import re

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    # Initialize the counts dictionary with the word list
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    # Base case: no more pages
    if after is None and counts == {}:
        return None

    # Set the headers and parameters for the request
    headers = {'User-Agent': 'holberton'}
    params = {'limit': 100}
    if after is not None:
        params['after'] = after

    # Make the request and get the JSON response
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()

    # Get the list of posts and the next page
    posts = data['data']['children']
    after = data['data']['after']

    # Loop through each post and count the keywords in the title
    for post in posts:
        title = post['data']['title']
        for word in word_list:
            # Use regular expression to match whole words, ignoring case and punctuation
            pattern = r'\b{}\b'.format(word)
            matches = re.findall(pattern, title, re.IGNORECASE)
            counts[word.lower()] += len(matches)

    # Recursive case: go to the next page if exists
    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        # Print the results in descending order by count
        print_results(counts)

def print_results(counts):
    """
    Prints the keyword counts in descending order by count,
    and ascending order alphabetically by keyword
    """
    # Sort the counts by value (descending) and key (ascending)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print only the keywords with non-zero count
    for key, value in sorted_counts:
        if value > 0:
            print("{}: {}".format(key, value))
