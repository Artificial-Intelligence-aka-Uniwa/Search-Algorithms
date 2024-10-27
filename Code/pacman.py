import copy

"""..................... Έλεγχοι χρήσης των τελεστών μετάβασης ....................."""

""" Έλεγχος χρήσης του τελεστή φαγώματος φρούτου """
def can_eat(state):
   for row in range(len(state)):
      for col in range(len(state[row])):
         if state[row][col][0] == 'p' and state[row][col][1] == 'f':
            return 1
   return 0 

""" Έλεγχος χρήσης του τελεστή μετακίνησης προς τα δεξιά """
def can_move_right(state):
   for row in range(len(state)):
      if state[row][len(state[row]) - 1][0] == 'p':
         return 0
   return 1

""" Έλεγχος χρήσης του τελεστή μετακίνησης προς τα αριστερά """
def can_move_left(state):
   for row in range(len(state)):
      if state[row][0][0] == 'p':
         return 0
   return 1

""" Έλεγχος χρήσης του τελεστή μετακίνησης προς τα πάνω """
def can_move_up(state):
   for col in range(len(state[0])):
      if state[0][col][0] == 'p':
         return 0
   return 1

""" Έλεγχος χρήσης του τελεστή μετακίνησης προς τα κάτω """
def can_move_down(state):
   for col in range(len(state[len(state) - 1])):
      if state[len(state) - 1][col][0] == 'p':
         return 0
   return 1

"""..................... Τελεστές Μετάβασης ....................."""

""" Τελεστής φαγώματος φρούτου """ 
def eat(state):
   if can_eat(state):
      for row in range(len(state)):
         for col in range(len(state[row])):
            if state[row][col][0] == 'p' and state[row][col][1] == 'f':  
               state[row][col][1] = ' '
               return state                
   else:
      return None

""" Τελεστής μετακίνησης προς τα δεξιά """ 
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

""" Τελεστής μετακίνησης προς τα αριστερά """ 
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

""" Τελεστής μετακίνησης προς τα πάνω """ 
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

""" Τελεστής μετακίνησης προς τα κάτω """ 
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

"""..................... Αλγόριθμοι αναζήτησης DFS και BFS ....................."""

""" Έλεγχος εύρεσης τελικής κατάστασης """
def is_goal_state(state):
   for row in range(len(state)):
      for col in range(len(state[row])):
         if state[row][col][1] == 'f':
            return 0
   return 1

""" Αρχικοποίηση του μετώπου αναζήτησης """
def make_front(state):
   return [state]

""" Αρχικοποίηση της ουράς αναζήτησης """
def make_queue(state):
    return [[state]]

""" Συνάρτηση εύρεσης μονοπατιού που οδηγεί από την αρχική κατάσταση στην τελική μέσω των αλγορίθμων αναζήτησης DFS ή BFS """
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
               print(queue[0][i][j])               # Οι κόμβοι-καταστάσεις στο τελικό μονοπάτι απεικονίζονται δισδιάστατα και ο ένας κάτω από τον άλλον
            print (' ')
   else:
      closed.append(front[0])
      front_copy = copy.deepcopy(front)
      front_children = expand_front(front_copy, method)
      queue_copy = copy.deepcopy(queue)
      queue_children = extend_queue(queue_copy, method)
      closed_copy = copy.deepcopy(closed)
      find_solution(front_children, queue_children, closed_copy, goal, method)

""" Επέκταση του μετώπου αναζήτησης """
def expand_front(front, method):  
   if method == 'DFS':                         # Επέκταση του μετώπου αναζήτησης του αλγορίθμου αναζήτησης DFS
      if front:
         print("Front : ")
         for i in range(len(front)):
            for j in range(len(front[i])):
               print(front[i][j])              # Οι κόμβοι-καταστάσεις στο μέτωπο αναζήτησης απεικονίζονται δισδιάστατα και ο ένας κάτω από τον άλλον
            print (' ')
         print('_______________________________________')
         node = front.pop(0)                   # Αφαίρεση του πρώτου κόμβου-κατάσταση από το μέτωπο αναζήτησης
         for child in find_children(node):     # Εύρεση καταστάσεων-παιδιά του κόμβου που αφαιρέθηκε από το μέτωπο, μέσω της συνάρτησης find_children
            front.insert(0, child)             # Οι καταστάσεις-παιδιά του κόμβου που αφαιρέθηκε, τοποθετούνται σε δομή στοίβας (LIFO) στην αρχή του μετ΄΄ωπου αναζήτησης
   elif method == 'BFS':                       # Επέκταση του μετώπου αναζήτησης του αλγορίθμου αναζήτησης BFS    
      if front:
         print ("Front : ")
         for i in range(len(front)):
            for j in range(len(front[i])):
               print(front[i][j])              # Οι κόμβοι-καταστάσεις στο μέτωπο αναζήτησης απεικονίζονται δισδιάστατα και ο ένας κάτω από τον άλλον
            print(' ')
         print('_______________________________________')
         node = front.pop(0)                   # Αφαίρεση του πρώτου κόμβου-κατάσταση από το μέτωπο αναζήτησης
         for child in find_children(node):     # Εύρεση καταστάσεων-παιδιά του κόμβου που αφαιρέθηκε από το μέτωπο, μέσω της συνάρτησης find_children
            front.append(child)                # Οι καταστάσεις-παιδιά του κόμβου που αφαιρέθηκε, τοποθετούνται σε δομή ουράς (FIFO) στο τέλος του μετώπου αναζήτησης
            
   return front

