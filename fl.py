def open_file():
  """
  This function ONLY serves to open a file, and does not take in parameters or
  returns anything.

  Parameters:
  - N/A

  Returns:
  - An opened file
  """
  f = open("/content/players_regular_season_career.txt", "r")
  return f
  # returns the opened file

def read_file():
    """
    This function serves to read data from the opened file and adds to a list.

    Parameters:
    - N/A

    Returns:
    - collection(list) , fname, lname
    """
    INFILE = open_file()
    i = 0
    collection = []  # created an empty list
    for line in INFILE:
        if i == 0:
            i += 1
            continue

        items = line.split("|")
        pts = float(items[6])
        reb = float(items[9])
        asts = float(items[10])
        stl = float(items[11])
        blk = float(items[12])
        fga = float(items[15])
        fgm = float(items[16])
        fta = float(items[17])
        ftm = float(items[-3])
        turnover = float(items[-8])
        gp = float(items[4])
        fname = items[1]
        lname = items[2]
        # Calculate efficiency
        efficiency = ((pts + reb + asts + stl + blk) - ((fga - fgm)) + ((fta - ftm)) + (turnover)) / gp
        collection.append([efficiency, fname, lname])
        i += 1


    return collection





def calculate_efficiency(pts, reb, asts, stl, blk, fga, fgm, fta, ftm, turnover, gp):

  """
   Calculates efficiency based on the given parameters.

    Parameters: pts,reb,asts,stl,blk,fga,fgm,fta,ftm,turnover,gp


    Returns:
     Calculated efficiency value
  """
    # Calculate efficiency
  efficiency = ((pts + reb + asts + stl + blk) - ((fga - fgm)) + ((fta - ftm)) + (turnover)) / gp
  return efficiency # Return efficiency


def writeOut_file(collection):
  """
  This function takes in a list named "collections" iterates through
  the first name, last name, and efficiency of the top 50 players.
  Moreover, we only want two columns s.t. the final output can look like:
    Wilt Chamberlain,52.60765550239235
    Artis Gilmore,45.42619047619048

  Parameters:
  - collection: A list that contains the first names, last names, and efficiencies
  for all the ~4K basketball players mentioned in the INFILE

  Returns:
  - top50.txt: the output file that contains the top 50 players
  """
  OUTFILE = open("top50.txt","w") # Open the OUTFILE for writing

  collection.sort()
  collection.reverse()

  top_boys = [] #created an empty list
  OUTFILE.write("FIRSTNAME LASTNAME EFFICIENCY \n")
  for i in range(50):
    #print(f'{collection[i][1]} {collection[i][2]}, {collection[i][0]}\n')
    OUTFILE.write(f'{collection[i][1]} {collection[i][2]}, {collection[i][0]}\n')
    top_boys.append(f'{collection[i][1]} {collection[i][2]}, {collection[i][0]}')






def print_finished():
  """
  Prints out a "Finished" when the output file is completed

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  print("Finished")

# collection = read_file() # Print "Finished" to indicate completion
# writeOut_file(collection)
# print_finished() # Call the function to print "Finished"










def open_file():
  """
   This  opens a file.

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  try:
    f = open("players_regular_season_career.txt", "r")
    return f
  except FileNotFoundError: # FileNotFoundError
    print("File not found")

