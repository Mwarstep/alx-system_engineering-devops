#!/usr/bin/python3
"""This uses reddit's API."""
import requests


def get_hot_titles(subreddit, after=None, hot_list=[]):
    """Will return top ten post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            return get_hot_titles(subreddit, after_data, hot_list)
        all_titles = results.json().get("data").get("children")
        hot_list.extend(title_.get("data").get("title")
                        for title_ in all_titles)
        return hot_list
    else:
        return None


subreddit = input("Enter subreddit name: ")
hot_titles = get_hot_titles(subreddit)

if hot_titles is not None:
    for index, title in enumerate(hot_titles, start=1):
        print(f"{index}. {title}")
else:
    print("An error occurred or the subreddit does not exist.")
