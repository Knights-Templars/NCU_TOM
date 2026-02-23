from django.shortcuts import render

# Create your views here.
from .alerce import fetch_alerce_alerts
from .models import BrokerTarget


def alerce_targets(request):

    fetch_alerce_alerts(top_n=20)
    targets = BrokerTarget.objects.order_by("-discovered_at")[:20]

    return render(request, "broker/alerce_targets.html", {"targets": targets})

