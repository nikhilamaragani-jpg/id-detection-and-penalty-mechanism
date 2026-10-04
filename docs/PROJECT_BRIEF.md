# Project brief — ID Detection & Penalty

| Field | Detail |
|-------|--------|
| Type | B.Tech project / automation workflow portfolio |
| Author | Amaragani Nikhil Sai |
| Domain | ID verification, access control, automated decisioning |
| Stack | Python, rules engine, SQLite, Docker |

## Goal

Separate **detection interface**, **policy rules**, **audit evidence**, and **operational analytics** so real computer-vision modules can plug in later without rewriting decision logic.

## Prototype vs future

- **Repo:** simulated scenarios, explicit unavailable-detector state, confidence validation, review-first rules, SQLite audit log, and aggregate metrics.
- **Safety boundary:** a missing, uncertain, or unavailable ID detection is sent to human review; the prototype never applies a penalty automatically.
- **Future:** validated OpenCV/YOLO integration, camera loop, richer alert channels, and privacy/retention controls.
