"""
Loads the csv file
Creates a conversion_graph that stores both forward and reverse conversion relationships.

eg: if the csv file has :
SourceUnit,TargetUnit,Factor
kg,g,1000

..our graph will store both:
Forward relationship : kg to g conversion factor = 1000
Reverse relationship : g to kg conversion factor = 1/1000
"""

import csv
import math

def load_csv(csv_file):


   conversion_graph = {}


   with open(csv_file, newline="") as f:
       reader = csv.DictReader(f) #read each row of the file as dict. Header is used as key


       for row in reader:


           '''each row looks similar to:
           {
               "SourceUnit": "meter",
               "TargetUnit": "feet",
               "Factor": "3.28084"
           }'''


           #Read every row in the csv file
           source = row["SourceUnit"].strip().lower()
           target = row["TargetUnit"].strip().lower()
           

           if not source:
               raise ValueError("Source unit cannot be empty")

           if not target:
              raise ValueError("Target unit cannot be empty")

           try:
              factor = float(row["Factor"]) #Convert string into float
           except (ValueError, TypeError):
               raise ValueError (f"Invalid conversion factor : {row['Factor']}")

           if not math.isfinite(factor) or factor == 0: #handles factor = nan, infinite and 0
               raise ValueError(f"Invalid Conversion factor: {source} -> {target} : {factor}")

           
           #Add conversion relationships

           if source not in conversion_graph:
               conversion_graph[source] = {}
           if target not in conversion_graph:
               conversion_graph[target] = {}


           #Add forward conversion relationship
           conversion_graph[source][target] = factor
           #Add backward conversion relationship
           conversion_graph[target][source] = 1 / factor           


   return conversion_graph
