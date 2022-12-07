import pathlib

file_path = pathlib.Path("Days/day6/input.txt")

file = open(file_path, "r")
data_buffer = file.readline()
file.close()

total_start_packet_marker = 0
for i in range(0, len(data_buffer)):
    if i + 4 > len(data_buffer):
        break
    characters = set(str(data_buffer[i: i + 4]))
    
    if (len(characters) == 4):
        total_start_packet_marker = i + 4
        break
print(total_start_packet_marker)

total_start_message_marker = 0

for i in range(0, len(data_buffer)):
    if i + 14 > len(data_buffer):
        break
    characters = set(str(data_buffer[i: i + 14]))
    
    if (len(characters) == 14):
        total_start_message_marker = i + 14
        break

print(total_start_message_marker)
