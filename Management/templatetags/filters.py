from django import template
import locale

register = template.Library()

@register.filter(name='state_display')
def state_display(value):
    return '\u2705' if value else '\u274c'
    # return 'Completo' if value else "Incompleto"


@register.filter(name='coupon_valid')
def coupon_valid(value):
    return "Válido" if value else "Ocupado"

# @register.filter(name='capitalize_month')
# def capitalize_month(value):
#     # Verifica si el valor es un mes válido
#     months = [
#         'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
#         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
#     ]

#     if value.lower() in months:
#         return value.capitalize()

#     return value 



# @register.filter(name='custom_date_format')
# def custom_date_format(value):
#     if value:
#         # locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
#         formatted_date = value.strftime("%d de %B del %Y %H:%M %p")  # Formatea la fecha según tus especificaciones
#         # locale.setlocale(locale.LC_TIME, '')
#         return formatted_date.replace(formatted_date.split()[2], formatted_date.split()[2].capitalize())  # Capitaliza el mes
#     else:
#         return "En ejecución"


@register.filter(name='custom_date_format')
def custom_date_format(value):
    if value:
        months = {
            'January': 'Enero',
            'February': 'Febrero',
            'March': 'Marzo',
            'April': 'Abril',
            'May': 'Mayo',
            'June': 'Junio',
            'July': 'Julio',
            'August': 'Agosto',
            'September': 'Septiembre',
            'October': 'Octubre',
            'November': 'Noviembre',
            'December': 'Diciembre',
        }
        formatted_date = value.strftime("%d de %B del %Y a las %H:%M %p")

        # Reemplazar el nombre del mes en inglés por el equivalente en español
        for month_en, month_es in months.items():
            formatted_date = formatted_date.replace(month_en, month_es)

        return formatted_date
    else:
        return "En ejecución"


@register.filter(name='custom_months_format')
def custom_months_format(value):
    if value:
        months = {
            'January': 'Enero',
            'February': 'Febrero',
            'March': 'Marzo',
            'April': 'Abril',
            'May': 'Mayo',
            'June': 'Junio',
            'July': 'Julio',
            'August': 'Agosto',
            'September': 'Septiembre',
            'October': 'Octubre',
            'November': 'Noviembre',
            'December': 'Diciembre',
        }
        formatted_date = value.strftime("%d de %B del %Y")

        # Reemplazar el nombre del mes en inglés por el equivalente en español
        for month_en, month_es in months.items():
            formatted_date = formatted_date.replace(month_en, month_es)

        return formatted_date
    else:
        return "En ejecución"
    
@register.filter(name='format_clp')
def format_clp(value):
    if value:
        try:
            value = int(value)
        except (ValueError, TypeError):
            return value
        
        formatted_value = '${:,.0f} pesos'.format(value)
        return formatted_value