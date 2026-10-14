import traceback

# Task 1: Diary
try:
    with open("diary.txt", "a") as diary:
        line = input("What happened today? ")
        diary.write(line + "\n")
        while line != "done for now":
            line = input("What else? ")
            diary.write(line + "\n")
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
