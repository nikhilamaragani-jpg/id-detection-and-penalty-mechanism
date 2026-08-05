# Project walkthrough — ID Detection & Penalty

## 60-second summary

I modeled an automated ID compliance workflow: detection results feed a rules engine that produces allow/warning/review/penalty-path decisions and logs every outcome to SQLite. The architecture is ready for real computer-vision modules later.

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

## Questions

**False positives?** Prefer warnings + human review before hard penalties.  
**Privacy?** Minimize retention of face/ID images; encrypt and restrict access if extended.  
**Prototype honesty?** Scenarios are simulated; live CV models are future work.
