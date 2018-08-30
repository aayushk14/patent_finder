# coding=utf-8
"""
Author : AA359290
Created on : 05/02/2017 12:51 PM
"""
import ConfigParser
import os


class ConfigReader(object):
    """
    Class to provide the configuration details
    """
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir,'config',
                                      'config.ini'))

    def getConfig(self, section, key):
        """
        Get value of a key in a section
        :param section:
        :param key
        :return:
        """
        return self.config.get(section, key)
