from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

traversal_path = []

def traversal(path, room_graph, player):
    from random import random
    revs = {'n':'s', 's':'n', 'w':'e', 'e':'w'}
    clockwise_directions = ['n', 'e', 's', 'w']
    backtrack_path = []
    current = player.current_room.id
    visited = {current}
    while len(visited) < 500:
        # get dictionary of neighboring rooms
        options = room_graph[current][1]

        # choose a direction 
        choice = None
        backtracking = False
        for way in clockwise_directions:
            # pick first unvisited neighbor, moving clockwise
            if (way in options.keys()) and (options[way] not in visited):
                choice = way
                break
        
        # if all neighbors are visited, backtrack a step.
        if choice == None:
            backtracking = True
            choice = revs[backtrack_path.pop()]

        # make the move
        current = options[choice]
        # mark the new room as visited
        visited.add(current)
        # keep track of your path
        path.append(choice)
        # if we're not backtracking, add to the backtrack path
        if not backtracking:
            print("\t-->", current)
            backtrack_path.append(choice)
        else:
            print(current, "<---")
        

traversal(traversal_path, room_graph, player)

print("length is:", len(traversal_path))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

exit()

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
