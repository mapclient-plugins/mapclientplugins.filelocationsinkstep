
"""
MAP Client Plugin
"""

__version__ = '0.3.0'
__author__ = 'Richard Christie'
__stepname__ = 'File Location Sink'
__location__ = 'https://github.com/mapclient-plugins/mapclientplugins.filelocationsinkstep'

# import class that derives itself from the step mountpoint.
from mapclientplugins.filelocationsinkstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
