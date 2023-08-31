from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Creacion de usuario mediante django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
# Creacion de Cookies
from django.contrib.auth import login, logout, authenticate
# Manejo de error de integridad
from django.db import IntegrityError
# Decoradores para login
from django.contrib.auth.decorators import login_required

# MODELOS 
from .models import Mechanic, Vehicle, Appointment, Job, Checklist, Point
# FORMULARIO
from .forms import CustomUserCreationForm, VehicleForm, AppointmentForm, MechanicForm, JobForm, ChecklistForm

# from time import timezone
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')

# VIEWS LOGIN 

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html',{
#             'form_user':UserCreationForm()
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 # register user
#                 print(request.POST)
#                 newUser = User.objects.create_user(
#                     username=request.POST['username'],
#                     password=request.POST['password1']
#                     # email
#                     # first_name
#                     # last_name
#                 )
#                 newUser.save()
#                 # Creacion de Cookie
#                 login(request, newUser)
#                 # Redireccion hacia la seccion de menu para realizar el pedido
#                 return redirect('index')
#             except IntegrityError:
#                 return render(request, 'signup.html',{
#                     'form_user':UserCreationForm(),
#                     'error':'User already exists'
#                 })
#         else:
#             return render(request, 'signup.html',{
#                 'form_user':UserCreationForm(),
#                 'error':'Password do no match'
#             })


def signup(request):
    if request.method == 'POST':
        form_register = CustomUserCreationForm(request.POST)
        if form_register.is_valid():
            user = form_register.save()
            messages.success(request, 'Usuario registrado con éxito')
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Error al registrar usuario')
    else:
        form_register = CustomUserCreationForm()
    
    return render(request, 'signup.html', {
        'form_register': form_register
        })

# def signup(request):
#     message = ""
#     if request.POST['password1'] == request.POST['password2']:
#         try:
#             # register user
#             print(request.POST)
#             newUser = User.objects.create_user(
#                 username=request.POST['username'],
#                 password=request.POST['password1']
#                 # email
#                 # first_name
#                 # last_name
#             )
#             newUser.save()
#             # Creacion de Cookie
#             login(request, newUser)
#             # Redireccion hacia la seccion de menu para realizar el pedido
#             return redirect('mainMenu')
#         except IntegrityError:
#             return render(request, 'signup.html',{
#                 'form_user':UserCreationForm(),
#                 'error':'User already exists'
#             })
#     else:
#         form_user = UserCreationForm()
#         message = 'Password do no match'

