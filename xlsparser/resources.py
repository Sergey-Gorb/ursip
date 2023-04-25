from import_export import resources
from .models import XlsRow
from datetime import date
import random


class XlsRowResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        dt = date.today()
        try:
            row['operdate'] = f'{dt.year}-{dt.month}-{int(random.random()*30)}'
        except Exception as e:
            print(e)

        return

    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        pass

    def skip_row(self, instance, original):
        return False

    class Meta:
        model = XlsRow
        fields = ('rowid', 'company',
                'fact_qlig_data1', 'fact_qlig_data2', 'fact_qoil_data1', 'fact_qoil_data2',
                'forecast_qlig_data1', 'forecast_qlig_data2', 'forecast_qoil_data1', 'forecast_qoil_data2',
                )

