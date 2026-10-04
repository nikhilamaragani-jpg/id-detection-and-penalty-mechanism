# Demo

```bash
pip install -r requirements.txt
python src/main.py
```

Walk through simulated ALLOW / WARNING / REVIEW outcomes and SQLite logging. The default detector reports unavailable because no image model is configured; all negative, uncertain, or unavailable results require manual review. No real image analysis or automatic penalty is performed.

The audit database is `data/detections.db` by default. Set `ID_DETECTION_DB_PATH` to redirect it. Each demo run appends four synthetic events and prints aggregate counts, mean confidence, and daily event volume from the local audit log.

Run the test suite with `pytest -q`. It covers policy thresholds, invalid confidence values, review-first handling, database persistence, and analytics.
