from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArmyForm
from .servises import fight_flangs

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


def fight_arm(request):
    army = Army.objects.all()
    return render(request, 'fight_arm.html', {'armys':army})

def fight(request, cname1, cname2):
    arm1 = Army.objects.get(commander_name = cname1)
    arm2 = Army.objects.get(commander_name = cname2)
    left = fight_flangs(arm1.left_army,arm2.left_army)
    center = fight_flangs(arm1.center_army,arm2.center_army)
    right = fight_flangs(arm1.right_army,arm2.right_army)
    winner = 0
    def winner1():
        nonlocal winner
        arm1.victories += 1
        arm1.save()
        arm2.defeats += 1
        arm2.save()
        winner = 1
    def winner2():
        nonlocal winner
        arm2.victories += 1
        arm2.save()
        arm1.defeats += 1
        arm1.save()
        winner = 2
    if left  == -999 or center  == -999 or right == -999:
        print(left, center, right)
        print("-----------------error-----------------error-----------------")
    elif left == 1 and center == 1:
        winner1()
    elif center == 1 and right == 1:
        winner1()
    elif left == 1 and right == 1:
        winner1()
    elif left == 2 and center == 2:
        winner2()
    elif center == 2 and right == 2:
        winner2()
    elif left == 2 and right == 2:
        winner2()
    elif (left == 1 and center == 0 and right == 0) or (left == 0 and center == 1 and right == 0) or (left == 0 and center == 0 and right == 1):
        winner1()
    elif (left == 2 and center == 0 and right == 0) or (left == 0 and center == 2 and right == 0) or (left == 0 and center == 0 and right == 2):
        winner2()
    else:
        print(left, center, right)
        print("No whinner")
    context = {'army1':arm1,
               'army2':arm2,
               'left':left,
               'center':center,
               'right':right,
               'whiner':winner}
    print(winner)
    return render(request, 'win_page.html', context)

def deleteArmy(request, army_id):
    army = get_object_or_404(Army, pk=army_id)
    army.delete()
    return redirect('main_page')