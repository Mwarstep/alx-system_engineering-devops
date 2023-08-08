#!/usr/bin/python3
"""This uses reddit's API."""
import requests


def recurse(subreddit, hot_list=None):
    """Will return top ten post titles recursively"""
    if hot_list is None:
        hot_list = []

    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_data in all_titles:
            hot_list.append(title_data.get("data").get("title"))
        return hot_list
    else:
        return None


subreddit = input("Enter subreddit name: ")
hot_titles = recurse(subreddit)

if hot_titles is not None:
    for index, title in enumerate(hot_titles, start=1):
        print(f"{index}. {title}")
else:
    print("An error occurred or the subreddit does not exist.")

