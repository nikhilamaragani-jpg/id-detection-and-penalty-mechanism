# Project walkthrough — ID Detection & Penalty

## 60-second pitch

I modeled an ID compliance workflow: detection results feed a review-first rules engine that produces ALLOW / WARNING / REVIEW outcomes and logs every decision to SQLite. A small analytics module aggregates outcomes, confidence, and event volume. The design explores the academic theme of linking **detection** with **compliance** mechanisms while staying honest that sensing is simulated today.

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

## Questions

**Missing ID detections?** Route to manual review; do not infer wrongdoing or apply an automatic penalty.
**Privacy?** Minimize retention of ID/face images if extended to real cameras.  
**Prototype honesty?** The default detector explicitly reports unavailable; simulated scenarios demonstrate the workflow. Live CV models are future work.
