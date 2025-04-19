
N, L, S = map(int, input().split())
taxi_positions = {}  

for _ in range(N):

    command = input().split()

    if command[0] == "TAXI":
        timestamp, taxi_id, position = int(command[1]), command[2], int(command[3])
        taxi_positions[taxi_id] = (position, timestamp)

    elif command[0] == "ORDER":
        timestamp, order_id, order_position, order_time = int(command[1]), command[2], int(command[3]), int(command[4])
        
        suitable_taxis = []
        for taxi_id, (position, taxi_timestamp) in taxi_positions.items():
            delta_time = timestamp - taxi_timestamp
            max_position = (position + S * delta_time) % L
            min_position = position
            
            min_dist = (order_position - max_position + L) % L
            max_dist = (order_position - min_position + L) % L
            
            if max(min_dist, max_dist) <= S * order_time:
                suitable_taxis.append(taxi_id)
                
        if suitable_taxis:
            print(" ".join(suitable_taxis[:5]))
        else:
            print(-1)
