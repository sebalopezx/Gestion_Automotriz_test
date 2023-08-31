from re import A
from django.db import models
from django.contrib.auth.models import User
from django.forms import CheckboxInput, DateField, DateTimeField, TimeField



# Create your models here.

# class User(User):
#     def __str__(self):
#         return self.username, self.password, self.email

class Vehicle(models.Model):
    customer = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False,)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    patent = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.brand} {self.model}, Patente: {self.patent}  de: {self.customer}"

class Workshop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    num_addres = models.IntegerField()

    def __str__(self):
        return f"{self.name} > {self.address} # {self.num_addres}"

class Mechanic(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    # phone = models.IntegerField() # cambiar a phone number
    # employee = models.ForeignKey(User, 
    #                              on_delete=models.CASCADE,
    #                              null=False,
    #                              blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attention(models.Model):
    attention = models.TimeField()
    # day = DateField()
    # date = DateTimeField()
    def formatted_attention(self):
        if self.attention.hour == 8:
            context = ('AM')
        else:
            context = ('PM') 
        return f"{self.attention.__format__('%H:%M')} {context}"
    
    def __str__(self):
        return f"{self.formatted_attention()}"

class Appointment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    attention = models.ForeignKey(Attention, on_delete=models.CASCADE)
    date_register = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True) # auto add: ingresa time automaticamente si no se ingresa manualmente
    date_finished = models.DateTimeField(null=True, blank=True) # Blank , se puede dejar vacio para llenado posterior
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    description_customer = models.TextField(null=True, blank=True)
    inprogress = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    
    # def get_state_display(self):
    #     return "Completo" if self.state else "Incompleto"

    def __str__(self):
        return f"Cita para vehículo: {self.vehicle} __  Fecha de la Cita: {self.date_register.strftime('%d-%m-%Y')}"

class Job(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    description_job = models.TextField(null=True, blank=True)
    # checklist = models.OneToOneField(Checklist, on_delete=models.CASCADE)
    
    def __str__(self):
        # if self.description_job == None:
        #     self.description_job = "Sin descripción"
        #     return f"({self.id}) {self.appointment} {self.description_job}"
        # else:
        return f"({self.id}) {self.appointment}"


class Point(models.Model):
    customer = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False,)
    points = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f" {self.customer} - Puntos: {self.points}"

class Checklist(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    front_lights = models.BooleanField(default=False)
    rear_lights = models.BooleanField(default=False)
    chassis = models.BooleanField(default=False)
    cleaning = models.BooleanField(default=False)  
    extinguisher = models.BooleanField(default=False)
    first_aid_kit = models.BooleanField(default=False)
    triangles = models.BooleanField(default=False)
    hydraulic_jack = models.BooleanField(default=False)
    spare_wheel = models.BooleanField(default=False)

    def __str__(self):
        return f"""Checklist: 
                {self.id}.
                {self.state}
                {self.front_lights}
                {self.rear_lights}
                {self.chassis} 
                {self.cleaning} 
                {self.extinguisher} 
                {self.first_aid_kit}
                {self.triangles}
                {self.hydraulic_jack}
                {self.spare_wheel}"""
