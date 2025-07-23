import jdatetime
from calendar import HTMLCalendar
from datetime import date

class JalaliCalendar(HTMLCalendar):
    def formatday(self, day, weekday):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            today = date.today()
            current_day = today.day
            current_month = today.month
            current_year = today.year

            cell_class = self.cssclasses[weekday]

            # بررسی اینکه آیا این روز، روز جاری است؟
            if (day == current_day):
                cell_class += " today"  # اضافه کردن کلاس today

            g_date = date(today.year, today.month, day)

            try:
                j_date = jdatetime.date.fromgregorian(date=g_date)
                j_day = j_date.day
                j_month = j_date.strftime('%B')
            except:
                j_day = '-'
                j_month = '-'

            return f"""
            <td class="{cell_class}">
                <div style="font-weight:bold;">{day}</div>
                <div style="font-size: 12px; color: #555;">{j_day} {j_month}</div>
            </td>
            """

