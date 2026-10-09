'''
find_conversion_factor() - calculates conversion factor from source -> target
convert() - calls find_conversion_factor() to get the conversion_factor. Then uses the conversion factor to return the final converted value

'''

from collections import deque


#function to calculate the conversion factor between source and target
def find_conversion_factor(conversion_graph, source, target):


   #1. Handle unknown units
   if source not in conversion_graph:
       raise ValueError(f"Unknown source :{source}")

   if target not in conversion_graph:
       raise ValueError(f"Unknow target: {target}")


   #2. Handle instances like meter -> meter
   if source == target:
       return 1.0

  
   #3. Find conversion factor starting from source using BFS
   queue = deque()
   queue.append((source, 1.0)) #(source, conversion factor of 1.0 as meter*1.0 = meter)


   discovered_unit = set() #maintain this to ensure we're not looking into the same unit again
   discovered_unit.add(source)


   while queue:
       
       current_unit, current_factor = queue.popleft()
       
       for neighbour, neighbour_factor in conversion_graph[current_unit].items():

           #Skip units that are already discovered
           if neighbour in discovered_unit:
               continue


           #Multiply conversion factor along the path
           new_factor = current_factor * neighbour_factor


           #If target is found return the accumulated factor
           if neighbour == target:
               return new_factor

           discovered_unit.add(neighbour)
           queue.append((neighbour, new_factor))


   raise ValueError(
       f"No conversion path found from {source} to {target}"
   )


#calculates final output
def convert(conversion_graph, quantity, source, target):

    conversion_factor = find_conversion_factor(conversion_graph, source, target) #call the function to calculate the conversion factor from source -> target

    return quantity * conversion_factor