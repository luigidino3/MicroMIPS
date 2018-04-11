from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Register, DataSegment, MipsProgram, MemoryClearer, IF, ID, EX, MEM, WB, Stall
import re

def immediateChecker(code):
    count = 0
    rt = ""
    rs = ""
    imm = ""
    for i in range(len(code)):
        if code[i] == 'r' and count == 0:
            j = i
            while code[j] != ',':
                rt+=code[j+1]
                j+=1

            count+=1
            #print(rt)
        elif code[i] == 'r' and count != 0:
            j = i
            while code[j] != ',':
                rs+=code[j+1]
                j+=1

            count+=1
            #print(rs)
        elif code[i] == '#' and count !=0:
            j = i
            ctr = 0
            while ctr != 4:
                imm = imm + code[j+1]
                j+=1
                ctr+=1
            #print(imm)
    return rt,rs,imm

def nonImmediateChecker(code):
    count = 0
    rt = ""
    rs = ""
    rd = ""

    for i in range(len(code)):
        if code[i] == 'r' and count == 0:
            j = i
            while code[j] != ',':
                rd+=code[j+1]
                j+=1
            count+=1
            #print(rd)

        elif code[i] == 'r' and count == 1:
            j = i
            while code[j] != ',':
                rs+=code[j+1]
                j+=1
            count+=1
            #print(rs)

        elif code[i] == 'r' and count == 2:
            try:
                j = i
                ctr = 0
                while ctr != 2:
                    rt = rt + code[j+1]
                    j+=1
                    ctr+=1

            except IndexError:
                j = i
                ctr = 0
                rt = ""
                while ctr != 1:
                    rt = rt + code[j+1]
                    j+=1
                    ctr+=1
            #print(rt)
    return rd,rs,rt

def bcCleaner(code):
    count = 0
    rs = ""

    for i in range(len(code)):
        if code[i] == 'r' and count == 0:
            j = i
            while code[j] != ',':
                rs+=code[j+1]
                j+=1
            count+=1

    return rs
def loadstoreChecker(code):
    count = 0
    rt = ""
    base = ""
    offset = ""

    for i in range(len(code)):
        if code[i] == 'r' and count == 0:
            j = i
            while code[j] != ',':
                rt+=code[j+1]
                j+=1
            count+=1
            #print(rt)
        elif code[i] == ',' and count == 1:
            j = i
            while code[j] != '(':
                offset += code[j+1]
                j+=1

            count+=1
            #print(offset)
        elif code[i] == '(' and count == 2:
            j = i
            while code[j] != ')':
                base += code[j+1]
                j+=1
            count+=1
            #print(base)

    return rt,offset,base

def loadstoreCleaner(rt,offset,base):
    rt = rt.rstrip(',')
    rt = rt.strip()
    offset = offset.rstrip('(')
    offset = offset.strip()
    base = base.rstrip(')')
    base = base.lstrip('r')
    base = base.strip()

    return rt,offset,base

def cleaner(rt,rs,imm):
    rt = rt.rstrip(',')
    rt = rt.strip()
    rs = rs.rstrip(',')
    rs = rs.strip()
    imm = imm.rstrip(',')
    imm = imm.strip()

    return rt,rs,imm

