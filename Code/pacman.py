import copy

"""..................... Usage checks of transition operators ....................."""

""" Check usage of the fruit-eating operator """
def can_eat(state):
   for row in range(len(state)):
      for col in range(len(state[row])):
         if state[row][col][0] == 'p' and state[row][col][1] == 'f':
            return 1
   return 0 

""" Check usage of the move-right operator """
def can_move_right(state):
   for row in range(len(state)):
      if state[row][len(state[row]) - 1][0] == 'p':
         return 0
   return 1

""" Check usage of the move-left operator """
def can_move_left(state):
   for row in range(len(state)):
      if state[row][0][0] == 'p':
         return 0
   return 1

""" Check usage of the move-up operator """
def can_move_up(state):
   for col in range(len(state[0])):
      if state[0][col][0] == 'p':
         return 0
   return 1

""" Check usage of the move-down operator """
def can_move_down(state):
   for col in range(len(state[len(state) - 1])):
      if state[len(state) - 1][col][0] == 'p':
         return 0
   return 1

"""..................... Transition Operators ....................."""

""" Fruit-eating operator """ 
def eat(state):
   if can_eat(state):
      for row in range(len(state)):
         for col in range(len(state[row])):
            if state[row][col][0] == 'p' and state[row][col][1] == 'f':  
               state[row][col][1] = ' '
               return state                
   else:
      return None

""" Move-right operator """ 
def move_right(state):
   if can_move_right(state):
      for row in range(len(state)):
         for col in range(len(state[row])):   
            if state[row][col][0] == 'p':
               state[row][col][0] = ' '
               state[row][col + 1][0] = 'p'
               return state
   else: 
      return None

""" Move-left operator """ 
def move_left(state):
   if can_move_left(state):
      for row in range(len(state)):
         for col in range(len(state[row])):   
            if state[row][col][0] == 'p':
               state[row][col][0] = ' '
               state[row][col - 1][0] = 'p'
               return state
   else: 
      return None

""" Move-up operator """ 
def move_up(state):
   if can_move_up(state):
      for row in range(len(state)):
         for col in range(len(state[row])):   
            if state[row][col][0] == 'p':
               state[row][col][0] = ' '
               state[row - 1][col][0] = 'p'
               return state
   else: 
      return None

""" Move-down operator """ 
def move_down(state):
   if can_move_down(state):
      for row in range(len(state)):
         for col in range(len(state[row])):   
            if state[row][col][0] == 'p':
               state[row][col][0] = ' '
               state[row + 1][col][0] = 'p'
               return state
   else: 
      return None

"""..................... DFS and BFS Search Algorithms ....................."""

""" Check for finding the goal state """
def is_goal_state(state):
   for row in range(len(state)):
      for col in range(len(state[row])):
         if state[row][col][1] == 'f':
            return 0
   return 1

""" Initialize the search front """
def make_front(state):
   return [state]

""" Initialize the search queue """
def make_queue(state):
    return [[state]]

""" Function to find the path from the initial state to the goal state using DFS or BFS algorithms """
def find_solution(front, queue, closed, goal, method):
   if not front:
      print('No solution found! End of searching...')
   elif front[0] in closed:
        new_front = copy.deepcopy(front)
        new_front.pop(0)
        new_queue = copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
   elif is_goal_state(front[0]):
      print('Goal found!')                         
      for i in range(len(queue[0])):
            for j in range(len(queue[0][i])):
               print(queue[0][i][j])               # Nodes-states in the final path are displayed in a 2D array format one below the other
            print (' ')
   else:
      closed.append(front[0])
      front_copy = copy.deepcopy(front)
      front_children = expand_front(front_copy, method)
      queue_copy = copy.deepcopy(queue)
      queue_children = extend_queue(queue_copy, method)
      closed_copy = copy.deepcopy(closed)
      find_solution(front_children, queue_children, closed_copy, goal, method)

""" Expand the search front """
def expand_front(front, method):  
   if method == 'DFS':                         # Expand the DFS search front
      if front:
         print("Front : ")
         for i in range(len(front)):
            for j in range(len(front[i])):
               print(front[i][j])              # Nodes-states in the search front are displayed in a 2D array format one below the other
            print (' ')
         print('_______________________________________')
         node = front.pop(0)                   # Remove the first node-state from the search front
         for child in find_children(node):     # Find child states of the removed node using the find_children function
            front.insert(0, child)             # Child states are placed in a stack (LIFO) at the beginning of the search front
   elif method == 'BFS':                       # Expand the BFS search front    
      if front:
         print ("Front : ")
         for i in range(len(front)):
            for j in range(len(front[i])):
               print(front[i][j])              # Nodes-states in the search front are displayed in a 2D array format one below the other
            print(' ')
         print('_______________________________________')
         node = front.pop(0)                   # Remove the first node-state from the search front
         for child in find_children(node):     # Find child states of the removed node using the find_children function
            front.append(child)                # Child states are placed in a queue (FIFO) at the end of the search front
            
   return front