#     return render(request, 'signup.html',{
#         'form_user':form_user,
#         'error':'Password do no match'
    #  })
    

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form_login':AuthenticationForm()
        })
    else:
        print(request.POST)
        user = authenticate(request, 
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            return render(request,'signin.html',{
                'form_login':AuthenticationForm(),
                'error':'Username or Password is incorrect'
            })
        else:
            # Crea la cookie con fecha de expiracion
            login(request, user)
            return redirect('index')


def signout(request):
    logout(request)
    return redirect('index')

# VIEWS CUSTOMERS

def register_vehicle(request):
    if request.method == 'POST':
        form_vehicle = VehicleForm(request.POST)
        if form_vehicle.is_valid():
            vehicle = form_vehicle.save(commit=False)
            vehicle.customer = request.user
            vehicle.save()
            messages.success(request, 'Vehículo creado exitosamente.')
            return redirect('vehicle')
        else:
             messages.error(request, 'Error al registrar vehículo')
    else:
        form_vehicle = VehicleForm()
        
    return render(request, 'register_vehicle.html', {
        'form': form_vehicle, 
    })


@login_required
def register_date(request):
    user = request.user  # Usuario Autenticado
    # Obtener los vehículos del usuario logeado
    user_vehicles = Vehicle.objects.filter(customer=user)
    # form_appointment = AppointmentForm(user=user)
    print(f"usuario para cita: {user}")
    if request.method == 'POST':
        form_appointment = AppointmentForm(request.POST, user=user)
        if form_appointment.is_valid():
            form_appointment.save()
            # msg = "Cita agregada"
            messages.success(request, 'Cita confirmada') 
            return redirect('appointment')
        else:
            # form_appointment = AppointmentForm()
            messages.error(request, 'Error al crear cita')

    else:
        # Filtro de vehiculos por usuario autenticado
        # vehiculos_usuario = Vehiculo.objects.filter(cliente=user)
        # form = CitaForm(vehiculo=vehiculos_usuario) 
        form_appointment = AppointmentForm(user=user)
        if not user_vehicles:
            # form_appointment.fields['vehicle'].widget.attrs['readonly'] = True
            for field in form_appointment.fields.values():
                field.widget.attrs['disabled'] = True
   

    return render(request, 'register_date.html', {
        'form': form_appointment,
        'user_vehicles': user_vehicles
    })


def points(request):
    pass


# VIEWS  PARA AMBOS

def list_user_data(request):
    user = User.objects.filter(username=request.user)
    error =  'No tiene datos'
    return render(request, 'user_data.html',{
        'list_data':user,
        'error':error
    })

# def detail_user_data(request, id):
#     if request.method == 'GET':
#          # Buscamos la tarea por id de tarea que servira de redireccion y por usuario
#         user = get_object_or_404(User, pk=id)
#         form_update = CustomUserCreationForm(instance=user)
#         return render(request, 'detail_user_data.html',{
#             'user':user,
#             'list_data_update':form_update
#         })
#     elif request.method == 'POST':
#         print(request.POST)
#         user = get_object_or_404(User, pk=id)
#         form_update = CustomUserCreationForm(request.POST, instance=user, exclude=['username'])
#         try:
#             if form_update.is_valid():
#                 form_update.save()
#                 messages.success(request, 'Datos actualizados exitosamente.') 
#                 return redirect('detail_user_data', id=id)
#             else:
#                 messages.error(request, 'Error al actualizar datos.')
#         except:
#             messages.error(request, 'Error al actualizar datos.')
#     return render(request, 'detail_user_data.html',{
#         'user':user,
#         'list_data_update':form_update,
#         'error':'Error updating user'
#     })

# def detail_user_data(request, id):
#     user = get_object_or_404(User, pk=id)

#     if request.method == 'POST':
#         form_update = CustomUserCreationForm(request.POST, instance=user)
#         try:
#             if form_update.is_valid():
#                 # form_update.save()
#                 user = form_update.save(commit=False)
#                 # user.username = user.username
#                 # user.save()
#                 if user.username == user.username:  # Verifica si el nombre de usuario cambió
#                     user.save()
#                     messages.success(request, 'Datos actualizados exitosamente.') 
#                     return redirect('detail_user_data', id=id)
#             else:
#                 messages.error(request, 'Error al actualizar datos.')
#         except:
#             messages.error(request, 'Error al actualizar datos.')
#     else:
#         form_update = CustomUserCreationForm(instance=user)
#         # Deshabilitar edición del campo username
#         form_update.fields['username'].widget.attrs['readonly'] = True

#     return render(request, 'detail_user_data.html', {
#         'user': user,
#         'list_data_update': form_update,
#         'error': 'Error updating user'
#     })



def detail_user_data(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        form_update = CustomUserCreationForm(request.POST, instance=user)
        form_update.fields['username'].widget.attrs['readonly'] = True
        try:
            if form_update.is_valid():
                form_update.save()
                messages.success(request, 'Datos actualizados exitosamente.') 
                return redirect('detail_user_data', id=id)
            else:
                messages.error(request, 'Error al actualizar datos.')
        except IntegrityError:
            messages.error(request, 'Error al actualizar datos.')

    else:
        form_update = CustomUserCreationForm(instance=user)
        # Deshabilitar edición del campo username
        form_update.fields['username'].widget.attrs['readonly'] = True
        
    return render(request, 'detail_user_data.html', {
        'user': user,
        'list_data_update': form_update,
        'error': 'Error updating user'
    })

# def detail_user_data(request, id):
#     user = get_object_or_404(User, pk=id)

#     if request.method == 'POST':
#         form_update = UserChangeForm(request.POST, instance=user)
#         try:
#             if form_update.is_valid():
#                 form = form_update.save(commit=False)
#                 if form.username == user.username:  # Verifica si el nombre de usuario cambió
#                     form.save()
#                     messages.success(request, 'Datos actualizados exitosamente.')
#                     return redirect('detail_user_data', id=id)
#                 else:
#                     messages.error(request, 'Error al actualizar datos: No se permite cambiar el nombre de usuario.')
#             else:
#                 messages.error(request, 'Error al actualizar datos.')
#         except:
#             messages.error(request, 'Error al actualizar datos.')
#     else:
#         form_update = UserChangeForm(instance=user)
#         # Deshabilitar edición del campo username
#         # form_update.fields['username'].widget.attrs['readonly'] = True
#         # form_update.fields['username'].disabled = True

#     return render(request, 'detail_user_data.html', {
#         'user': user,
#         'list_data_update': form_update,
#         'error': 'Error updating user'
#     })



def list_vehicles(request):
    vehicles = Vehicle.objects.filter(customer=request.user)
    # appointment = Appointment.objects.filter(appointment_customer=request.user)
    vehicle_ids = vehicles.values_list('id', flat=True)  # Obtener los IDs de los vehículos
    appointment = Appointment.objects.filter(vehicle_id__in=vehicle_ids)
    error =  'No tiene vehículos'
    return render(request, 'vehicle.html',{
        'list_vehicle':vehicles,
        'appointment':appointment,
        'error':error
    })

def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id, customer=request.user)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle')

def state_vehicle(request, id):
    # vehicles = Vehicle.objects.filter(pk=id, customer=request.user)
    # state_vehicle = Job.objects.filter(job_appointment_vehicle_id=id)
    state_vehicle = get_object_or_404(Appointment, pk=id, vehicle__customer=request.user)
    error =  'No tiene vehículos'
    return render(request, 'state_vehicle.html',{
        # 'list_vehicle':vehicles,
        'state_vehicle':state_vehicle,
        'error':error
    })


def list_appointment(request):
    # date = Vehicle.objects.filter(customer=request.user)
    date = Appointment.objects.filter(vehicle__customer=request.user)
    # date = Appointment.objects.all()
    error =  'No tiene citas'
    return render(request, 'appointment.html',{
        'list_dates':date,
        'error':error
    })

def update_user_data(request):
    pass

def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, pk=id, vehicle__customer=request.user)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment')




