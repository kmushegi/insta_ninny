#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import time
import sys

test_username = 't.589345'
test_password = 'koka123'
test_user_id = '5945742704'

pair_username = ''
pair_password = ''

target_user_id = '541878084'

class insta_ninny:

	def __init__(self, username, password):
		print('Initializing API')
		self.api = InstagramAPI(username, password)
		self.api.login()

	def requestUserInfo(self, user_id):
		self.user_info = self.api.getUsernameInfo(user_id)
		return self.api.LastJson

	def requestUserFollowings(self, last_json, user_id):
		following = []
		next_max_id = True
		while next_max_id:
		    print next_max_id
		    #first iteration hack
		    if next_max_id == True: next_max_id=''
		    _ = self.api.getUserFollowings(user_id,maxid=next_max_id)
		    following.extend ( self.api.LastJson.get('users',[]))
		    next_max_id = self.api.LastJson.get('next_max_id','')

		unique_following = {
    		f['pk'] : f
   			for f in following
		}

		print('Unique Following: ' + str(len(unique_following)))
		return unique_following

	def requestUserFollowers(self, last_json, user_id):
		followers = []
		next_max_id = True
		while next_max_id:
			print next_max_id
			#possibly hackity hack
			if next_max_id == True: next_max_id=''
			_ = self.api.getUserFollowers(user_id, maxid=next_max_id)
			followers.extend ( self.api.LastJson.get('users',[]))
			next_max_id = self.api.LastJson.get('next_max_id','')

		unique_followers = {
			f['pk'] : f
			for f in followers
		}

		print('Unique Followers: ' + str(len(unique_followers)))
		return unique_followers

	def followAccounts(self, user_ids, timeout):
		for idx, uid in enumerate(user_ids):
			print('IDX: ' + str(idx) + ' | Following UID: ' + str(uid))
			self.api.follow(uid)
			time.sleep(timeout)

	def unfollowAccounts(self, user_ids, timeout):
		for idx, uid in enumerate(user_ids):
			print('IDX: ' + str(idx) + ' | Unfollowing UID: ' + str(uid))

			self.api.unfollow(uid)
			time.sleep(timeout)

ig_client = insta_ninny(test_username, test_password)

target_user_info = ig_client.requestUserInfo(target_user_id)
target_unique_followers = ig_client.requestUserFollowers(target_user_info, target_user_id)

test_user_info = ig_client.requestUserInfo(test_user_id)
self_unique_followings = ig_client.requestUserFollowings(test_user_info, test_user_id)

# unique_followings = ig_client.requestUserFollowings(user_info, target_user_id)
ig_client.followAccounts(target_unique_followers, 60)