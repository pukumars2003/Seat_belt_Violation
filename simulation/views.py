from django.shortcuts import render

# simulation/views.py

# simulation/views.py

from django.shortcuts import render, redirect
from .forms import SimulationForm
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        form = SimulationForm(request.POST)
        if form.is_valid():
            request.session['chassis_number'] = form.cleaned_data['chassis_number']
            request.session['mobile_number'] = form.cleaned_data['mobile_number']
            request.session['seatbelt_worn'] = form.cleaned_data['seatbelt_worn']
            request.session['distance'] = 0  # Start at 0 km
            return redirect('simulate')
    else:
        form = SimulationForm()
    return render(request, 'index.html', {'form': form})

def simulate(request):
    if 'distance' not in request.session:
        return redirect('index')
    
    distance = request.session['distance']

    # Check if distance is >= 15 km
    if distance >= 15:
        return redirect('challan')
    # Check if distance is 5 or 10 km
    elif distance in [5, 10]:
        return redirect('notification')

    # Increment distance every 2 seconds (handled in frontend)
    return render(request, 'simulate.html', {
        'distance': distance,
        'chassis_number': request.session['chassis_number'],
        'mobile_number': request.session['mobile_number']
    })

def update_distance(request):
    if 'distance' in request.session:
        request.session['distance'] += 1

        # After updating distance, check if it exceeds 15 km
        if request.session['distance'] >= 15:
            return JsonResponse({'redirect': 'challan'})
        
        # Check if the new distance is 5 or 10 km
        elif request.session['distance'] in [5, 10]:
            return JsonResponse({'redirect': 'notification'})

    return JsonResponse({'distance': request.session['distance']})

def notification(request):
    
    if 'distance' in request.session:
        request.session['distance'] += 1

        # After updating distance, check if it exceeds 15 km
        if request.session['distance'] >= 15:
            return redirect('challan')
        

    return render(request,'notification.html',{
        'distance':request.session['distance']
    })

def challan(request):
    return render(request, 'challan.html', {
        'chassis_number': request.session['chassis_number'],
        'mobile_number': request.session['mobile_number'],
        'fine': 500
    })
        

