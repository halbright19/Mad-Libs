from colored import fg, stylize

#Here are the drawing functions for our story! Each function will draw an animal with a certain color
#We got them from https://www.asciiart.eu/

def draw_red():
  print(stylize("                    / V\ \n                  / `  /\n                 <<   |\n                 /    |\n               /      |\n             /        |\n           /    \  \ /\n          (      ) | |\n  ________|   _/_  | |\n<__________\______)\__)", fg("red_3b")))
#a wolf for red riding hood

def draw_hare():
  print(stylize("         ,\ \n         \\\\\\,_\n          \` ,\ \n     __,.-' =__)\n   .'        )\n,_/   ,    \/\_\n\_|    )_-\ \_-`\n   `-----` `--`", fg("dark_orange_3a")))
  print(stylize("               __\n   .,-;-;-,.  /'_\ \n  _/_/_/_|_\_\) /\n'-<_><_><_><_>=/\ \n  `/_/====/_/-'\_\ \n   ''     ''    ''", fg("green_4")))
  #a tortoise and hare

def draw_ant():
    print(stylize("/\/\ \n  \_\  _..._\n  ('')(_..._)\n   ^^  // \\\ \n", fg("grey_54")))
    print(stylize(" //_____ __ \n@ )====// .\___\n\#\_\__(_/_\\\_/\n   / /       \\\ \n", fg("spring_green_1")))
  #a grasshopper and ant
