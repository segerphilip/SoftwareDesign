"""
Created by: Philip Seger
Created on: 3/3/14
"""

class User:
	pass

def print_user(user):
	print user.name + " is a " + user.gender
	print "Friends: "
	for friend in user.friends:
		print " " + friend.name

def make_friends(user1, user2):
	user1.friends.append(user2)
	user2.friends.append(user1)

if __name__ == '__main__':
	u = User()
	u.name = "Philip Seger"
	u.gender = "male"
	u.friends = []

	u1 = User()
	u1.name = "Austin Greene"
	u1.gender = "male"
	u1.friends = []

	make_friends(u,u1)

	u1.name = "Austin Funkhouser"

	print_user(u)
	print_user(u1)