def top_10_minutes():
  """
  Reads data from a file containing players' regular season career information,
    extracts the top 10 players with the highest minutes played, and writes their
    information to a new file 'top_10_minutes.txt'.

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  try:
    f = open("players_regular_season_career.txt","r")# opens the file
    i = 0
  except FileNotFoundError:
    print("file not found")
  player_min = []
  for line in f:
    if i == 0:
      i +=1
      continue
    items = line.split("|")
    fname = items[1]
    lname = items[2]
    minutes = items[5]
    player_min.append([int(minutes), fname, lname])

    player_min.sort()
    player_min.reverse()

  new_lst = [] #created empty list to store data
  player_min = player_min[:10]
  out = open("top_10_minutes","w") #opened the file for writing
  my_dict = {}
  out.write("ID FIRSTNAME LASTNAME MINUTES \n")
  for i in player_min:
    new_lst.append(i)
    char = i[2][:2] + i[1][:3]
    if not char in my_dict:
      my_dict[char] = 1
    else:
      my_dict[char] += 1
    out.write(f"{ char + str(my_dict[char]) },{i[1]},{i[2]},{i[0]}\n")

  return f"{new_lst[0][1]} {new_lst[0][2]} played {new_lst[0][0]} minutes (most minutes)."

def top_10_games():
  """
   Reads data from a file containing players' regular season career information,
    extracts the top 10 players with the most games played, and writes their
    information to a new file 'top_10_games.txt'.

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  try:
    f = open_file() # opens the file
    i = 0
    player_game= []
    for line in f:
      collection = []
      if i == 0:
        i +=1
        continue
      items = line.split("|")
      fname = items[1]
      lname = items[2]
      game = items[4]
      player_game.append([int(game), fname, lname])

      player_game.sort()
      player_game.reverse()

    new_lst = []
    player_game= player_game[:10]
    IN = open("top_10_games","w")
    my_dict = {} #created empty dict
    IN.write("ID FIRSTNAME LASTNAME GAMES \n")
    for i in player_game:
      new_lst.append(i)
      char = i[2][:2] + i[1][:3]
      if not char in my_dict:
        my_dict[char] = 1
      else:
        my_dict[char] += 1
      IN.write(f"{ char + str(my_dict[char]) },{i[1]},{i[2]},{i[0]}\n")
    return f"{new_lst[0][1]} {new_lst[0][2]} played {new_lst[0][0]} games (most games)."
  except IndentationError as e:
    print(f"Error {e}")

def top_10_points():
  """
  Reads data from a file containing players' regular season career information,
    extracts the top 10 players with the highest points scored, and writes their
    information to a new file 'top_10_points.txt'.

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  f = open("players_regular_season_career.txt","r")
  i = 0
  player_points = [] #created an empty list
  for line in f:

    if i == 0:
      i +=1
      continue
    items = line.split("|")
    fname = items[1]
    lname = items[2]
    points = items[6]
    player_points.append([int(points), fname, lname])

    player_points.sort()
    player_points.reverse()


  new_lst = []
  player_points = player_points[:10]
  fav = open("top_10_points","w")
  try :
    my_dict = {}  # created an empty dictionary
    fav.write(f"ID FIRSTNAME LASTNAME POINTS \n")
    for i in player_points:

            new_lst.append(i)
            char = i[2][:2] + i[1][:3]
            if not char in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
            fav.write(f"{char + str(my_dict[char])}, {i[1]}, {i[2]}, {i[0]}\n")
  except KeyError as e:
        print(f"Error: {e}")

  return f"{new_lst[0][1]} {new_lst[0][2]} played {new_lst[0][0]} points (most points)."

def top_10_rebound():
  """
    Reads data from a file containing players' regular season career information,
    extracts the top 10 players with the most rebounds, and writes their
    information to a new file 'top_10_rebound.txt'.



  Parameters:
  - N/A

  Returns:
  - N/A
  """
  f = open("players_regular_season_career.txt", "r") # opened the file
  i = 0
  player_reb = []
  for line in f:

    if i == 0:
      i +=1
      continue
    items = line.split("|")
    fname = items[1]
    lname = items[2]
    reb = items[-12]
    player_reb.append([int(reb), fname, lname])
  try:
    player_reb.sort()
    player_reb.reverse()
  except AttributeError as e:
    print(f"Error: {e}")
  new_lst = [] #empty list
  player_reb = player_reb[:10]
  jjk = open("top_10_rebounds","w")
  my_dict = {}
  jjk.write(f"ID FIRSTNAME LASTNAME REBOUNDS \n")
  for i in player_reb:
    new_lst.append(i)
    char = i[2][:2] + i[1][:3] #slicing
    if not char in my_dict:
      my_dict[char] = 1
    else:
      my_dict[char] += 1
    jjk.write(f"{ char + str(my_dict[char]) },{i[1]},{i[2]},{i[0]}\n")

  return f"{new_lst[0][1]} {new_lst[0][2]} played {new_lst[0][0]} rebounds (most rebounds)."

def top_10_pen():
  """
   Reads data from a file containing players' regular season career information,
    extracts the top 10 players with the most penalties, and writes their
    information to a new file 'top_10_pen.txt
  .

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  f = open("players_regular_season_career.txt", "r")
  i = 0
  player_pen = []
  for line in f:

    if i == 0: # skips header line
      i +=1
      continue
    items = line.split("|")
    fname = items[1]
    lname = items[2]
    pen = items[-7]  # specify index of penalties
    player_pen.append([int(pen), fname, lname])

    player_pen.sort()
    player_pen.reverse()

  new_lst = []
  player_pen = player_pen[:10]
  jjk = open("top_10_penalties","w")
  my_dict = {}
  jjk.write(f" ID FIRSTNAME LASTNAME PENALTIES \n")
  try:
    for i in player_pen:
      new_lst.append(i)
      char = i[2][:2] + i[1][:3]
  except IndexError as e:
    print(f"Error {e}")
    if not char in my_dict:
      my_dict[char] = 1
    else:
      my_dict[char] += 1
    jjk.write(f"{ char + str(my_dict[char]) },{i[1]},{i[2]},{i[0]}\n")

  return f"{new_lst[0][1]} {new_lst[0][2]} played {new_lst[0][0]} penalties (most penalties)."

