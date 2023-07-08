from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from django.utils import timezone

@csrf_exempt
@login_required(login_url="/courier/sign-in/")
def current_job_update_api(request,id):
    job = Job.objects.filter(
        id=id,
        courier = request.user.courier,
        status__in=[
            Job.PICKING_STATUS,
            Job.DELIVERING_STATUS
        ]
    ).last()

    if job.status == Job.PICKING_STATUS:
        job.pickup_photo = request.FILES['pickup_photo']
        job.pickuedup_at = timezone.now()
        job.status = Job.DELIVERING_STATUS
        job.save()

    return JsonResponse({
        "success": True
    })