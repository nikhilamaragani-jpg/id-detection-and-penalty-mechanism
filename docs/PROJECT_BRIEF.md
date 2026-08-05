# Project brief - ID Detection & Penalty

| Field | Detail |
|-------|--------|
| Type | B.Tech project / automation workflow |
| Author | Amaragani Nikhil Sai |
| Institution | SIIET (JNTUH) |
| Domain | ID verification, access control, automated decisioning |

## Goal

Separate concerns cleanly: **detection interface** → **policy rules** → **decision outcomes** → **audit evidence**. The design is ready for real computer-vision modules later without rewriting the decision layer.

## Prototype vs future

- **This repo:** multi-scenario simulation + rules engine + SQLite audit log.  
- **Future / full CV scope:** live OpenCV/YOLO models, camera loop, alert channels.  

Keep claims aligned with what `python src/main.py` actually runs.
