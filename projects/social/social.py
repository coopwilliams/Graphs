import numpy as np
from random import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        if avg_friendships > num_users:
            print("Not enough users")
            return

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # add users
        for num in range(num_users):
            self.add_user(num)

        # add friendships
        for user in self.users:
            # sample number of friends from normal distribution
            for i in range(int(np.random.normal(avg_friendships))):
                # user cannot be friends with self or current friends
                possible_friends = list(self.users.keys())
                possible_friends.remove(user)
                possible_friends = [x for x in possible_friends 
                                    if x not in list(self.friendships[user])]
                friend = np.random.choice(possible_friends)
                self.add_friendship(user, friend)
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = dict()
    

        # Check each degree of separation, starting with user
        layer = {user_id}
        # loop until no new IDs found
        another_round = True
        while another_round:
            next_layer = set()
            another_round = False
            for id in layer:
                if id == user_id:
                    visited[id] = [id]
                friends = self.friendships[id]
                next_layer.update(friends)
                for friend in friends:
                    if friend not in visited:
                        another_round = True
                        visited[friend] = visited[id] + [friend]
            layer = next_layer
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