def opcode(code):
    #syntaxCheck = re.match(checker,code)
    syntaxCheck = True
    if syntaxCheck:
        #print ("Goods")
        if re.search(r'DADDIU',code):
            #print("NICE DADDIU NAKITA")
            opcode = '011001'
            rt,rs,imm = immediateChecker(code)
            rt,rs,imm = cleaner(rt,rs,imm)

            rtbin = '{0:05b}'.format(int(rt))
            rsbin = '{0:05b}'.format(int(rs))


            final = opcode + rsbin + rtbin
            final = hex(int(final,2))

            #print("OPCODE in hex: "+final+imm)
            final = final + imm
            print("OPCODE in hex: "+'0x' + final[2:].zfill(8))
            final2 = final[2:].zfill(8)

        elif re.search(r'XORI',code):
            #print("XORI")
            opcode = '001110'
            rt,rs,imm = immediateChecker(code)
            rt,rs,imm = cleaner(rt,rs,imm)

            '''
            print("THIS IS RT: "+rt) #5
            print("THIS IS RS: "+rs) #5
            print("THIS IS IMM: "+imm) #16
            '''

            rtbin = '{0:05b}'.format(int(rt))
            rsbin = '{0:05b}'.format(int(rs))


            final = opcode + rsbin + rtbin
            final = hex(int(final,2))

            #print("OPCODE in hex: "+final+imm)
            final = final + imm
            print("OPCODE in hex: "+'0x' + final[2:].zfill(8))
            final2 = final[2:].zfill(8)


        elif re.search(r'DADDU',code):
            #print("DADDU")
            opcode = '000000'
            sa = '00000'
            func = '101101'
            rd,rs,rt = nonImmediateChecker(code)
            rt,rs,rd = cleaner(rt,rs,rd)
            #print(rs)
            #print(rt)

            rtbin = '{0:05b}'.format(int(rt))
            rsbin = '{0:05b}'.format(int(rs))
            rdbin = '{0:05b}'.format(int(rd))

            final = opcode + rsbin + rtbin + rdbin + sa + func
            #print(final)
            final = hex(int(final,2))

            #print("OPCODE in hex: "+final)
            print("OPCODE in hex: "+'0x' + final[2:].zfill(8))
            final2 = final[2:].zfill(8)

        elif re.search(r'SLT',code):
            #print("DADDU")
            opcode = '000000'
            sa = '00000'
            func = '101010'
            rd,rs,rt = nonImmediateChecker(code)
            rt,rs,rd = cleaner(rt,rs,rd)
            #print(rs)
            #print(rt)

            rtbin = '{0:05b}'.format(int(rt))
            rsbin = '{0:05b}'.format(int(rs))
            rdbin = '{0:05b}'.format(int(rd))

            final = opcode + rsbin + rtbin + rdbin + sa + func
            #print(final)
            final = hex(int(final,2))

            #print("OPCODE in hex: "+final)
            print("OPCODE in hex: "+'0x' + final[2:].zfill(8))
            final2 = final[2:].zfill(8)

        elif re.search(r'SD',code):
            #print("SD")
            opcode = '111111'
            rt,offset,base = loadstoreChecker(code)
            rt,offset,base = loadstoreCleaner(rt,offset,base)

            #rint(rt)
            #print(offset)
            #print(base)

            rtbin = '{0:05b}'.format(int(rt))
            basebin = '{0:05b}'.format(int(base))

            final = opcode + basebin + rtbin

            final = hex(int(final,2))

            final = final + offset

            print("OPCODE in hex: "+'0x' + final[2:].zfill(8))
            final2 = final[2:].zfill(8)

        elif re.search(r'LD',code):
            opcode = '110111'
            rt,offset,base = loadstoreChecker(code)
            rt,offset,base = loadstoreCleaner(rt,offset,base)

            #rint(rt)
            #print(offset)
            #print(base)

            rtbin = '{0:05b}'.format(int(rt))
            basebin = '{0:05b}'.format(int(base))

            final = opcode + basebin + rtbin

            final = hex(int(final,2))

            final = final + offset

            print("OPCODE in hex: "+'0x' + final[2:].zfill(8))

            final2 = final[2:].zfill(8)

        elif re.search(r'BGTZ',code):
            print("BGTZ")
            opcode = '000111'
            rt = '00000'

            rs = bcCleaner(code)
            rs = rs.rstrip(',')
            rs = rs.strip()
            print(rs)
            final = opcode + rs + rt

            final = hex(int(final,2))
            print(final)
            print("OPCODE in hex: " + '0x'+final[2:].zfill(4)+" + 4 bytes of offset ")
            final2 = "n/a"
        elif re.search(r'BC',code):
            opcode = '110010'
            final2 = '0'
            print("OPCODE in Binary: " + opcode + "26-bit offset")
    else:
       print("Syntax error!")
       final2 = "Error"

    return final2


