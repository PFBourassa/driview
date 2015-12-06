global errors
errors =[]

def add(drive, problem):
    new_error = {"Drive": drive, "Problem": problem}
    errors.append(new_error)

def print_all():
    for error in errors:
        print error["Drive"]
        print error["Problem"]

"""   
[{"Drive": "Drive A", "Problem": "missing"}, 
{"Drive": "Drive C", "Problem": "new"}]
"""