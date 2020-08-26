import subprocess
import time

input_files = []
for i in range(1987, 2009):
    input_files.append('data_csv/' + str(i) + '.csv')
base_command = r'hadoop jar C:\hadoop\share\hadoop\tools\lib\hadoop-streaming-3.1.3.jar -mapper "python mapper{}.py" -reducer "python reducer{}.py" -file mapper{}.py -file reducer{}.py -input {} -output output{}'
runtimes_dict = {}
runtimes_list = []

for i in range(1, 23):
    for j in range(1, 4):
        command = base_command.format(j, j, j, j, ' '.join(input_files[0:i]), str(i) + str(j))
        t0 = time.perf_counter()
        p = subprocess.run(command, shell = True)
        t1 = time.perf_counter() - t0
        print(t1)
        if p.returncode == 1:
            print("There was an error!")
            print()
            print(runtimes_dict)
            print()
            print(runtimes_list)
            exit()
        runtimes_dict['1987-' + str(1986 + i) + ' J' + str(j)] = t1
        runtimes_list.append(t1)

for key, value in runtimes_dict.items():
    print(key, str(value) + "s")

print()
print(runtimes_dict)
print()
print(runtimes_list)

        