# VIEWS WORK USERS

# def register_mechanic(request):
#     if request.method == 'POST':
#         form_user = CustomUserCreationForm(request.POST)
#         form_mechanic = MechanicForm(request.POST)

#         if form_user.is_valid() and form_mechanic.is_valid():
#             # Crea el usuario primero
#             user = form_user.save()
#             # Crea el mecánico utilizando los datos del usuario
#             mechanic = form_mechanic.save(commit=False)
#             mechanic.first_name = user.first_name 
#             mechanic.last_name = user.last_name
#             mechanic.employee = user
#             mechanic.save()

#             messages.success(request, 'Mecánico agregado exitosamente.')
#             return redirect('register_mechanic')
#         else:
#              messages.error(request, 'Error al registrar Mecánico')
#     else:
#         form_user = CustomUserCreationForm()
#         form_mechanic = MechanicForm()
        
#     return render(request, 'register_mechanic.html', {
#         'form_user': form_user,
#         'form_mechanic': form_mechanic,
#     })

# def list_mechanic(request):
#     mechanic = Mechanic.objects.all()
#     error =  'No existen Mecánicos'
#     return render(request, 'list_mechanic.html',{
#         'list_mechanic':mechanic,
#         'error':error
#     })

# def update_mechanic(request, id):

    # if request.method == 'GET':
    #     # Buscamos la tarea por id de tarea que servira de redireccion y por usuario
    #     mechanic = get_object_or_404(Mechanic, pk=id)
    #     form_update = MechanicForm(instance=mechanic)
    #     return render(request, 'update_mechanic.html',{
    #         'data_mechanic':mechanic,
    #         'form_update':form_update
    #     })
    # else:
    #     try:
    #         print(request.POST)
    #         mechanic = get_object_or_404(Mechanic, pk=id)
    #         form_update = MechanicForm(request.POST, instance=mechanic)
    #         form_update.save()
    #         return redirect('list_mechanic')
    #     except:
    #         return render(request, 'update_mechanic.html',{
    #         'data_mechanic':mechanic,
    #         'form_update':form_update,
    #         'error':'Error updating mechanic'
    #     })


def list_mechanic(request):
    mechanic = Mechanic.objects.all()
    error =  'No existen Mecánicos'   
    return render(request, 'list_mechanic.html', {
        'list_mechanic':mechanic,
        'error':error
    })

def register_mechanic(request):
    if request.method == 'POST':
        form_mechanic = MechanicForm(request.POST)

        if form_mechanic.is_valid():
            form_mechanic.save()
            messages.success(request, 'Mecánico agregado exitosamente.')
            return redirect('list_mechanic')
        else:
             messages.error(request, 'Error al registrar Mecánico')
    else:
        error =  'No existen Mecánicos'
        form_mechanic = MechanicForm()
        
    return render(request, 'register_mechanic.html', {
        'form_mechanic': form_mechanic,
        'error':error
    })


def update_mechanic(request, id):

    if request.method == 'POST':
        mechanic = get_object_or_404(Mechanic, pk=id)
        form_update = MechanicForm(request.POST, instance=mechanic)
        print(form_update)
        try:   
            if form_update.is_valid():
                form_update.save()
                return redirect('list_mechanic')
        except Exception as e:
            print(e)
            messages.error(request, "Error al cargar : " + e)
    else:
        mechanic = get_object_or_404(Mechanic, pk=id)
        form_update = MechanicForm(instance=mechanic)

    return render(request, 'update_mechanic.html',{
            'data_mechanic': mechanic,
            'form_update': form_update,
        })

