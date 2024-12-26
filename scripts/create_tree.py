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
    
open("problems.json","w").write(json.dumps(problems))