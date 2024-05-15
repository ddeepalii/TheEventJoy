from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from .forms import *
from .models import *
from math import ceil
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.core.mail import send_mail
from django.conf import settings
import json
from django.core import serializers


@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # remove other sessions
    Session.objects.filter(usersession__user=user).delete()

    # save current session
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user,
        session_id=request.session.session_key
    )


def index(request):
    user = request.session.get('user')
    if user is not None:
        return HttpResponseRedirect('/profile')
    else:
        return render(request, "index.html")


def aboutus(request):
    return render(request, "aboutus.html")


def contactus(request):
    if request.method == "POST":
        c = Contact(request.POST, request.FILES)
        if c.is_valid():
            c.save()
            messages.success(request, "Your query has been sent Successfully !!")
            return HttpResponseRedirect('profile')
    else:
        c = Contact()
    return render(request, 'contactus.html', {'c': c})


def viewquery(request):
    viewquery = Contactus.objects.all()
    return render(request, 'adminviewquery.html', {'viewquery': viewquery})


def adminindex(request):
    return render(request, "adminindex.html")


def hallslot(request):
    if request.method == "POST":
        f = HSlot(request.POST, request.FILES)
        if f.is_valid():
            name = f.cleaned_data['timeslot']
            fc = HallSlot.objects.filter(timeslot=name)
            if fc.exists():
                return HttpResponse("Time Slot already Added")
            else:
                f.save()
                messages.success(request, "Timeslot Added Successfully")
                return HttpResponseRedirect('hallslot')
    else:
        f = HSlot()
    return render(request,'hallslot.html', {'f': f})


def hallform(request):
    if request.method == "POST":
        h = Hall(request.POST, request.FILES)
        if h.is_valid():
            name = h.cleaned_data['hallname']
            hall = HallDetails.objects.filter(hallname=name)
            if hall.exists():
                return HttpResponse("Food Already Added")
            else:
                h.save()
                messages.success(request,"Hall Added Successfully")
                return HttpResponseRedirect('hallform')

    else:
        h = Hall()
    return render(request,'hallform.html', {'h': h})

    # if request.method == "POST":
    #     h = Hall(request.POST, request.FILES)
    #     if h.is_valid():
    #         h.save()
    #         return render(request, 'hallform.html', {'h': h})
    # else:
    #     h = Hall()
    # return render(request,'hallform.html', {'h': h})


def updatehall(request,hal):
    hall = HallDetails.objects.get(hallname=hal)
    if request.method == "POST":
        hform = Hall(request.POST, instance=hall)
        if hform.is_valid():
            # name = form.cleaned_data['cname']
            # f = CategoryFood(cname=name)
            hform.save()
            messages.success(request, "Hall Updated Successfully")
            return HttpResponseRedirect('adminhdd')
    else:
        hform = Hall(instance=hall)
    return render(request, "UpdateHall.html", {'hform': hform})


def deletehall(request, hal):
    instance = HallDetails.objects.get(hallname=hal)
    instance.delete()
    return HttpResponseRedirect('adminhdd')


def adminviewhall(request,hal):
    halldetails = HallDetails.objects.filter(hallname=hal)
    return render(request, "adminviewhall.html", {'halldetails': halldetails})


# data fetch in basis of fname, if already exisits then print otherwise add
def foodform(request):
    if request.method == "POST":
        f = Food(request.POST, request.FILES)
        if f.is_valid():
            name = f.cleaned_data['fname']
            food = DetailFood.objects.filter(fname=name)
            if food.exists():
                return HttpResponse("Food Already Added")
            else:
                f.save()
                messages.success(request,"Food Added Successfully")
                return HttpResponseRedirect('foodform')

    else:
        f = Food()
    return render(request,'foodform.html', {'f': f})


def updatefood(request, fid):
    upfood = DetailFood.objects.get(fid=fid)
    if request.method == "POST":
        form = Food(request.POST, instance=upfood)
        if form.is_valid():
            # name = form.cleaned_data['cname']
            # f = CategoryFood(cname=name)
            form.save()
            messages.success(request, "Food Item Updated Successfully")
            return render(request, "adminfdd.html")
    else:
        form = Food(instance=upfood)
    return render(request, "UpdateFood.html", {'form': form})


def delfood(request,fn):
    instance = DetailFood.objects.get(fname=fn)
    instance.delete()
    messages.success(request, "Food Item Deleted Successfully")
    return HttpResponseRedirect('fdd')


def foodcat(request):
    if request.method == "POST":
        f = FoodCat(request.POST, request.FILES)
        if f.is_valid():
            name = f.cleaned_data['cname']
            fc = CategoryFood.objects.filter(cname=name)
            if fc.exists():
                return HttpResponse("Food category already Added")
            else:
                f.save()
                messages.success(request, "Food Added Successfully")
                return HttpResponseRedirect('foodcat')

    else:
        f = FoodCat()
    return render(request,'foodCategory.html', {'f': f})


def foodcatdisplay(request):
    fcat = CategoryFood.objects.all()
    return render(request, "FoodCatDisplay.html", {'fcat': fcat})


