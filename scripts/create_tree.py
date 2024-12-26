import os, json

problem_mds = os.listdir("./problems")

print(problem_mds)

problems = {"problems":[]}
for problem in problem_mds:
    meta_text = open(f"./problems/{problem}","r").read().split("<metadata>")[1].split("</metadata>")[0]
    print(meta_text)
    meta = json.loads(meta_text)
    meta["categories"].sort()
    problems["problems"].append({problem:meta})
# Function to convert date string to a tuple (year, month, day) 
def date_key(problem): 
    for key, value in problem.items(): 
        day, month, year = map(int, value["created"].split("/")) 
        return (year, month, day) # Sorting the problems list by the created date
    
problems["problems"] = sorted(problems["problems"], key=date_key,reverse=True)

    
open("problems.json","w").write(json.dumps(problems))