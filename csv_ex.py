#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import csv

with open( "test.txt", "wt" ) as TRG:
	FMT = csv.writer( TRG )
	FMT.writerow( ["Tixon", codecs.encode("Егорченков"), 120] )
	FMT.writerow( ["Igor", "Marchuk", 110] )