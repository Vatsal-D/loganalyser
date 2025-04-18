# parser/log_parser.py

def parse_log_file(file_content):
    logs = []
    lines = file_content.splitlines()
    for line in lines:
        parts = line.strip().split(" ", 3)
        if len(parts) == 4:
            timestamp, level, source, message = parts
            logs.append({
                "timestamp": timestamp,
                "level": level,
                "source": source,
                "message": message
            })
    return logs