def IFFunction(code):
    try:
        VIF = IF.objects.latest('id')
    except: 
        VIF = None
    try:
        VStall = Stall.objects.latest('id')
    except: 
        VStall = None
    if VIF != None:
        IFcycle = 0
        IFrow = 0
        if VStall != None:
            if VStall.cycle < VIF.cycle:
                IFcycle = VIF.cycle + 1
            else:
                IFcycle = VStall.cycle + 1
        else:
            IFcycle = VIF.cycle + 1
        IFrow = VIF.row + 1     
        newIF = IF(cycle = IFcycle, row = IFrow, ir = code.opcode, pc = hex(code.name + 4)[2:].zfill(4).upper())
        newIF.save()
    else:
        newIF = IF(cycle = 1, row = 1, ir = code.opcode, pc =  hex(code.name + 4)[2:].zfill(4).upper())
        newIF.save()

def IDFunction(code):
    try:
        VStall = Stall.objects.latest('id')
    except: 
        VStall = None
    try:
        VID = ID.objects.latest('id')
    except: 
        VID = None
    if VID != None:
        if VStall != None:
            if VStall.cycle > VID.cycle:
                newID = ID(cycle=VStall.cycle+1, row=VStall.row)
                newID.save()
            else:
                newID = ID(cycle=VID.cycle+1, row=VID.row+1)
                newID.save()
        else:
            newID = ID(cycle=VID.cycle+1, row=VID.row+1)
            newID.save()
    else:        
        newID = ID(cycle=2, row=1)
        newID.save()

def EXFunction(code):
    try:
        VEX = EX.objects.latest('id')
    except: 
        VEX = None
    VID = ID.objects.latest('id')
    if VEX != None:
        newEX = EX(cycle=VID.cycle+1, row=VID.row)
        newEX.save()
    else:
        newEX = EX(cycle=3, row=1)
        newEX.save()

def MEMFunction(code):
    try:
        VMEM = MEM.objects.latest('id')
    except: 
        VMEM = None
    VEX = EX.objects.latest('id')
    if VMEM != None:
        newMEM = MEM(cycle=VEX.cycle+1, row=VEX.row)
        newMEM.save()
    else:
        newMEM = MEM(cycle=4, row=1)
        newMEM.save()

def WBFunction(code):
    try:
        VWB = WB.objects.latest('id')
    except: 
        VWB = None
    VMEM = MEM.objects.latest('id')
    if VWB != None:
        newWB = WB(cycle=VMEM.cycle+1, row=VMEM.row)
        newWB.save()
    else:
        newWB = WB(cycle=5, row=1)
        newWB.save()
        
def reset(request):
    registers = Register.objects.all()
    clear = MemoryClearer.objects.all()
    for x in registers:
        x.value = "0000000000000000"
        x.save()
    data = DataSegment.objects.all()
    request.session['goto'] = 0
    request.session['programCount'] = 0
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
#    while IF.objects.count():
#        IF.objects.all()[0].delete()
#    while ID.objects.count():
#        ID.objects.all()[0].delete()
#    while EX.objects.count():
#        EX.objects.all()[0].delete()
#    while MEM.objects.count():
#        MEM.objects.all()[0].delete()
#    while WB.objects.count():
#        WB.objects.all()[0].delete()
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
    request.session['programCount'] = len(programLines)
    x = 0
    for y in programMemory:
        y.value = programLines[x]
        y.opcode = opcode(programLines[x])
        y.save()
        newClearer = MemoryClearer(name=y.name, memoryType=1)
        newClearer.save()
        x = x + 1
    return render(request, 'simulator/home.html')

def pipeline(request):
    programMips = MipsProgram.objects.all().order_by('id')[:request.session['programCount']]
    for x in programMips:
        IFFunction(x)
        IDFunction(x)
        EXFunction(x)
        MEMFunction(x)
        WBFunction(x)
    return render(request, 'simulator/pipeline.html')

def purge(request):
    VIF = IF.objects.all()
    VID = ID.objects.all()
    VEX = EX.objects.all()
    VMEM = MEM.objects.all()
    VWB = WB.objects.all()
    VStall = Stall.objects.all()
    for x in VIF:
        x.delete()
    for x in VID:
        x.delete()
    for x in VEX:
        x.delete()
    for x in VMEM:
        x.delete()
    for x in VWB:
        x.delete()
    for x in VStall:
        x.delete()
    return render(request, 'simulator/home.html')