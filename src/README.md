# CryptoCurrency Comment Parser

Simple script and bot which finds the daily thread on `reddit.com/r/cryptocurrency` and counts the number of times a coin defined in `coins.txt` has been mentionen in a comment.
My idea is that this is a basic and very crude indication of popularity, coin shilling and/or current rockets which could be used as a data point for desicions regarding investments.

## Caveats

* coin names like `one` are very likely to have skewed data, since it is a common word
* no regards to upvote/downvote or if the coin is mentioned in a positive/negative manner are taken

## Running the script

First you must update the `praw.ini` with your reddit app/bots `client_secret` and `client_id`, as well as `user_agent`:

```
client_id=
client_secret=
user_agent=
```

Then you run it with `src` as the working directory:

```bash
$ ./cccp.py
Parsing comments for coins ...
Expanding 7995 comments    ->
          513.0023 seconds <-
```

And the results are saved in `./result.json`