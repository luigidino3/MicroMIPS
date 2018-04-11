# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Register, DataSegment, MipsProgram, MemoryClearer, IF, ID, EX, MEM, WB,Table, memoryComparer

admin.site.register(Register)
admin.site.register(DataSegment)
admin.site.register(MipsProgram)
admin.site.register(MemoryClearer)
admin.site.register(IF)
admin.site.register(ID)
admin.site.register(EX)
admin.site.register(MEM)
admin.site.register(WB)
admin.site.register(Table)
admin.site.register(memoryComparer)