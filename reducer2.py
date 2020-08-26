import sys

performance = {}

for line in sys.stdin:
    line = line.strip()
    origin, taxi_out, dest, taxi_in = line.split('\t', 3)

    if taxi_out.isdigit():
        performance[origin] = performance.get(origin, [[0,0], [0,0]])
        performance[origin][0][1] += 1
        performance[origin][0][0] += (int(taxi_out) - performance[origin][0][0]) / performance[origin][0][1]
    if taxi_in.isdigit():
        performance[dest] = performance.get(dest, [[0,0], [0,0]])
        performance[dest][1][1] += 1
        performance[dest][1][0] += (int(taxi_in) - performance[dest][1][0]) / performance[dest][1][1]

if len(performance) < 3:
    print("Less than 3 airports for which data was provided:")
    for key, value in performance.items():
        print(key, "average taxi out time:", value[0][0])
        print(key, "average taxi in time:", value[1][0])
else:
    s_taxi_out = sorted(performance.items(), key = lambda kv: kv[1][0][0])
    s_taxi_in = sorted(performance.items(), key = lambda kv: kv[1][1][0])

    # Low average taxi time is good
    # High average taxi time is bad
    print('Top 3 Airports by Average Taxi-In Time')
    for i in range(3):
        print(s_taxi_in[i][0], s_taxi_in[i][1][1][0])

    print('Top 3 Airports by Average Taxi-Out Time')
    for i in range(3):
        print(s_taxi_out[i][0], s_taxi_out[i][1][0][0])

    print('Bottom 3 Airports by Average Taxi-In Time')
    for i in range(1, 4):
        print(s_taxi_in[-i][0], s_taxi_in[-i][1][1][0])

    print('Bottom 3 Airports by Average Taxi-Out Time')
    for i in range(1, 4):
        print(s_taxi_out[-i][0], s_taxi_out[-i][1][0][0])