def top_10_free():
  """
  Reads data from a file containing players' regular season career information,
    extracts the top 10 players with the most free throws made, and writes their
    information to a new file 'top_10_free.txt'.

  Parameters:
  - N/A

  Returns:
  - N/A
  """
  try:
    f = open_file()
  except FileNotFoundError as e:
    print(f'Error : {e}')
  i = 0
  player_free = []
  for line in f:

    if i == 0: #skips header line
      i +=1
      continue
    items = line.split("|")
    fname = items[1]
    lname = items[2]
    free = items[-3]
    player_free.append([int(free), fname, lname])

    player_free.sort() # use  the sort method
    player_free.reverse()


  new_lst = []
  player_free = player_free[:10]
  jjk = open("top_10_freethrows","w")
  my_dict = {}
  jjk.write("ID FIRSTNAME LASTNAME FREETHROWS \n")
  for i in player_free:
    new_lst.append(i)
    char = i[2][:2] + i[1][:3]
    if not char in my_dict:
      my_dict[char] = 1
    else:
      my_dict[char] += 1
    jjk.write(f"{ char + str(my_dict[char]) },{i[1]},{i[2]},{i[0]}\n")

  return f"{new_lst[0][1]} {new_lst[0][2]} played {new_lst[0][0]} freethrows (most freethrows)."


def best(x, y, c, f, q, n):
  """
    Writes the results of  top 10 functions to a file named 'le_goats.txt'.

    Args:
        x (str): Result of top_10_minutes function.
        y (str): Result of top_10_games function.
        c (str): Result of top_10_points function.
        f (str): Result of top_10_rebound function.
        q (str): Result of top_10_pen function.
        n (str): Result of top_10_free function.
  """
    # Open the output file in write mode
  with open("le_goats.txt", "w") as OUTFILE:
        # Write the results of each function to the file
        OUTFILE.write(f"{x} (most minutes).\n")
        OUTFILE.write(f"{y} (most games). \n")
        OUTFILE.write(f"{c} (most points).\n")
        OUTFILE.write(f"{f} (most rebounds).\n")
        OUTFILE.write(f"{q} (most penalties). \n")
        OUTFILE.write(f"{n} (most freethrows).\n")
  try:
 #Calls the best() function with results of various top 10 functions
    best(x, y, c, f, q, n)
  except Exception as e:
    print(f"Error ")


def do_everything():

  collection = read_file()
  writeOut_file(collection)
  print_finished()

  x = top_10_minutes()
  y = top_10_games()
  c = top_10_points()
  f = top_10_rebound()
  q = top_10_pen()
  n = top_10_free()
  best(x, y, c, f, q, n)

#do_everything()




