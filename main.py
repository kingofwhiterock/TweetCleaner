# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# #########################################################################
#
# 2020/05/20
# written by: Apoi
# version: 1.0.0
#
# #########################################################################
#
# PROJECT:
# * TweetCleaner
#
# FILE PURPOSE:
# * To delete all of my tweets.
#
# FILE ISSUE
#
# #########################################################################


# #########################################################################
# library importing
# #########################################################################
import os
import twitter
import json
# #########################################################################
# python file importing
# #########################################################################

# #########################################################################
# class
# #########################################################################


class TweetCleaner:

    def __init__(self):
        pass

    def main(self):
        # api settings
        api = twitter.Api(
            consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        )

        # to delete valiable name
        with open('dataset/tweet.js', encoding='utf-8', mode='r') as f:
            text = f.read()
            text = text.replace('window.YTD.tweet.part0 = ', '', 1)
        with open('dataset/tweet.js', encoding='utf-8', mode='w') as f:
            f.write(text)

        # to delete tweets
        with open('dataset/log.txt', mode='w', encoding='utf-8')as l:
            with open('dataset/tweet.js', mode='r', encoding='utf-8') as f:
                json_data = json.load(f)
                for tweet0 in json_data:
                    tweet = tweet0['tweet']
                    print(tweet['id'] + '->', end='')
                    try:
                        api.DestroyStatus(tweet['id'])
                        print('deleted')
                    except Exception as e:
                        print('not deleted. See "log.txt".')
                        l.write(tweet['id'] + '->' + e.args + '\n')


if __name__ == "__main__":
    tc = TweetCleaner()
    tc.main()
