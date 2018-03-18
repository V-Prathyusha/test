import json

def recursion(children,dashcount):
    children=children["children"]
    for child in children:
       if child["selected"]==1:
           print("-"*dashcount+">"+child["name"])
           recursion(child,dashcount+5)
       
                           
mainfile=json.loads(open("foodyo_output.json", "r").read())
recommendations=(mainfile["body"]["Recommendations"])
for recommendation in recommendations:
   print(recommendation["RestaurantName"])
   menus=recommendation["menu"]
   for menu in menus:
       if menu["type"]=="sectionheader":
              children1=menu["children"]
              for child1 in children1:
                   if child1["type"]=="item" and child1["selected"]==1:
                        print("-->"+child1["name"])
                        recursion(child1,5)
                            
                                                 
       
