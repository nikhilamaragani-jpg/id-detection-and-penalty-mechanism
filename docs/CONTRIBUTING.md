# Contributing

## Setup
```bash
pip install -r requirements.txt
python src/main.py
pytest -q
```

## Modules
- `detector.py` — explicit unavailable result until a real model is integrated
- `rules.py` — validated, review-first compliance decisions
- `database.py` — SQLite audit log
- `analytics.py` — aggregate audit metrics
- `main.py` — synthetic workflow demo

See [the data dictionary](DATA_DICTIONARY.md) for audit-field and metric definitions. Keep test fixtures synthetic; do not commit ID images or personally identifying data.
