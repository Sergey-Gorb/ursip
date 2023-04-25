import datetime
from django.db import models


class XlsRow(models.Model):

    rowID = models.PositiveBigIntegerField()
    company = models.CharField(max_length=100)
    fact_qlig_data1 = models.IntegerField()
    fact_qlig_data2 = models.IntegerField()
    fact_qoil_data1 = models.IntegerField()
    fact_qoil_data2 = models.IntegerField()
    forecast_qlig_data1 = models.IntegerField()
    forecast_qlig_data2 = models.IntegerField()
    forecast_qoil_data1 = models.IntegerField()
    forecast_qoil_data2 = models.IntegerField()
    #operdate = models.DateField(default=datetime.date.today)
    operdate = models.DateField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.rowID, self.company)


