from django.db import models

class CaseQuery(models.Model):
    # The user's query
    case_type = models.CharField(max_length=100)
    case_number = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    # The scraped results
    parties_names = models.TextField(blank=True, null=True)
    filing_date = models.CharField(max_length=20, blank=True, null=True)
    next_hearing_date = models.CharField(max_length=20, blank=True, null=True)
    case_status = models.CharField(max_length=100, blank=True, null=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    raw_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.case_type} {self.case_number}/{self.year}"