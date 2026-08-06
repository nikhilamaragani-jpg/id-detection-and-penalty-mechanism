# Project walkthrough — ID Detection & Penalty

## 60-second pitch

I modeled an automated ID compliance workflow: detection results feed a rules engine that produces ALLOW / WARNING / REVIEW / PENALTY_PATH outcomes and logs every decision to SQLite. The design matches the academic theme of linking **detection** with **penalty / compliance** mechanisms, while the code stays honest about simulated sensing today.

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

## Questions

**False positives?** Prefer REVIEW / WARNING before hard penalties.  
**Privacy?** Minimize retention of ID/face images if extended to real cameras.  
**Prototype honesty?** Scenarios are simulated; live CV models are future work.
