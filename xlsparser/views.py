import datetime

from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from tablib import Dataset

from xlsparser.models import XlsRow
from xlsparser.resources import XlsRowResource


def xls_upload(request):
    if request.method == 'POST':
        row_resource = XlsRowResource()
        dataset = Dataset()
        new_rows = request.FILES['xlsfile']

        imported_data = dataset.load(new_rows.read())
        result = row_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            row_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'xlsparser/xls_upload.html')


def get_stat(request):
    date_today = datetime.date.today()
    if request.method == 'POST':
        date_from = request.POST.get('date_from',date_today)
        date_to = request.POST.get('date_to',date_today)
        stat = XlsRow.objects.filter(
            operdate_range=(date_from, date_to)
        ).aggregate(
            sum1=Sum('fact_qlig_data1'),
            sum2=Sum('fact_qlig_data2'),
            sum3=Sum('fact_qoil_data1'),
            sum4=Sum('fact_qoil_data2'),
            sum5=Sum('forecast_qlig_data1'),
            sum6=Sum('forecast_qlig_data2'),
            sum7=Sum('forecast_qoil_data1'),
            sum8=Sum('forecast_qoil_data2')
        ).values()
        return JsonResponse({'status': 'ok', 'sum': stat})
    else:
        return JsonResponse({'status': 'error'})

