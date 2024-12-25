import os, json

problem_mds = os.listdir("./problems")

print(problem_mds)

problems = {"problems":problem_mds}
open("problems.json","w").write(json.dumps(problems))