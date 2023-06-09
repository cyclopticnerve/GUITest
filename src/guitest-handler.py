# ------------------------------------------------------------------------------
# Project : GUITest                                                /          \
# Filename: guitest-handler.py                                    |     ()     |
# Date    : 05/12/2023                                            |            |
# Author  : cyclopticnerve                                        |   \____/   |
# License : WTFPLv2                                                \          /
# ------------------------------------------------------------------------------

# TODO: flesh this out more once we use it for a gui app
# this is a hot mess
# what level indenting???

# TODO: init controls in window
# TODO: set handler to class?

# TODO: move handler class to separate file
#     how to avoid circular imports?

# TODO: check for gtk version 3/4
#   does gi.repository have a >= ?
#   load ui file based on installed GTK version

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # noqa: E402 (import not at top of file)

# ------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------

# this is the dir where the script is being run from
# # (e.g. ~/Documents/Projects/Python/Apps/GUITest)
DIR_CURR = os.path.dirname(__file__)

# ------------------------------------------------------------------------------
# Globals
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Class
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# The main class of the program
# ------------------------------------------------------------------------------
class GUITestApp(Gtk.Application):
    """
        The main class of the program

        A class that extends Gtk.APplication to provide a GUI for the calling
        python script.
    """

    # --------------------------------------------------------------------------
    # Public methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Called when the main window is shown
    # --------------------------------------------------------------------------
    def on_activate(self, app):
        """
            Called when the main window is shown

            Parameters:
                self [Class]: the Class object
                app [Gtk.Application]: the Application object

            The Application is about to show the Window.
        """

        path_gui = os.path.join(DIR_CURR, 'guitest-gtk3.ui')

        # load file from abs path
        builder = Gtk.Builder()
        builder.add_from_file(path_gui)
        builder.connect_signals(self)

        # show window
        winMain = builder.get_object('guitest.winMain')
        self.add_window(winMain)
        winMain.present()

    # --------------------------------------------------------------------------
    # Called when a button is clicked
    # --------------------------------------------------------------------------
    def clicked(self, obj):
        """
            Called when a button is clicked

            Parameters:
                self [Class]: the __PP_NAME_BIG_App class object
                obj [object]: the Gtk object that was clicked

            The GTK object was clicked (probably a button).
        """
        print('click')

    # --------------------------------------------------------------------------
    # Private methods
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # Initialize the class to an object/instance
    # --------------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
            Initialize the class to an object/instance

            Parameters:
                self [Class]: the __PP_NAME_BIG_App class object
                **kwargs [dict]: the dict of parameters passes to the __init__
                function

            This method is called when a new instance of the class is created.
        """

        # always call super
        super().__init__(**kwargs)

        # connect default operations
        self.connect('activate', self.on_activate)


# # show the window
# gui = GUITestApp()
# gui.run()