""" Επέκταση της ουράς αναζήτησης """
def extend_queue(queue, method):
# Επέκταση της ουράς αναζήτησης του αλγορίθμου αναζήτησης DFS
   if method == 'DFS':                         
      print ("Queue : ")
      for i in range(len(queue)):
         for j in range(len(queue[i])):
            for w in range(len(queue[i][j])):
               print(queue[i][j][w])           # Οι κόμβοι-καταστάσεις στην ουρά αναζήτησης απεικονίζονται δισδιάστατα και ο ένας κάτω από τον άλλον 
            print (' ')                        # Ένα μονοπάτι είναι μία σειρά από κόμβους ο ένας κάτω από τον άλλον και τελειώνει στον κόμβο που εμφανίζεται πριν το μήνυμα "End of path"
         print ('------------ End of path ------------')
         print (' ')
      print('_______________________________________')
      node = queue.pop(0)                      # Αφαίρεση του πρώτου μονοπατιού από την ουρά αναζήτησης
      queue_copy = copy.deepcopy(queue)
      children = find_children(node[-1])       # Εύρεση καταστάσεων-παιδιά του κόμβου που βρισκόταν στο τέλος του μονοπατιού που αφαιρέθηκε από την ουρά, μέσω της κλήσης find_children
      for child in children:
         path = copy.deepcopy(node)
         path.append(child)                    # Οι καταστάσεις-παιδιά αποθηκεύονται στη λίστα path δημιουργώντας ένα νέο μονοπάτι με τερματισμό έναν κόμβο-παιδί του τελευταίου κόμβου που βρισκόταν στο μονοπάτι που αφαιρέθηκε από την ουρά 
         queue_copy.insert(0,path)             # Το μονοπάτι τοποθετείται σε δομή στοίβας (LIFO), στην αρχή της ουράς αναζήτησης
# Επέκταση της ουράς αναζήτησης του αλγορίθμου αναζήτησης BFS
   elif method == 'BFS':                       
      print ("Queue : ")
      for i in range(len(queue)):
         for j in range(len(queue[i])):
            for w in range(len(queue[i][j])):
               print(queue[i][j][w])           # Οι κόμβοι-καταστάσεις στην ουρά αναζήτησης απεικονίζονται δισδιάστατα και ο ένας κάτω από τον άλλον 
            print (' ')
         print ('------------ End of path ------------')
         print (' ')
      print('_______________________________________')
      node = queue.pop(0)                      # Αφαίρεση του πρώτου μονοπατιού από την ουρά αναζήτησης
      queue_copy = copy.deepcopy(queue)
      children = find_children(node[-1])       # Εύρεση καταστάσεων-παιδιά του κόμβου που βρισκόταν στο τέλος του μονοπατιού που αφαιρέθηκε από την ουρά, μέσω της κλήσης find_children
      for child in children:
         path = copy.deepcopy(node)
         path.append(child)                    # Οι καταστάσεις-παιδιά αποθηκεύονται στη λίστα path δημιουργώντας ένα νέο μονοπάτι με τερματισμό έναν κόμβο-παιδί του τελευταίου κόμβου που βρισκόταν στο μονοπάτι που αφαιρέθηκε από την ουρά 
         queue_copy.append(path)               # Το μονοπάτι τοποθετείται σε δομή ουράς (FIFO), στo τέλος της ουράς αναζήτησης
    
   return queue_copy

