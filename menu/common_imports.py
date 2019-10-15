#!/bin/usr/env python3
from menu import MainMenu
from menu import ConfigurationMenu
from menu import InjectMenu
from menu import TapMenu
from menu import RulesMenu

def MainMenuLoop():
    """Go back to the main menu"""
    MainMenu.MainMenu().cmdloop()
    
def perform_exit():
    """Exit the program"""
    print("Exiting NAU Tools! A system restart might be required.")
    exit(0)