""" Expand the search queue """
def extend_queue(queue, method):
# Expand the DFS search queue
   if method == 'DFS':                         
      print ("Queue : ")
      for i in range(len(queue)):
         for j in range(len(queue[i])):
            for w in range(len(queue[i][j])):
               print(queue[i][j][w])           # Nodes-states in the search queue are displayed in a 2D array format one below the other 
            print (' ')                        # A path is a series of nodes, one below the other, ending with the node that appears before the "End of path" message
         print ('------------ End of path ------------')
         print (' ')
      print('_______________________________________')
      node = queue.pop(0)                      # Remove the first path from the search queue
      queue_copy = copy.deepcopy(queue)
      children = find_children(node[-1])       # Find child states of the last node in the removed path using the find_children function
      for child in children:
         path = copy.deepcopy(node)
         path.append(child)                    # Child states are stored in the path list, creating a new path ending in a child node of the last node in the removed path
         queue_copy.insert(0, path)            # The path is placed in a stack (LIFO), at the beginning of the search queue
# Expand the BFS search queue
   elif method == 'BFS':                       
      print ("Queue : ")
      for i in range(len(queue)):
         for j in range(len(queue[i])):
            for w in range(len(queue[i][j])):
               print(queue[i][j][w])           # Nodes-states in the search queue are displayed in a 2D array format one below the other 
            print (' ')
         print ('------------ End of path ------------')
         print (' ')
      print('_______________________________________')
      node = queue.pop(0)                      # Remove the first path from the search queue
      queue_copy = copy.deepcopy(queue)
      children = find_children(node[-1])       # Find child states of the last node in the removed path using the find_children function
      for child in children:
         path = copy.deepcopy(node)
         path.append(child)                    # Child states are stored in the path list, creating a new path ending in a child node of the last node in the removed path
         queue_copy.append(path)               # The path is placed in a queue (FIFO), at the end of the search queue
    
   return queue_copy

""" Function to find descendants of a node state """
def find_children(state):
   children = []
   right_state = copy.deepcopy(state)       
   child_right = move_right(right_state)      # Find descendant-state where pacman can move to the right 
   left_state = copy.deepcopy(state) 
   child_left = move_left(left_state)         # Find descendant-state where pacman can move to the left 
   up_state = copy.deepcopy(state)
   child_up = move_up(up_state)               # Find descendant-state where pacman can move up 
   down_state = copy.deepcopy(state)
   child_down = move_down(down_state)         # Find descendant-state where pacman can move down 
   eat_state = copy.deepcopy(state) 
   child_eat = eat(eat_state)                 # Find descendant-state where pacman eats fruit 

   if child_right:
      children.append(child_right)            # If the descendant-state is not null, add it to the list of descendants
   if child_left:
      children.append(child_left)
   if child_up:
      children.append(child_up)
   if child_down:
      children.append(child_down)
   if child_eat:
      children.append(child_eat)
    
   return children

    
"""..................... Problem World ....................."""

def main():
   # Initial and goal state of the problem in 4x4 dimensions (DFS is preferred as the main search algorithm)
   
   init_state = [[[' ', 'f'], [' ', 'f'], [' ', ' '], [' ', 'f']], 
                 [[' ', ' '], [' ', ' '], ['p', ' '], [' ', 'f']], 
                 [[' ', ' '], [' ', 'f'], [' ', 'f'], [' ', ' ']], 
                 [[' ', 'f'], [' ', 'f'], [' ', 'f'], [' ', 'f']]]  

   goal_state = [[[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']], 
                 [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']], 
                 [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']], 
                 [[' ', ' '], [' ', ' '], [' ', ' '], ['p', ' ']]]   
   
   # Initial and goal state of the problem for a case where a solution cannot be found 
   """
   init_state = []
   
   goal_state = []
   """
   # Initial and goal state of the problem where the initial state is the same as the goal state 
   """ 
   init_state = [[[' ', ' '], ['p', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' ']]]
   
   goal_state = [[[' ', ' '], ['p', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' ']]]
   """
   # Initial and goal state of the problem in 2x2 dimensions (BFS is preferred for Step D)
   """
   init_state = [[[' ', 'f'], ['p', ' ']],
                 [[' ', 'f'], [' ', ' ']]]
   
   goal_state = [[[' ', ' '], [' ', ' ']],
                 [['p', ' '], [' ', ' ']]]
   """
   # Initial and goal state of the problem in 2x2 dimensions (BFS is preferred for Step D)
   """
   init_state = [[[' ', ' '], [' ', 'f']],
                 [['p', ' '], [' ', 'f']]]
   
   goal_state = [[[' ', ' '], ['p', ' ']],
                 [[' ', ' '], [' ', ' ']]]
   """
   method = 'Blind searching algorithm'
   # Choose between the two search algorithms, DFS or BFS, as the main search algorithm to solve the pacman problem
   while method != 'DFS' and method != 'BFS':
      method = input('Choose between DFS and BFS as main blind searching algorithm : ')
   # Call find_solution to find the path that will lead from the predefined initial to the goal state using the selected search algorithm
   print(' ')
   print('Begin Searching...')
   print('Searching algorithm :', method)
   print(' ')
   find_solution(make_front(init_state), make_queue(init_state), [], goal_state, method)

if __name__ == "__main__":
    main()
