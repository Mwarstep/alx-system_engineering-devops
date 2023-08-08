#!/usr/bin/python3
"""
This gives the number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Will query the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
