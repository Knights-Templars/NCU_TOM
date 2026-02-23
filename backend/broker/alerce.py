import requests
from datetime import datetime

from .models import BrokerTarget

ALERCE_SEARCH_URL = 'https://api.alerce.online/ztf/v1/objects/'

def fetch_alerce_alerts(top_n=100):

    params = {"page_size": top_n,
        "page": 1,
        "sort": "-lastmjd",
        "classifier": "lc_classifier",
        "ndet": 5,
        "probability": 0.7,
        }
    
    response = requests.get(ALERCE_SEARCH_URL, params=params, timeout=30)

    data = response.json()
    alerts = []

    for obj in data.get("items", []):
        target = BrokerTarget(
            name = obj.get("oid"),
            ra=obj.get("meanra"),
            dec=obj.get("meandec"),
            magnitude=None,
            alert_id=obj.get("oid"),
            discovered_at=obj.get("lastmjd")
        )

        target.save()
        alerts.append(target)

    return alerts





