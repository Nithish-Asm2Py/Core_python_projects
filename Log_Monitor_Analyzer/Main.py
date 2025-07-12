import re
import threading
import time

# ✅ Generator: Reads file line-by-line (memory-efficient)
def log_reader(filepath):
    """
    Generator function to yield one log line at a time from the file.
    Efficient for large files since it avoids loading everything into memory.
    """
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                yield line

# ✅ Regex-based log parser
def parse_log(line):
    """
    Parses a single line using regex to extract:
    - log level (e.g., INFO, ERROR)
    - message
    - optional timestamp (e.g., 10:30 AM)
    Returns a dictionary or None if the line is malformed.
    """
    pattern = r"\[(\w+)\]\s+(.*?)(?:\sat\s([\d:]+\s*[APM]*))?$"
    match = re.match(pattern, line)
    if match:
        level = match.group(1)
        message = match.group(2)
        timestamp = match.group(3) if match.group(3) else "N/A"
        return {
            "level": level.upper(),
            "message": message,
            "time": timestamp
        }
    return None

# ✅ Thread worker function
def process_logs(logs, level, output_file):
    """
    Filters logs by level and writes them to a separate output file.
    Intended to run inside a thread for concurrent processing.
    """
    filtered = [log for log in logs if log['level'] == level]
    
    with open(output_file, 'w') as file:
        for log in filtered:
            file.write(f"[{log['level']}] {log['message']} at {log['time']}\n")
    
    print(f"✅ {level} logs written to {output_file} ({len(filtered)} entries)")

# ✅ Main function
def main():
    input_file = "sample1.log"
    start = time.perf_counter()  # Track start time

    print(f"📥 Reading log file: {input_file}")

    # Step 1: Read and parse logs using generator and regex
    raw_lines = log_reader(input_file)
    parsed_logs = [parse_log(line) for line in raw_lines]
    
    # Remove any malformed log lines
    parsed_logs = [log for log in parsed_logs if log is not None]

    # Step 2: Identify all unique log levels (e.g., INFO, ERROR, WARNING)
    levels = set(log['level'] for log in parsed_logs)

    # Step 3: Create and start a thread for each log level
    threads = []
    for level in levels:
        filename = f"{level.lower()}s.txt"  # Output file e.g., infos.txt
        t = threading.Thread(target=process_logs, args=(parsed_logs, level, filename))
        threads.append(t)
        t.start()

    # Step 4: Wait for all threads to finish
    for t in threads:
        t.join()
        print(f"🔁 Started thread for {level} | Thread name: {threading.current_thread().name}")

    end = time.perf_counter()  # Track end time

    # Step 5: Print log summary
    print("\n📊 Log Summary")
    print("-----------------------")
    print(f"Total lines processed: {len(parsed_logs)}")
    for level in sorted(levels):
        count = sum(1 for log in parsed_logs if log['level'] == level)
        print(f"[{level}] Count: {count}")
    print(f"\n⏱️ Total time taken: {end - start:.2f} seconds")

# ✅ Entry point
if __name__ == "__main__":
    main()
