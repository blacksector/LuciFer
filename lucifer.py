from cmd import Cmd
from subprocess import call
import os, random

import tools

VERSION = '0.0.1'
BANNER = tools.bcolors.HEADER + """
     _                   ___
    | |   _  _  __  (_) | __|  __   _ _
    | |__| || |/ _| | | |  _|/ -_) | '_|
    |____|\_,_|\__| |_| |_|  \___| |_|

""" + tools.bcolors.ENDC

BANNER += """
    Name: Lucifer
    Version: """ + VERSION + """
    Description: Lucifer is an advanced and very useful tool
    for penetration testing and open source intelligence gathering.

    Enter 'list' to list all commands.
"""
BANNER += tools.bcolors.OKBLUE + """
    TIP: Type 'exit' inside of any tool to leave it. Most tools are in a loop
    so they will not exit until you explicitly ask it to.
""" + tools.bcolors.ENDC



class LucyPrompt(Cmd):

    if os.name == 'nt':
        call('cls', shell=True)
    else:
        call('clear', shell=True)

    prompt = 'lucifer> '
    intro = BANNER
    ruler = '-'

    MAIN_MENU_SELECTION = 0
    SECONDARY_MENU_SELECTION = 0

    def do_list(self, inp):
        print("Select something:")
        print("""
        1. Social Media
        2. Server Information
        3. Open Source Intelligence
        4. Data Scraping / Downloading
        5. Misc
        99. Exit to Main Menu
        """)

    def help_list(self):
        print("Lists all available commands and tools.")

    def do_exit(self, inp):
        print("See ya later ;)")
        return True

    def help_exit(self):
        print('Exit the application. Shorthand: x q')

    def do_add(self, inp):
        print("adding '{}'".format(inp))

    def help_add(self):
        print("Add a new entry to the system.")

    def default(self, inp):
        COMMANDS = ['list', 'exit', 'add']
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        elif inp == 'clear':
            if os.name == 'nt':
                call('cls', shell=True)
            else:
                call('clear', shell=True)
        elif inp.isdigit():
            selection = int(inp)
            if self.MAIN_MENU_SELECTION == 0:
                if selection in range(1, 6):
                    self.MAIN_MENU_SELECTION = selection

                    if selection == 1:
                        print("----- Social Media Tools -----")
                        print("1. Facebook ID")
                        print("2. Instagram ID")
                        print("3. Instagram Media ID Converter vice versa")
                        print("")
                    elif selection == 2:
                        print("----- Server Information Tools -----")
                        print("1. Domain Information (Registrar, Age, etc)")
                        print("2. MX Record look up (what sort of backend email service they are using)")
                        print("3. CMS / Server details look up")
                        print("4. SSH Connection checker")
                        print("5. Whois tool")
                        print("6. Traceroute tool")
                        print("7. Ping tool")
                        print("8. DNS look up")
                        print("")
                    elif selection == 3:
                        print("----- Open Source Intelligence Tools -----")
                        print("1. Search social medias for person")
                        print("2. Get details on IP Address")
                        print("3. Get data on weather conditions, recent headlines etc of a certain geo target")
                        print("4. Facebook account scraper")
                        print("5. Instagram account scraper")
                        print("6. Twitter account scraper")
                        print("")
                    elif selection == 4:
                        print("----- Data Scraping / Downloading Tools -----")
                        print("1. Proxy list generator")
                        print("2. Dork Scanner")
                        print("3. Download Instagram Feed")
                        print("4. Download VSCO Feed")
                        print("")
                    elif selection == 5:
                        print("----- Misc Tools -----")
                        print("1. MD5 Hash Cracker")
                        print("2. Credit Card Validator")
                        print("3. Random Profile Generator")
                        print("")
                else:
                    print("ERROR: Invalid range. Please select a number between 1 to 5.")
            elif selection == 99:
                self.MAIN_MENU_SELECTION = 0
                self.SECONDARY_MENU_SELECTION = 0
            else:
                if self.MAIN_MENU_SELECTION == 1:
                    if selection == 1:
                        tools.facebook().get_facebook_id()
                    else:
                        print("ERROR: Invalid range. Please select a number between 1 to 3.")
                elif self.MAIN_MENU_SELECTION == 5:
                    if selection == 2:
                        tools.algorithms().luhn()
                    else:
                        print("ERROR: Invalid range. Please select a number between 1 to 3.")

        else:
            from difflib import get_close_matches
            name = inp.lower()

            close_commands = get_close_matches(name, COMMANDS)

            if close_commands:
                print('ERROR: unknown command "'+name+'" - maybe you meant "'+close_commands[0]+'"')
            else:
                print('ERROR: unknown command "'+name+'"')

        # print("Default: {}".format(inp))

    do_l = do_list
    help_l = help_list
    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':

    LucyPrompt().cmdloop()
