import django_tables2 as tables
from .models import Orders
from owners_page.models import Car

giveBack_car = """<a href="{% url 'giveBack_car' record.pk %}">giveBack</a>
"""


# EDIT_doctor="""<a href="{% url 'modifier_doctor' record.pk %}"><i class="fa fa-edit" style="margin-down : 33px; font-size: 21px;"></i></a>
# """

class OrdersTable(tables.Table):
    # modifier = tables.TemplateColumn( verbose_name="modifier", template_code=EDIT_doctor, empty_values=())#,'modifier_bc_achat', args=[A('pk')], empty_values=(),orderable=False, text='Edit', attrs={"td": {"align": "center"}})
    giveBack = tables.TemplateColumn(verbose_name="GiveBack", template_code=giveBack_car, empty_values=())

    class Meta:
        model = Orders
        fields = ['car_owner', 'car', 'is_complete']
        template_name = "django_tables2/bootstrap4.html"
        orderable = True


rent = """<a href="{% url 'rent_car' record.pk %}">rent</a>
"""


# EDIT_doctor="""<a href="{% url 'modifier_doctor' record.pk %}"><i class="fa fa-edit" style="margin-down : 33px; font-size: 21px;"></i></a>
# """

class carsTable(tables.Table):
    # modifier = tables.TemplateColumn( verbose_name="modifier", template_code=EDIT_doctor, empty_values=())#,'modifier_bc_achat', args=[A('pk')], empty_values=(),orderable=False, text='Edit', attrs={"td": {"align": "center"}})
    rent = tables.TemplateColumn(verbose_name="rent", template_code=rent, empty_values=())

    class Meta:
        model = Car
        fields = ['car_name', 'car_model', 'car_seats', 'gearbox', 'date_added', 'extra_info', 'owner', 'price']
        template_name = "django_tables2/bootstrap4.html"
        orderable = True


