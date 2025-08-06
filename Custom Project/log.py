from datetime import datetime

current_time = datetime.now()

file_name = 'log.txt'
with open(file_name, 'a') as file:
    file.write(f"[{current_time.strftime("%Y-%M-%d %H-%M-%S")}] Test\n")