from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Register, DataSegment, MipsProgram, MemoryClearer, IF, ID, EX, MEM, WB



def reset(request):
    registers = Register.objects.all()
    clear = MemoryClearer.objects.all()
    for x in registers:
        x.value = "0000000000000000"
        x.save()
    data = DataSegment.objects.all()
    request.session['goto'] = 0
    reset = None
    for x in clear:
        if x.memoryType == 0:
            try:
                reset = DataSegment.objects.get(name = x.name)
                reset.value = "0000000000000000"
                reset.save()
            except DataSegment.DoesNotExist:
                reset = None
        else:
            try:
                reset = MipsProgram.objects.get(name = x.name)
                reset.value = "0000000000000000"
                reset.save()
            except MipsProgram.DoesNotExist:
                reset = None
    while MemoryClearer.objects.count():
        MemoryClearer.objects.all()[0].delete()
    return render(request, 'simulator/home.html')
#    for x in data:
#        x.value = "0000000000000000"
#        x.save()
#    mips = MipsProgram.objects.all()
#    for x in mips:
#        x.value = "0000000000000000"
#        x.save()
#    while MemoryClearer.objects.count():
#        MemoryClearer.objects.all()[0].delete()
#    return render(request, 'simulator/home.html')
#    memory = DataSegment.objects.all()    
#    for x in memory:
#        x.value = "00"
#        x.save()
#    y = 0
#    a = 0
#    b = 0
#    c = 0
#    first = 0
#    second = 0
#    third = 0
#    while y < 4096:
#        if a == 0:
#            first = str(a)
#        else:
#            first = hex(a).lstrip("0x").upper()
#        if b == 0:
#            second = str(b)
#        else:
#            second = hex(b).lstrip("0x").upper()
#        if c == 0:
#            third = str(c)
#        else:
#            third = hex(c).lstrip("0x").upper()
#            
#        memoryname = "1" + third + second + first
#        new_memory = MipsProgram(name=memoryname, value="00")
#        new_memory.save()
#        if a <= 14:
#            a = a + 1
#        elif b <=14 and a == 15:
#            a = 0
#            b = b + 1
#        elif c <= 14 and b == 15 and a == 15:
#            a = 0
#            b = 0
#            c = c + 1
#        y = y + 1
#    y = 0
#    a = 0
#    while y < 1024:
#        new_memory = MipsProgram(name=a, value="0000000000000000")
#        new_memory.save()
#        a = a + 4
#        y = y + 1
    

def home(request):
    request.session['goto'] = 0
    return render(request, 'simulator/home.html')

def gotoMemory(request):
    memory = int(request.POST['memoryHere'], 16)
    mips = None
    data = None
    if memory >= 4096:
        request.session['goto'] = 1
        y = 0
        memory = memory - 4096
        while y <= 3:
            try:
                mips = MipsProgram.objects.get(name = memory - y)
                break
            except MipsProgram.DoesNotExist:
                mips = None
            y = y + 1
        context = {
            'memory':request.POST['memoryHere'],
            'mips': mips
        }
        return render(request, 'simulator/home.html', context)
    else:
        request.session['goto'] = 1
        y = 0
        while y <= 7:
            try:
                data = DataSegment.objects.get(name = memory - y)
                break
            except DataSegment.DoesNotExist:
                data = None
            y = y + 1
        context = {
            'memory':request.POST['memoryHere'],
            'data':data
        }
        return render(request, 'simulator/home.html', context)

def registeredReg(request):
    request.session['goto'] = 0
    registers = Register.objects.all()
    for x in registers:
        x.value = request.POST[x.name]
        x.save()
    return render(request, 'simulator/home.html')

def changeDataMemory(request):
    request.session['goto'] = 0
    data = int(request.POST['memoryName'], 16)
    memory = None
    y = 0
    while y <= 7:
        try:
            memory = DataSegment.objects.get(name = data - y)
            memory.value = request.POST['memoryValue']
            memory.save()
            newClearer = MemoryClearer(name=data-y, memoryType=0)
            newClearer.save()
            break
        except DataSegment.DoesNotExist:
            memory = None
        y = y + 1
    return render(request, 'simulator/home.html')

def inputReg(request):
    request.session['goto'] = 0
#    while MipsProgram.objects.count():
#        MipsProgram.objects.all()[0].delete()
    firsthalf_registers = Register.objects.all()[:10]
    secondhalf_registers = Register.objects.all()[10:20]
    thirdhalf_registers = Register.objects.all()[20:]
    context = {
        'first_registers' : firsthalf_registers,
        'second_registers' : secondhalf_registers,
        'third_registers' : thirdhalf_registers,
    }
    return render(request, 'simulator/inputRegisters.html', context)

def programRegistered(request):
    request.session['goto'] = 0
    programLines = [l for l in request.POST['mipsProgram'].split("\n") if l]
    programMemory = MipsProgram.objects.all().order_by('id')[:len(programLines)]
    x = 0
    for y in programMemory:
        y.value = programLines[x]
        y.save()
        newClearer = MemoryClearer(name=y.name, memoryType=1)
        newClearer.save()
        x = x + 1
    return render(request, 'simulator/home.html')

def pipeline(request):
	return render(request, 'simulator/pipeline.html', context)