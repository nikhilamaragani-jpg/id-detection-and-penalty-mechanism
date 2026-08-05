# ID Card Detection and Penalty Mechanism

**B.Tech Project** | Computer Vision | Compliance Automation Concept

A prototype that demonstrates how ID detection results can be connected to simple compliance rules and stored in a database for review.

---

## Overview

This project models a basic workflow:

1. Analyze an input image reference
2. Produce a detection result
3. Apply a rule-based decision
4. Log the outcome in SQLite

**Project Type:** Academic Prototype  
**Status:** Runnable decision workflow with database logging

---

## Architecture

```text
Image Input (path/reference)
            |
            v
+--------------------+
| Detection Module   |  (prototype detection result)
+--------------------+
            |
            v
+--------------------+
| Rules Engine       |  (compliance / penalty decision)
+--------------------+
            |
            v
+--------------------+
| SQLite Database    |  (stores detection decisions)
+--------------------+
```

---

## Tech Stack

| Area | Technology |
|------|------------|
| Language | Python |
| Vision Concept | OpenCV-oriented design |
| Storage | SQLite |
| Tools | Git |

---

## Project Structure

```text
id-detection-and-penalty-mechanism/
├── README.md
├── requirements.txt
├── data/
├── src/
│   ├── main.py
│   ├── detector.py
│   ├── rules.py
│   └── database.py
└── LICENSE
```

---

## How to Run

```bash
git clone https://github.com/nikhilamaragani-jpg/id-detection-and-penalty-mechanism.git
cd id-detection-and-penalty-mechanism

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python src/main.py
```

---

## Current Status

- [x] Problem definition
- [x] Detection + rules workflow
- [x] SQLite decision logging
- [ ] Real OpenCV/YOLO model integration
- [ ] Image dataset demos

---

## Author

**Amaragani Nikhil Sai**  
B.Tech in Computer Science and Engineering

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [Amaragani Nikhil Sai](https://linkedin.com/in/amaraganinikhilsai)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License
