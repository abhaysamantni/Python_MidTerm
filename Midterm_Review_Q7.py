def csv_reader_with_generator(file):
    result = []
    for row in file:
        result.append(row)
        yield result


import time

file = open("LargeCSVFile.csv", "r")
csv_gen = csv_reader_with_generator(file)
row_count = 0
start_time = time.perf_counter_ns()
for row in csv_gen:
    row_count += 1
total_time = time.perf_counter_ns() - start_time
print(f"Row count is {row_count}")
print(total_time / 1e9)
file.close()