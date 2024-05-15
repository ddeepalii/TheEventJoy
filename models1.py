# from django.db import models
# from django.contrib.auth.models import User
# FOOD_CHOICES = (
#     ('Indian', 'INDIAN'),
#     ('Italian', 'ITALIAN'),
#     ('Chinese', 'CHINESE')
# )
#
#
# class Bookings(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     eventname = models.CharField(max_length=255)
#     eventdate = models.DateField()
#     eventime = models.TimeField()
#
#     def __str__(self):
#         return self.eventname + " by " + self.user.username
#
#
# class HallDetails(models.Model):
#     hallname = models.CharField(max_length=200, primary_key=True)
#     guests = models.IntegerField(default=" ")
#     halltype = models.CharField(max_length=200)
#     light = models.CharField(max_length=20)
#     ac = models.BooleanField()
#     dj = models.BooleanField()
#     food = models.CharField(max_length=20, choices=FOOD_CHOICES, default='INDIAN')
#     hall_image = models.ImageField(null=True, blank=True, upload_to='TheEventJoy/Images', default="")
#
#     def __str__(self):
#         return f'{self.hallname}'
#
#
# class Availability(models.Model):
#     a_date = models.DateField()
#     a_time_in = models.TimeField()
#     a_time_out = models.TimeField()
#     hall_category = models.ForeignKey(HallDetails, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.a_date} from {self.a_time_in} to {self.a_time_out}'
#
#
#
#
#
# from django.contrib import admin
# from .models import Availability,HallDetails, Bookings
#
#
# admin.site.register(HallDetails)
# admin.site.register(Availability)
# admin.site.register(Bookings)
#
#
# def booknow(request):
#     if request.method == "POST":
#         eventname = request.POST['eventname']
#         eventdate = request.POST['eventdate']
#         eventime = request.POST['eventime']
#         booking = Bookings(eventname=eventname, eventdate=eventdate, eventime=eventime)
#         booking.save()
#         messages.success(request, "Booking Successfully Done !")
#     return render(request, "availability.html")
#
#
#
# # def services(request):
# #     if request.method == "POST":
# #         # check = Availability.objects.all()
# #         # for c in check:
# #         #     if check.exists():
# #         #         return HttpResponse("Found")
# #         #     else:
# #         #         return HttpResponse("Not Found")
# #         date = request.POST.get('date', ' ')
# #         time = request.POST.get('time', ' ')
# #         availability = Availability(a_date=date, a_time=time)
# #         availability.save()
# #
# #     return render(request, "availability.html")
#
# def handlesignup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirmpassword = request.POST['confirmpassword']
#
#         # Create User
#         myuser = User.objects.create_user(username,email, password)
#         myuser.name = name
#         myuser.phone = phone
#         myuser.save()
#         messages.success(request, "Your account has been successfully created")
#         return redirect('/')
#
#     else:
#         return HttpResponse("Error")
#
#
# def handlelogin(request):
#     if request.method == "POST":
#         loginUsername = request.POST['loginUsername']
#         loginPassword = request.POST['loginPassword']
#         user = authenticate(username=loginUsername, password=loginPassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Successfully Logged In")
#             return redirect("/")
#         else:
#             messages.error(request, "Invalid Credentials ! Please try again")
#             return redirect("/")
#     return HttpResponse("404 Not Found")
#
#
#
#
#
#
# #
#
#
#
#
#
#
#
# class Hall(forms.ModelForm):
#     class Meta:
#         model = HallDetails
#         fields = ['hallname', 'guests', 'halltype', 'light', 'ac', 'dj', 'food', 'hall_image']
#
#
# class Avail(forms.ModelForm):
#     a_date = forms.DateField(widget=DatePickerInput(format='%d %m %y'))
#     a_time_in = forms.TimeField(widget=TimePickerInput)
#     a_time_out = forms.TimeField(widget=TimePickerInput)
#
#     class Meta:
#         model = Availability
#         fields = ['a_date', 'a_time_in','a_time_out']
#
#
#
#
#
# alag se model ameniites ka : ac/heater, dj-short ya large, dance floor:- floor1,floor2, decoration :- flowers, baloons, ribbons,
# external - decoartions
#
#     , food