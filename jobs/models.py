from djongo import models

class Job(models.Model):
    position_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "python_jobs"  # Ensure Django looks at the correct collection

    def __str__(self):
        return self.position_name
