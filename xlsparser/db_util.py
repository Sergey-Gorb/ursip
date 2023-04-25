from django.db import connection


class DbWriter():
    def __init__(self, dbname='default'):
        self.db_name = dbname

    def bulk_xmlrow_variables(self, xmlrows):
        items = []
        for row in xmlrows:
            sb2 = self.subject2 and (
                MailingEmail.AB_SUBJECT_1 if email in subj1_half else MailingEmail.AB_SUBJECT_2
            ) or MailingEmail.AB_SUBJECT_NOT_USED
            items.append([self.mailing_id, email.pk, email.value, MailingEmail.STATE_INITIAL, sb2])
        with connection[self.db_name].cursor() as cursor:
            cursor.executemany(
                'INSERT INTO xmlrow (rowid, company, '
                'fact_qlig_data1, fact_qlig_data2, fact_qoil_data1, fact_qoil_data2, '
                '"forecast_qlig_data1, forecast_qlig_data2, forecast_qoil_data1, forecast_qoil_data2, operdate) '
                ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                items
            )

        conn.commit()
