from django.db import models
import uuid
# Create your models here.


class Record(models.Model):
    record_id = models.UUIDField(primary_key=True, null=False, editable=False, default=uuid.uuid4())
    record_progress = models.IntegerField(null=True)
    KDM = 1026
    DCP = 1027
    SPL = 1028
    PACK = 1029
    RAR = 1030
    TYPE_CHOICES = [
        (KDM, 'KDM'),
        (DCP, 'DCP'),
        (SPL, 'SPL'),
        (PACK, 'PACK'),
        (RAR, 'RAR'),
    ]
    record_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=KDM,
    )
    record_annotation = models.CharField(max_length=200, null=True)
    record_theatre = models.CharField(max_length=200, null=True)
    record_datetime = models.CharField(max_length=100, null=True)
    PENDING = -1
    QUEUED = 0
    IN_PROGRESS = 1
    IN_PROGRESS_POST = 2
    PAUSED = 3
    FINISHED = 4
    CANCELED = 5
    EXCEPTION = 6
    STATUS_CHOICE = [
        (PENDING, 'PENDING'),
        (QUEUED, 'QUEUED'),
        (IN_PROGRESS, 'IN_PROGRESS'),
        (IN_PROGRESS_POST, 'IN_PROGRESS_POST'),
        (PAUSED , 'PAUSED'),
        (FINISHED , 'FINISHED'),
        (CANCELED , 'CANCELED'),
        (EXCEPTION , 'EXCEPTION'),
    ]
    record_status = models.IntegerField(
        choices=STATUS_CHOICE,
        default=PENDING,
    )
    record_exception_messages = models.CharField(max_length=2000, null=True)

    class Meta:
        db_table = "record"

    def __str__(self):
        return self.record_id
