global errors
errors =[]

def add(drive, problem):
    new_error = {"Drive": drive, "Problem": problem}
    errors.append(new_error)

"""   
[{"Drive": "Drive A", "Problem": "missing"}, 
{"Drive": "Drive C", "Problem": "new"}]
"""