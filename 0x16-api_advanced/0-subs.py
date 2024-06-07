#!/usr/bin/python3
"""
Script to query the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers for a given subreddit.

    :param subreddit: Name of the subreddit
    :return: Number of subscribers, or 0 if the subreddit does not exist or an error occurs
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException as e:
        # Handle any requests exceptions, such as network issues
        print(f"Error fetching subreddit data: {e}")
        return 0
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error parsing JSON response: {e}")
        return 0


# Example usage:
if __name__ == "__main__":
    subreddit_name = "python"
    subscribers = number_of_subscribers(subreddit_name)
    print(f"Number of subscribers in r/{subreddit_name}: {subscribers}")
