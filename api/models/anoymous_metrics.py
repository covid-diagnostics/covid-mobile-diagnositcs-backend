from django.db import models


class Lightnings:
    DARK_ROOM = "dark room"
    NATURAL = "natural"
    LAMP = "lamp"


class MeasurementMethods:
    PHONE_ON_THE_MEASURING_HAND = "PHONE_ON_THE_MEASURING_HAND"
    PHONE_ON_THE_OTHER_HAND = "PHONE_ON_THE_OTHER_HAND"
    PHONE_ON_TABLE = "PHONE_ON_TABLE"


class AnonymousMetrics(models.Model):

    MEASUREMENT_METHODS = ((MeasurementMethods.PHONE_ON_THE_MEASURING_HAND, "phone on the measuring hand"),
                           (MeasurementMethods.PHONE_ON_THE_OTHER_HAND, "phone on the other hand"),
                           (MeasurementMethods.PHONE_ON_TABLE, "phone on the table"))
    LIGHTNING_OPTIONS = ((Lightnings.DARK_ROOM, "dark room"), (Lightnings.NATURAL, "natural"), (Lightnings.LAMP, "lamp"))

    filled_on = models.DateTimeField(auto_now_add=True)

    app_heart_rate = models.IntegerField(null=True, blank=True)
    device_heart_rate = models.IntegerField(null=True, blank=True)
    heart_rate_diff = models.IntegerField(null=True, blank=True)

    app_saturation = models.IntegerField(null=True, blank=True)
    device_saturation = models.IntegerField(null=True, blank=True)
    saturation_diff = models.IntegerField(null=True, blank=True)

    device_type = models.TextField(null=True, blank=True)

    measurement_method = models.TextField(choices=MEASUREMENT_METHODS)

    lightning = models.TextField(choices=LIGHTNING_OPTIONS)

    age = models.IntegerField(null=True, blank=True)

    past_medical_status = models.TextField(null=True, blank=True)

    face_recording = models.FileField(null=True, blank=True)
    chest_recording = models.FileField(null=True, blank=True)
    finger_video = models.FileField(null=True, blank=True)

    FILE_FIELDS = ["face_recording", "chest_recording", "finger_video"]

    def save(self):
        if self.device_heart_rate and self.app_heart_rate:
            self.heart_rate_diff = self.device_heart_rate - self.app_heart_rate
        if self.device_saturation and self.app_saturation:
            self.saturation_diff = self.device_saturation - self.app_saturation
        super(AnonymousMetrics, self).save()
