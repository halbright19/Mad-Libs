from colored import fg, stylize
import stories
import random_words
import drawing
import time

def color_print(text, color):#prints desired text with chosen color
  print(stylize(str(text), fg(str(color))))

color_print("~~~~~~~~~~~~~~~~~~~~~~~~", "sky_blue_2")
color_print("| Welcome to Mad Libs! |", "dodger_blue_2")
color_print("~~~~~~~~~~~~~~~~~~~~~~~~", "sky_blue_2")
time.sleep(1)
y = 0   #used in main loop

while y == 0:
  i = 0   # used in 1st inner while loop
  x = 0   # used in 2nd inner while loop

  while i == 0: #this loop will allow us to ask the question again if the user inputs an invalid input
    color_print("Which story would you like to use?\n  1. Little Red Riding Hood\n  2. The Tortoise and the Hare\n  3. The Grasshopper and the Ant\n  4. Pick for me!\n(Please just put the number)", "light_cyan")
    choice = input()
    #The user will put in a number that coordinates with what story they want
    if choice == '1':
      story = stories.redRidingHood
      i += 1
    elif choice == '2':
      story = stories.tortAndHare
      i += 1
    elif choice == '3':
      story = stories.grasshopper_ants
      i += 1
    elif choice == '4':
      story = stories.ran_story() #the function to pick a random story is in our stories.py
      i += 1
    else:
      print('Sorry this is an invalid input, try again!\n ')
      #If no story is selected (not in the right format), the loop will restart. 
  
    if story == stories.redRidingHood:
      color = "deep_pink_2"
      draw = 1
    if story == stories.tortAndHare:
      color = "spring_green_1"
      draw = 2
    if story == stories.grasshopper_ants:
      color ="dark_orange_3a"
      draw = 3
    #this assigns a color to each of our stories and a number to draw pictures later

  decision = input('Would you like to create the story yourself or see a\nrandomly generated one? (random/original):\n')
  # random will allow the computer to just fill in adjectives and original will have the person do it manually

  while x == 0: #This allows us to fill in more words if the user misses them
    try: 
      a_count = 0
      v_count = 0
      n_count = 0
      pv_count = 0
      av_count = 0
      #We initialized the type of words as 0, so we could add to them

      for word in story.split():    
  #Splits our big story string by word and counts number of verbs, nouns, adjectives, etc. in our story (we had replaced those with out _a_ form).
        if word == '_a_':
          a_count += 1
        elif word == '_v_':
          v_count += 1
        elif word == '_n_':
          n_count += 1
        elif word == '_pv_':
          pv_count +=1
        elif word == '_av_':
          av_count += 1

        a = 0
        v = 0
        n = 0
        pv = 0
        av = 0
      #these variables are for choosing from the index of the list

      if a_count != 0: #will not ask if there is no adjectives to replace
        if decision == 'random': #if the input was random
          a_list = [] #need an empty list to add to
          for ran_adj in range(0, a_count + 1): #This range allows to have as many adjectives added, as are needed based on our count
            ran_adj = random_words.adjective() #takes a radom word, using the random word function from random_words.py
            a_list.append(ran_adj) 
            #adds the word to a_list which will be used to input into story
        if decision == 'original': #if the user input was not random
          adjectives = input('Enter {} adjectives as a comma-separated list (ex: happy, sad, mad, etc.):\n'.format(a_count))
          a_list = adjectives.split(', ')    
          #The user creates a string of words that is then split into a list
        while '_a_' in story:
          #when there is still an adjective in the story, the blank spot is replaced by a different word in the input list
          adj = a_list[a] 
          #picks an adjective from the list's index
          a += 1 
          #adds to the value of the index, so the next ajective will then be picked
          story = story.replace('_a_ ', adj, 1)
          #replaces that blank space

      #All the other word types follow that same format as adjectives!
      if v_count != 0:
        if decision == 'random':
          v_list = []
          for ran_vrb in range(0, v_count + 1):
            ran_vrb = random_words.verb()
            v_list.append(ran_vrb)
        if decision == 'original':
          verbs = input('Enter {} present tense verbs as a comma-separated list (ex: walk, run, jump, etc.):\n'.format(v_count))
          v_list = verbs.split(', ')
        while '_v_' in story:
          vrb = v_list[v]
          v += 1
          story = story.replace('_v_ ', vrb, 1)

      if av_count != 0:
        if decision == 'random':
          av_list = []
          for ran_adv in range(0, av_count + 1):
            ran_adv = random_words.ad_verb()
            av_list.append(ran_adv)
        if decision == 'original':
          adv = input('Enter {} adverbs as a comma-separated list (ex: boldly, lively, actually etc.):\n'.format(av_count))
          av_list = adv.split(', ')
        while '_av_' in story:
          adv = av_list[av]
          av += 1
          story = story.replace('_av_ ', adv, 1)

      if n_count != 0:
        if decision == 'random':
          n_list = []
          for ran_noun in range(0, n_count + 1):
            ran_noun = random_words.noun()
            n_list.append(ran_noun)
        if decision == 'original':
          nouns = input('Enter {} nouns as a comma-separated list (ex: market, cat, joke, etc.):\n'.format(n_count))
          n_list = nouns.split(', ')
        while '_n_' in story:
          noun = n_list[n]
          n += 1
          story = story.replace('_n_ ', noun, 1)

      if pv_count != 0: 
        if decision == 'random':
          pv_list = []
          for ran_pv in range(0, a_count + 1):
            ran_pv = random_words.p_verb()
            pv_list.append(ran_pv)
        if decision == 'original':
          p_verbs = input('Enter {} past tense verbs as a comma-separated list (ex: walked, ran, jumped, etc.):\n'.format(pv_count))
          pv_list = p_verbs.split(', ')
        while '_pv_' in story:
          pvrb = pv_list[pv]
          pv += 1
          story = story.replace('_pv_ ', pvrb, 1)

      x += 1
      #has us exit the loop when this is done

    except IndexError:
      x = 0
      #If there's not enough words which would cause an IndexError, the word count and replacement will run again so that the user can add the words that they forgot
  print("Generating your story...")
  time.sleep(1)
  color_print(story, color)
  #prints the story with our assigned color after 2 seconds
  
  #based on the number assigned above, this will run the function that prints different pictures at the end of each story
  if draw == 1:
    drawing.draw_red()
  if draw == 2:
    drawing.draw_hare()
  if draw == 3:
    drawing.draw_ant()

  new_story = input('Would you like to play again (Y/N)?\n')
  #gives the user an option to play again

  if new_story == 'Y':
    print('Awesome! Here we go!\n')
    #If they select yes it will stay in the main loop
  elif new_story == 'N':
    y += 1
    #If they select no it will exit the main loop
  else:
    print ("I'm sorry, I didn't understand that.\n")
    y += 1
    #If they don't put in yes, or no the program will end anyway

color_print('Goodbye!', "hot_pink_1b")