#!/usr/bin/python3
"""This uses reddit's API."""
import requests
post = None


def recurse(subreddit, hot_list=[]):
    """Willreturn top ten post titles recursively"""
    global post
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': post}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        post_data = results.json().get("data").get("after")
        if post_data is not None:
            post = post_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