""" Συνάρτηση εύρεσης απογόνων μίας κατάστασης-κόμβος """
def find_children(state):
   children = []
   right_state = copy.deepcopy (state)       
   child_right = move_right (right_state)      # Εύρεση απογόνου-καταστάση με την οποία ο pacman μπορεί να μετακινηθεί προς τα δεξιά 
   left_state = copy.deepcopy (state) 
   child_left = move_left (left_state)         # Εύρεση απογόνου-καταστάση με την οποία ο pacman μπορεί να μετακινηθεί προς τα αριστερά 
   up_state = copy.deepcopy (state)
   child_up = move_up (up_state)               # Εύρεση απογόνου-καταστάση με την οποία ο pacman μπορεί να μετακινηθεί προς τα πάνω 
   down_state = copy.deepcopy (state)
   child_down = move_down (down_state)         # Εύρεση απογόνου-καταστάση με την οποία ο pacman μπορεί να μετακινηθεί προς τα κάτω
   eat_state = copy.deepcopy (state)
   child_eat = eat (eat_state)                 # Εύρεση απογόνου-καταστάση με την οποία ο pacman μπορεί να φάει φρούτο
   
   if not child_right == None:                 # Έλεγχος τυχόν εύρεσης απογόνου-κατάσταση με την οποία ο pacman μπορεί να μετακινηθεί προς τα δεξιά
      children.append(child_right)
   if not child_left == None:                  # Έλεγχος τυχόν εύρεσης απογόνου-κατάσταση με την οποία ο pacman μπορεί να μετακινηθεί προς τα αριστερά
      children.append(child_left)  
   if not child_up == None:                    # Έλεγχος τυχόν εύρεσης απογόνου-κατάσταση με την οποία ο pacman μπορεί να μετακινηθεί προς τα πάνω
      children.append(child_up)                  
   if not child_down == None:                  # Έλεγχος τυχόν εύρεσης απογόνου-κατάσταση με την οποία ο pacman μπορεί να μετακινηθεί προς τα κάτω
      children.append(child_down)    
   if not child_eat == None:                   # Έλεγχος τυχόν εύρεσης απογόνου-κατάσταση με την οποία ο pacman μπορεί να φάει φρούτο
      children.append(child_eat)

   return children
    
"""..................... Ο κόσμος του προβλήματος ....................."""

def main():
   # Αρχική και τελική κατάσταση του προβλήματος σε διαστάσεις 4x4 (προτιμάται ο DFS για κύριο αλγόριθμο αναζήτησης)
   
   init_state = [[[' ', 'f'], [' ', 'f'], [' ', ' '], [' ', 'f']], 
                 [[' ', ' '], [' ', ' '], ['p', ' '], [' ', 'f']], 
                 [[' ', ' '], [' ', 'f'], [' ', 'f'], [' ', ' ']], 
                 [[' ', 'f'], [' ', 'f'], [' ', 'f'], [' ', 'f']]]  

   goal_state = [[[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']], 
                 [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']], 
                 [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']], 
                 [[' ', ' '], [' ', ' '], [' ', ' '], ['p', ' ']]]   
   
   # Αρχική και τελική κατάσταση του προβλήματος για την περίπτωση που δεν μπορεί να βρεθεί λύση 
   """
   init_state = []
   
   goal_state = []
   """
   # Αρχική και τελική κατάσταση του προβλήματος για την περίπτωση που η τελική κατάσταση είναι η ίδια η αρχική 
   """ 
   init_state = [[[' ', ' '], ['p', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' ']]]
   
   goal_state = [[[' ', ' '], ['p', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' '],
                  [' ', ' '], [' ', ' '], [' ', ' ']]]
   """
   # Αρχική και τελική κατάσταση του προβλήματος σε διαστάσεις 2x2 (προτιμάται ο BFS για το Βήμα Δ)
   """
   init_state = [[[' ', 'f'], ['p', ' ']],
                 [[' ', 'f'], [' ', ' ']]]
   
   goal_state = [[[' ', ' '], [' ', ' ']],
                 [['p', ' '], [' ', ' ']]]
   """
   # Αρχική και τελική κατάσταση του προβλήματος σε διαστάσεις 2x2 (προτιμάται ο BFS για το Βήμα Δ)
   """
   init_state = [[[' ', ' '], [' ', 'f']],
                 [['p', ' '], [' ', 'f']]]
   
   goal_state = [[[' ', ' '], ['p', ' ']],
                 [[' ', ' '], [' ', ' ']]]
   """
   method = 'Blind searching algorithm'
   # Επιλογή ενός από τους δύο αλγόριθμους αναζήτησης DFS ή BFS για τον κύριο αλγόριθμο αναζήτησης επίλυσης του προβλήματος με τον pacman
   while method != 'DFS' and method != 'BFS':
      method = input('Choose between DFS and BFS as main blind searching algorithm : ')
   # Κλήση της find_solution για την εύρεση μονοπατιού που θα οδηγήσει από την προεπιλεγμένη αρχική στην τελική κατάσταση με βάση προεπιλεγμένο αλγόριθμο αναζήτησης
   print (' ')
   print ('Begin Searching...')
   print ('Searching algorithm :',method)
   print (' ')
   find_solution(make_front(init_state), make_queue(init_state), [], goal_state, method)

if __name__ == "__main__":
    main()