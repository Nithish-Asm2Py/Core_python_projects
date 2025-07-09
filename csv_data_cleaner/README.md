# 🧹 CSV Data Cleaner

The **CSV Data Cleaner** is a simple Python utility that reads a `.csv` file, removes rows with missing values, trims extra spaces, and lowercases the headers. 

---

## 📌 Features

- Reads input `.csv` file
- Strips whitespace from headers and data cells
- Converts all headers to lowercase
- Removes rows with **any missing/blank fields**
- Saves the cleaned data to a new `.csv` file

## Sample Input :

Name , Age , Email
Nithish Kumar , 23 , Nithish@example.com
  ,43,
alex, ,alex@email.com

## Sample Output :

name,age,email
Nithish Kumar,23,Nithish@example.com

🔧 Tech Stack
Python 3
csv module (built-in)

🎯 Why This Project?
Dataset cleaning is essential before feeding data into ML models.
This project simulates part of an ETL (Extract, Transform, Load) pipeline.
You’ll use this type of logic again when working with pandas, NumPy, or sklearn later.

🙋‍♂️ Author
Nithish Kumar
Documenting my journey to AI Engineering through hands-on Python projects.


