# util/helpers.py
def detect_threats(df):
    alerts = []

    for _, row in df.iterrows():
        message = str(row.get("message", "")).lower()
        if "failed login" in message or "unauthorized access" in message:
            alerts.append(row)

    return alerts
