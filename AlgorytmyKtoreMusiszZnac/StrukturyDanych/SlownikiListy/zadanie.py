a1 = { 
    "hour": "9:00", 
    "type": "lecture", 
    "topic": "Microbiology", 
    "teacher": "prof Virus" 
} 
 
a2 = { 
    "hour": "12:00", 
    "type": "lab", 
    "topic": "Chemistry", 
    "teacher": "prof Kolba" 
} 
 
a3 = { 
    "hour": "14:00", 
    "type": "lecture", 
    "topic": "Ethics", 
    "teacher": "prof Ojej" 
} 
 
plan_list = [a1, a2, a3] 
 
plan_dict = {} 
for position in plan_list: 
    plan_dict[position["topic"]] = position 
 
 
for position in plan_list: 
    print(f"{position['topic']} at {position['hour']}") 
 
 
for k,v in plan_dict.items(): 
    print(f"{v['topic']} at {v['hour']}")