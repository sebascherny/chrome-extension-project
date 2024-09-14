from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserEvent
from .hardcoded_content import NOTIFICATION_CONTENT


@csrf_exempt
def get_notification(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            url = data.get("url")
            domain = url.split("/")[2] if url else None
            if domain in NOTIFICATION_CONTENT:
                return HttpResponse(NOTIFICATION_CONTENT[domain], content_type="text/html")
            else:
                return HttpResponse(
                    "<div>No notifications available for this site.</div>",
                    content_type="text/html",
                )
        except (KeyError, json.JSONDecodeError) as e:
            return HttpResponse("<div>Error processing request.</div>", status=400)
    return HttpResponse(status=405)  # Method not allowed


@csrf_exempt
def log_event(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            action = data.get("action")
            url = data.get("url")
            comment = data.get("comment")

            # Log the event in the database
            if action and url:
                UserEvent.objects.create(event_type=action, url=url, comment=comment)
                return JsonResponse(
                    {"status": "success", "message": "Event logged successfully"},
                    status=200,
                )
            else:
                return JsonResponse(
                    {"status": "error", "message": "Invalid data"}, status=400
                )
        except (KeyError, json.JSONDecodeError) as e:
            return JsonResponse(
                {"status": "error", "message": "Error processing request"}, status=400
            )
    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=405
    )
