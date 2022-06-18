from django.shortcuts import render
from datetime import datetime
from .models import Event, Itinerary, Date



# Create your views here.
# def Home(request):
#     events = Event.objects.all()
#     for i in events:
#         i.time = i.time.strftime("%A, %B %d|%H:%M").split("|")
#         i.formattedtime = i.time[1]
#         ind = i.description.rfind(".")
#         if ind != -1:
#             i.description = i.description[:ind+1]

#     if request.method == 'POST':
#         dates = {i.time[0] for i in events}
#         organizebydate = {date:[] for date in dates}
#         for i in range(len(events)):
#             organizebydate[events[i].time[0]].append((events[i], i%2))
#         #sort by time[1]
#         for i in organizebydate:
#             organizebydate[i] = sorted(organizebydate[i], key=lambda x: x[0].time[1])
#         print(organizebydate)
#         selection = request.POST.get('date')
#         print(selection)
#         if selection=="default":
#             return render(request, 'index.html', context={
#                 "dates": dates,

#                 "chosen":False,
#             })
        
#         return render(request, 'index.html', context={
#                 "dates": dates,
#                 "timelinevals": organizebydate[selection],
#                 "chosen":True,
#                 "date":selection,
#         })
#     else:
#         dates = {i.time[0] for i in events}

#         return render(request, 'index.html', context={
#             "dates": dates,
#             "chosen":False,
#         })

def Home(request):
    events = Event.objects.all()
    # for i in events:
    #     i.time = i.time.strftime("%A, %B %d|%H:%M").split("|")
    #     i.formattedtime = i.time[1]
    #     ind = i.description.rfind(".")
    #     if ind != -1:
    #         i.description = i.description[:ind+1]
    if request.method == 'POST':
        #Sort into itineraries
        print(Itinerary.objects.all())
        print(events)
        
        itins = {i.title:[] for i in Itinerary.objects.all()}
        # print(itins)
        for i in events:
            if len(i.description)>500:
                ind = i.description.rfind(".")
                if ind != -1:
                    i.description = i.description[:ind+1]
            # print(i.itin.all())
            for j in i.itin.all():
                itins[j.title].append(i)
        selection = request.POST.get('Itinerary')
        #create date dicts
        chosenitin = itins[selection]
        dates = {i.time.date() for i in chosenitin}
        organizebydate = {date:[] for date in dates}
        for ev in chosenitin:
            organizebydate[ev.time.date()].append(ev)
            ev.time = ev.time.strftime("%A, %B %d|%H:%M").split("|")[1]
        print(organizebydate)
        #sort by .time.time()
        dates = []
        count = 0
        for i in organizebydate:
            organizebydate[i] = sorted(organizebydate[i], key=lambda x: x.time)
            k = []
            for ev in organizebydate[i]:
                k.append((ev, count%2))
                print(ev.time)
                count += 1
            organizebydate[i] = k
            d = Date(date=i)
            d.events = organizebydate[i]
            d.save()
            dates.append(d)
        #sort dates by date
        dates = sorted(dates, key=lambda x: x.date)
        print(dates)
        itins = {i for i in Itinerary.objects.all()}
        return render(request, 'index.html', context={
            "Itineraries" : itins,
            "Itinerary" : selection,
            "dates": dates,
            "chosen":True,
        })
    else:
        itins = {i.title for i in Itinerary.objects.all()}
        return render(request, 'index.html', context={
            "Itineraries": itins,
            "chosen":False,
        })
            
            
        
    

def About(request):
    return render(request, 'about.html', context={})

def Tutorial(request):
    return render(request, 'tutorial.html', context={})
