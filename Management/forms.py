from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vehicle, Workshop, Appointment, Mechanic, Job, Checklist, Point, Attention

from django.forms import DateTimeInput, DateField, DateInput
from django.utils import timezone
import datetime

# Create your forms here.

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required. Enter your last name.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Password',
            'password2': 'Confirmación Password',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'E-mail'
        }

# class VehicleForm(forms.ModelForm):
#     brand_choices = [('ford', 'Ford'), ('toyota', 'Toyota'), ('honda', 'Honda')]
#     model_choices = [('focus', 'Focus'), ('corolla', 'Corolla'), ('civic', 'Civic')]

#     brand = forms.ChoiceField(choices=brand_choices)
#     model = forms.ChoiceField(choices=model_choices)
#     class Meta:
#         model = Vehicle
#         fields = ['brand', 'model', 'patent']
#         labels = {
#             'brand': 'Marca',
#             'model': 'Modelo',
#             'patent': 'Patente'
#         }

class VehicleForm(forms.ModelForm):
    # brand_choices = [('','Elegir marca vehículo'), ('ford', 'Ford'), ('toyota', 'Toyota'), ('honda', 'Honda')]
    # model_choices = [('','Elegir modelo vehículo'), ('focus', 'Focus'), ('corolla', 'Corolla'), ('civic', 'Civic')]

    # brand = forms.ChoiceField(choices=brand_choices)
    # model = forms.ChoiceField(choices=model_choices)
    # brand = forms.CharField(label='Marca')
    # model = forms.CharField(label='Modelo')

    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'patent']
        labels = {
            'brand': 'Marca',
            'model': 'Modelo',
            'patent': 'Patente'
        }
        widgets = {
            'brand': forms.Select(choices=[('','Elegir marca vehículo'), ('ford', 'Ford'), ('toyota', 'Toyota'), ('honda', 'Honda')]),
            'model': forms.Select(choices=[('','Elegir modelo vehículo'), ('focus', 'Focus'), ('corolla', 'Corolla'), ('civic', 'Civic')])
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     brand_choices = [('','Elegir marca vehículo')('ford', 'Ford'), ('toyota', 'Toyota'), ('honda', 'Honda')]
    #     model_choices = [('','Elegir modelo vehículo')('focus', 'Focus'), ('corolla', 'Corolla'), ('civic', 'Civic')]

    #     self.fields['brand'].widget = forms.Select(choices=brand_choices)
    #     self.fields['model'].widget = forms.Select(choices=model_choices)

    def clean_patent(self):
        patent = self.cleaned_data['patent']
        if Vehicle.objects.filter(patent=patent).exists():
            raise forms.ValidationError("Ya existe un vehículo con esta patente.")
        return patent


class AppointmentForm(forms.ModelForm):
    # def __init__(self, *args, vehiculos=None, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if vehiculos is not None:
    #         self.fields['vehiculo'].queryset = vehiculos
    def __init__(self, *args, user=None):
        super().__init__(*args)
        if user is not None:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(customer=user)

    class Meta:
        model = Appointment
        fields = ['vehicle','attention','date_register','mechanic','workshop','description_customer']
        labels = {
            'vehicle':'Vehículo',
            'attention':'Atención',
            'date_register':'Fecha',
            'mechanic':'Mecánico',
            'workshop':'Sucursal',
            'description_customer':'Descripción'
        }
        widgets = {
             'date_register': DateInput(
                format='%Y-%m-%d',  # Formato de la fecha que se muestra
                attrs={
                    'type': 'date',
                    # cadena que representa 'AAAA-MM-DDTHH:MM'
                    'min': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                    'max': (datetime.datetime.now() + datetime.timedelta(days=365)).strftime('%Y-%m-%d'),
                }
            ),
            # 'fecha_hora': DateTimeInput(
            #     attrs={
            #         'type': 'datetime-local',
            #         # cadena que representa 'AAAA-MM-DDTHH:MM'
            #         'min': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%dT08:00'),
            #         'max': (datetime.datetime.now() + datetime.timedelta(days=365)).strftime('%Y-%m-%dT17:00'),
            #     }
            # ),
        }

    # def clean_date_register(self):
    #     date_register = self.cleaned_data.get('date_register')
    #     if date_register:
    #         min_hora = timezone.make_aware(datetime.datetime.combine(date_register.date(), datetime.time(8, 0)))
    #         max_hora = timezone.make_aware(datetime.datetime.combine(date_register.date(), datetime.time(17, 0)))
            
    #         if not min_hora <= date_register <= max_hora:
    #             raise forms.ValidationError("La hora debe estar entre las 8:00 AM y las 17:00 PM.")
    #     return date_register


# class MechanicForm(UserCreationForm):
#     phone = forms.IntegerField(label='Teléfono', required=True)
#     employee = forms.ModelChoiceField(queryset=Mechanic.objects.all(), label='Empleado', required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'employee')
#         labels = {
#             'username': 'Nombre de usuario',
#             'password1': 'Password',
#             'password2': 'Confirmación Password',
#             'first_name': 'Nombre',
#             'last_name': 'Apellido',
#             'email': 'E-mail'
#         }
        
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         if commit:
#             user.save()
#         return user

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'phone': 'Teléfono'
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # fields = ['appointment', 'description_job']
        fields = ['description_job']
        labels = {
            # 'appointment': 'Cita',
            'description_job': 'Descripción del trabajo'
        }

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['state', 'front_lights', 'rear_lights', 'chassis', 'cleaning', 'extinguisher', 'first_aid_kit', 'triangles', 'hydraulic_jack', 'spare_wheel']
        labels = {
            'state': 'Estado',
            'front_lights': 'Luces delanteras',
            'rear_lights': 'Luces traseras',
            'chassis': 'Chasis',
            'cleaning': 'Limpieza',
            'extinguisher': 'Extinguidor',
            'first_aid_kit': 'Kit primeros auxilios',
            'triangles': 'Triángulos',
            'hydraulic_jack': 'Gata hidráulica',
            'spare_wheel': 'Rueda de repuesto'
        }
