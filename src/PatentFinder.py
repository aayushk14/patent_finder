#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import os
import os.path
import sys
import shutil
import time
import logging
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
parent_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)
sys.path.append(parent_dir)
from util.LogUtil import LogUtil
logging.getLogger("werkzeug").setLevel(logging.ERROR)
logUtil = LogUtil()

class PatentFinder:
    def __init__(self,filePath):
        self.patent_list = pd.read_excel(filePath)
        #print self.patent_list
        #self.patent_list.set_index("Wipro Ref #", inplace=True)
        self.patent_list_indexed = self.patent_list.set_index("Wipro Ref #", drop = False)
        print self.patent_list_indexed

    def stats(self):
        print self.patent_list.head()
        print"============================="
        print self.patent_list.columns
        print"============================="
        print self.patent_list['Wipro Ref #'][0]
        print"============================="
        #print self.patent_list.loc['LCR.CTO.001IN1']
        print self.patent_list_indexed.loc["LCR.CTO.002IN2", : ]
        print"============================="
        print self.patent_list_indexed.loc["LCR.CTO.002IN2", "Comment"]

    def get_details(self, id):
        """
        method to find details for a given patent reference
        :param id: patent reference
        :return: string
        """
        try:
            #return self.patent_list_indexed.loc["LCR.CTO.002IN2", "Comment"]
            abc = self.patent_list_indexed.loc[id, : ]
            abc.to_json(orient='split')
            print "*********",abc,type(abc)
        except ZeroDivisionError:
            diff = 1


    def get_status(self, id):
        """
        method to find status for a given patent reference
        :param id: patent reference
        :return: string
        """
        try:
            #return self.patent_list_indexed.loc["LCR.CTO.002IN2", "Comment"]
            return self.patent_list_indexed.loc[id, "Comment"]
        except ZeroDivisionError:
            diff = 1



