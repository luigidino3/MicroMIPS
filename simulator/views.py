from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Register, DataSegment, MipsProgram, MemoryClearer, IF, ID, EX, MEM, WB
import re

def opcode():
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
        elif re.search(r'BC',code):
            opcode = '110010'

            print("OPCODE in Binary: " + opcode + "26-bit offset")
    else:
       print ("Syntax error!")

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