def updatefoodcat(request, fc):
    fcat = CategoryFood.objects.get(cname=fc)
    if request.method == "POST":
        form = FoodCat(request.POST, instance=fcat)
        if form.is_valid():
            # name = form.cleaned_data['cname']
            # f = CategoryFood(cname=name)
            form.save()
            messages.success(request, "Food Category Updated Successfully")
            return HttpResponseRedirect('fcd')
    else:
        form = FoodCat(instance=fcat)
    return render(request, "UpdateFoodCat.html", {'form': form})


def deletefoodcat(request, fc):
    instance = CategoryFood.objects.get(cname=fc)
    instance.delete()
    messages.success(request, "Food Category Deleted Successfully")
    return HttpResponseRedirect('fcd')


def fooddetaildisplay(request,hal):
    allprods = []
    catprods = DetailFood.objects.values('fcategory')
    cats = {item['fcategory'] for item in catprods}
    for c in cats:
        prod = DetailFood.objects.filter(fcategory=c)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
        params = {"allprods": allprods}
    return render(request, "FoodDetailDisplay.html", params)


def checkout(request, hal):
    if request.method == "POST":
        hall_date = request.POST.get('datepickerid')
        timeslot = request.POST.get('slot', '')
        fc = Booking.objects.filter(hall_date=hall_date).filter(booked_hall=hal).filter(timeslot=timeslot)
        if fc.exists():
            return HttpResponse("Hall already booked")
        else:
            items_json = request.POST.get('items_json', '')
            print(items_json)
            bill = request.POST.get('bill', '')
            # booked_hall = request.POST.get('booked_hall', '')
            timeslot = request.POST.get('slot', '')
            user = request.session.get('user')
            booking = Booking(user=user, items_json=items_json, bill=bill, booked_hall=hal, hall_date=hall_date, timeslot=timeslot)
            booking.save()

            obj = User.objects.get(username=request.session.get('user'))
            print(obj.email)
            subject = "Test Mail"
            message = "This is your hall booking confirmation mail from TheEventJoy. To view your Booking Click - http://127.0.0.1:8000/viewbooking"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [obj.email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, "Booking Successful !! Check your email for the confirmation mail !!")
            return HttpResponseRedirect('/profile')
    halldetails = HallDetails.objects.filter(hallname=hal)
    hslots = HallSlot.objects.all()
    return render(request, "checkout.html", {'halldetails':halldetails, 'hslots': hslots})


def viewbooking(request):
    user = request.session.get('user')
    print(user)
    items_json = request.POST.get('items_json', '')
    # type(items_json)
    # print(items_json)
    # print(item_json['pr5'])
    # ij = json.dumps(item_json)
    # print(ij)
    booking = Booking.objects.filter(user=user)
    print(items_json)
    if not booking:
        print(booking)
        return render(request, 'nobooking.html')
    else:
        print(items_json)
        return render(request, 'viewbooking.html', {'booking': booking})


def adminviewbooking(request):
    booking = Booking.objects.all()

    return render(request,'adminviewbooking.html', {'booking': booking})


def adminfdd(request):
    allprods = []
    catprods = DetailFood.objects.values('fcategory')
    cats = {item['fcategory'] for item in catprods}
    for c in cats:
        prod = DetailFood.objects.filter(fcategory=c)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
        params = {"allprods": allprods}
    return render(request, "adminfdd.html", params)


def halldetaildisplay(request):
    halldetails = HallDetails.objects.all()
    return render(request, "HallDetailDisplay.html", {'halldetails': halldetails})


def adminhdd(request):
    halldetails = HallDetails.objects.all()
    return render(request, "adminhdd.html", {'halldetails': halldetails})


def bookinghall(request, hal):
    halldetails = HallDetails.objects.filter(hallname=hal)
    return render(request, "confirmhall.html", {'halldetails': halldetails})


def availability(request, hal):
    halldetails = HallDetails.objects.filter(hallname=hal)
    hslots = HallSlot.objects.all()
    if request.method == "POST":
        hall_date = request.POST.get('datepickerid')
        timeslot = request.POST.get('slot', '')
        fc = Booking.objects.filter(hall_date=hall_date).filter(booked_hall=hal).filter(timeslot=timeslot)
        if fc.exists():
            return render(request, 'hallunavail.html', {'halldetails':halldetails,'hslots': hslots})
        else:
            return HttpResponseRedirect('fdd')
    return render(request, "availability.html", {'halldetails': halldetails, 'hslots':hslots })


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account Created Successfully ! Please Login to Continue !")
            return HttpResponseRedirect('/login')

    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def log_in(request):
    if request.method == "POST":
        items_json = request.POST.get('items_json')
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)

            if user is not None and user.is_active:
                logout(request)
                request.session['user'] = uname

                login(request, user)
                messages.success(request, "Logged In Successfully")
                return HttpResponseRedirect('/profile')

        else:
            messages.success(request, "Incorrect Username or Password ! Try Again !")
            return HttpResponseRedirect('/login')
    else:
        fm = AuthenticationForm(request=request, data=request.POST)
    return render(request, 'login.html', {'form': fm})


def profile(request):
    if request.user.is_superuser == True:
            return render(request, 'adminindex.html')
    elif request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'pleaselogin.html')


def pleaselogin(request):
    return render(request, 'pleaselogin.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, "Password Changed Successfully")
                return HttpResponseRedirect('/profile')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login')

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response

