from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArmyForm

from .models import *

def main_page(request):
    a = Army.objects.all()
    print(a[0].faction.flag)
    context = {'armies' : a}
    return render(request, 'MainPage.html', context)


def add_army(request):
    if request.method == 'POST':
        form = ArmyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = ArmyForm()
    return render(request, 'add_army.html', {'form': form})


def army_detail_view(request, army_id):
    army = get_object_or_404(Army, pk=army_id)
    army_types = ArmyType.objects.all()

    if request.method == 'POST':
        left_army_id = request.POST.get('left_army')
        left_army = get_object_or_404(ArmyType, pk=left_army_id)
        army.left_army = left_army
        
        center_army_id = request.POST.get('center_army')
        center_army = get_object_or_404(ArmyType, pk=center_army_id)
        army.center_army = center_army
        
        right_army_id = request.POST.get('right_army')
        right_army = get_object_or_404(ArmyType, pk=right_army_id)
        army.right_army = right_army

        army.save()
        return redirect('main_page')

    return render(request, 'army_detail.html', {'army': army, 'army_types': army_types})

def deleteArmy(request, army_id):
    army = get_object_or_404(Army, pk=army_id)
    army.delete()
    return redirect('main_page')