# 🧾 Log Level Separator (Multithreading + Generators + Regex)

This project demonstrates how to **read and parse a large log file efficiently** using:

- ✅ Generators (for memory-efficient reading)
- ✅ Regular expressions (for parsing log structure)
- ✅ Multithreading (to parallelize writing logs by level)

---

## 📌 Features

- Reads log files line-by-line using a **Python generator**
- Uses **regex** to extract:
  - Log level (e.g., INFO, ERROR, WARNING)
  - Log message
  - Optional timestamp
- Spawns **separate threads** to write each log level into its own file
- Summarizes total logs processed and count per level
- Handles malformed lines gracefully

---

## 🧰 Modules Used

- `re` – for regex-based parsing  
- `threading` – to handle writing logs concurrently  
- `time` – to measure performance  
- `built-in file handling` – to read and write files  

---

## 💡 Learning Highlights
Regex skills for real-world log parsing
Threading concepts to handle multiple outputs in parallel
Generators for efficient file processing
Clean, readable Python code with error handling