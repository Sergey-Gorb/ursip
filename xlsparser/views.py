from django.shortcuts import render
from tablib import Dataset

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
