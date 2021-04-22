#! ../.venv/bin/python

import json
import praw
import time

def get_daily_thread(subreddit):
    """return submission containing 'daily' in the title"""
    for submission in subreddit.hot(limit=5):
        if "daily" in submission.title.lower():
            return submission


def get_coins(filename):
    """return a list of all coins defined in 'filename', containing 1 name per line"""
    with open(filename, 'r') as f:
        return [name.rstrip() for name in f]


def get_all_comments(submission):
    print("Expanding %d comments    ->"%(submission.num_comments))
    start = time.perf_counter()
    submission.comments.replace_more(limit=None)
    end = time.perf_counter()
    print(f"          {end-start:0.4f} seconds <-")
    return submission.comments.list()


def save(dailyname, new_data, filename="result.json"):
    data = []
    try:
        with open(filename, 'r') as fp:
            data = json.load(fp)
    except:
        print("Couldn't find result.json, creating one...")

    now = time.time()
    data.append({"name":dailyname,"coin_stats":new_data, "timestamp": now})
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=4)

def main():
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("cryptocurrency")
    submission = get_daily_thread(subreddit)

    print("Parsing comments for coins ...")
    coins = get_coins('coins.txt')
    coin_stats = {coin:0 for coin in coins}
    for comment in get_all_comments(submission):
        for coin in coins:
            if coin in comment.body.lower().split():
                coin_stats[coin] += 1

    daily = ''.join(submission.title.split('-')[1].split(',')[0].split())
    save(daily, dict(sorted(coin_stats.items(), key=lambda item: item[1], reverse=True)))



if __name__ == '__main__':
    main()