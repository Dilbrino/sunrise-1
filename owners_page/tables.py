import django_tables2 as tables
from .models import Car

DEL_car = """<a href="{% url 'delete_car' record.pk %}">del</a>
"""
EDIT_car = """<a href="{% url 'edit_car' record.pk %}">edit</a>
"""


class carTable(tables.Table):
    edit = tables.TemplateColumn(verbose_name="edit", template_code=EDIT_car, empty_values=())
    delete = tables.TemplateColumn(verbose_name="delete", template_code=DEL_car, empty_values=())

    class Meta:
        model = Car
        fields = ['car_name', 'car_model', 'car_seats', 'gearbox', 'date_added', 'extra_info', 'available_car']
        template_name = "django_tables2/bootstrap4.html"
        orderable = True
