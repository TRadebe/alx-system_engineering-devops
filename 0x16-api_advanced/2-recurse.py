#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store titles of hot posts (default is an empty list).
        after (str): Identifier for the next set of posts in pagination (default is an empty string).
        count (int): Running count of posts retrieved (default is 0).

    Returns:
        list or None: Returns a list of titles of all hot posts on the specified subreddit.
                     Returns None if the subreddit is not found (404 error).
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
