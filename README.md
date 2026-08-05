# ID Card Detection and Penalty Mechanism

**B.Tech Project** | Computer Vision | Automated Compliance | Security Workflow

A prototype that models ID card presence detection, decision rules, and automated penalty/logging workflows. The full project scope includes real-time camera capture, face detection, ID card localization, and alert mechanisms.

---

## Overview

Identification systems are critical for security and compliance. This project demonstrates:

1. Input analysis (image / detection result)
2. Detection outcome generation
3. Rule-based compliance decision (valid / missing / mismatch)
4. Penalty action modeling + SQLite logging for audit

**Status:** Runnable decision + logging prototype  
**Full Project Scope (from documentation):** Haar Cascade face detection, YOLOv5-style ID card detection, face recognition matching, and SMTP email alerts for violations

---

## System Architecture (Aligned with Project Report)

```text
Camera / Image Input
        |
        v
+---------------------------+
| Detection Module          |  Face + ID card presence (prototype / CV concept)
+---------------------------+
        |
        v
+---------------------------+
| Recognition / Matching    |  Identity verification logic
+---------------------------+
        |
        v
+---------------------------+
| Rules / Penalty Engine    |  Decision: warning / penalty / allow
+---------------------------+
        |
        v
+---------------------------+
| Logging + Alert Layer     |  SQLite audit + (concept) email notification
+---------------------------+
```

State-chart style flow from the report covers: initialize → capture → detect face/ID → recognize → decide → send alert if needed.

---

## Tech Stack

| Area              | Technology / Concept                     |
|-------------------|------------------------------------------|
| Language          | Python 3                                 |
| Vision Concepts   | OpenCV, Haar Cascade, YOLO-style detection |
| Decision Logic    | Rule engine                              |
| Storage           | SQLite                                   |
| Alerts (scope)    | SMTP / email notifications               |

---

## Project Structure

```text
id-detection-and-penalty-mechanism/
├── src/
│   ├── main.py         # Workflow entry
│   ├── detector.py     # Detection result simulation / interface
│   ├── rules.py        # Compliance & penalty rules
│   └── database.py     # SQLite decision logging
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/nikhilamaragani-jpg/id-detection-and-penalty-mechanism.git
cd id-detection-and-penalty-mechanism
pip install -r requirements.txt
python src/main.py
```

---

## Current Status vs Full Scope

- [x] Problem definition & workflow modeling
- [x] Detection result → rules → decision pipeline
- [x] SQLite logging of outcomes
- [ ] Real OpenCV / YOLOv5 model integration
- [ ] Live camera + face recognition pipeline
- [ ] SMTP alert implementation

---

## Author

**Amaragani Nikhil Sai**  
B.Tech in Computer Science and Engineering  
Sri Indu Institute of Engineering and Technology

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [Amaragani Nikhil Sai](https://linkedin.com/in/amaraganinikhilsai)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License