def delete_mechanic(request, id):
    mechanic = get_object_or_404(Mechanic, pk=id)
    if request.method == 'POST':
        mechanic.delete()
        return redirect('list_mechanic')




# JOBS

def list_jobs_pending(request):
    appointments = Appointment.objects.all()
    # jobs = Job.objects.all()
    error =  'No existen citas para trabajos'
     
    return render(request, 'list_jobs_pending.html', {
        'list_appointments':appointments,
        # 'list_jobs':jobs,
        'error':error
    })

def list_jobs_inprogress(request):
    # appointments = Appointment.objects.all()
    jobs = Job.objects.all()
    error =  'No existen citas para trabajos'
     
    return render(request, 'list_jobs_inprogress.html', {
        # 'list_appointments':appointments,
        'list_jobs':jobs,
        'error':error
    })

def list_jobs_completed(request):
    appointments = Appointment.objects.all()
    jobs = Job.objects.all()
    error =  'No existen citas para trabajos'
     
    return render(request, 'list_jobs_completed.html', {
        'list_appointments':appointments,
        'list_jobs':jobs,
        'error':error
    })

# def list_jobs(request):
#     appointments = Appointment.objects.all()
#     jobs = Job.objects.all()
#     error =  'No existen citas para trabajos'
     
#     return render(request, 'list_jobs.html', {
#         'list_appointments':appointments,
#         'list_jobs':jobs,
#         'error':error
#     })

def generate_ot(request, id):
    appointment = get_object_or_404(Appointment, pk=id)

    if request.method == 'POST':
        # Se genera una descripcion mas técnica del trabajo
        description = request.POST.get('description')
        # Al generar OT se genera el trabajo y checklist de la cita
        job = Job.objects.create(appointment=appointment, description_job=description)
        checklist = Checklist.objects.create(job=job)
        # Cambio de estado de la cita
        appointment.inprogress = True
        appointment.save()

        messages.success(request, "Trabajo creado exitosamente.")
        return redirect('list_jobs_pending')

    return HttpResponse(request, "Error al crear trabajo.")


# ESTE ES EL BUENO
def job_checklist (request, id):

    if request.method == 'POST':
        job = get_object_or_404(Job, pk=id)
        checklist = job.checklist
        form_update = ChecklistForm(request.POST, instance=checklist)  # , instance=job.checklist
        try:   
            if form_update.is_valid():
                form_update.save()
                return redirect('checklist')
        except Exception:
            messages.error(request, "Error al cargar")
    else:
        job = get_object_or_404(Job, pk=id)
        checklist =  job.checklist
        form_update = ChecklistForm(instance=checklist)

    return render(request, 'checklist.html', {
        'form_checklist':form_update,
        'checklist':checklist
    })


def update_job(request, id):
    if request.method == 'POST':
        job = get_object_or_404(Job, pk=id)
        # checklist = job.checklist
        form_update = JobForm(request.POST, instance=job) 
        try:   
            if form_update.is_valid():
                form_update.save()
                return redirect('list_jobs_inprogress')
        except Exception:
            messages.error(request, "Error al cargar")
    else:
        job = get_object_or_404(Job, pk=id)
        # checklist =  job.checklist
        form_update = JobForm(instance=job)

    return render(request, 'update_job.html', {
        'form_update':form_update,
        'job':job
    })


def delete_job(request, id, job_type):
    job = get_object_or_404(Job, pk=id)
    if request.method == 'POST':
        job.delete()
        if job_type == 'pending':
            return redirect('list_jobs_pending')
        elif job_type == 'inprogress':
            return redirect('list_jobs_inprogress')
        elif job_type == 'completed':
            return redirect('list_jobs_completed')
      

def completed_job(request, id):
    job = get_object_or_404(Job, pk=id)

    if request.method == 'POST':
        # Cambio de estado de la cita
        job.appointment.description_customer = job.description_job
        job.appointment.completed = True
        job.appointment.date_finished = timezone.now()
        job.appointment.save()

        messages.success(request, "Trabajo creado exitosamente.")
        return redirect('list_jobs_inprogress')

    return HttpResponse(request, "Error al crear trabajo.")



def update_vehicle(request):
    pass

def update_register_date(request):
    pass

def del_user(request):
    pass

def del_appointment(request):
    pass




def checklist(request):
    pass