# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=3)
    value = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name
    
class DataSegment(models.Model): #512
    name = models.IntegerField(default=0)
    value = models.CharField(blank=True, null=True, max_length=16)
    
    def __int__(self):
        return self.name
    
class MipsProgram(models.Model): #1024
    name = models.IntegerField(default=0)
    value = models.CharField(blank=True, null=True, max_length=500)
    opcode = models.CharField(blank=True, null=True, max_length=10)
    def __int__(self):
        return self.name
    
class MemoryClearer(models.Model):
    name = models.IntegerField(default=0)
    memoryType = models.IntegerField(default=0)
    
    def __int__(self):
        return self.name
	
class IF(models.Model):
    cycle = models.IntegerField(default=0)
    row = models.IntegerField(blank=True, null=True, max_length=16)
    ir = models.CharField(blank=True, null=True, max_length=16)
    pc = models.CharField(blank=True, null=True, max_length=16)
    
    def __int__(self):
        return self.name
	
class ID(models.Model):
    cycle = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    a = models.CharField(blank=True, null=True, max_length=16)
    b = models.CharField(blank=True, null=True, max_length=16)
    imm = models.CharField(blank=True, null=True, max_length=16)
    ir = models.CharField(blank=True, null=True, max_length=16)
	
    def __int__(self):
        return self.name
	
class EX(models.Model):
    cycle = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    aluoutput = models.CharField(blank=True, null=True, max_length=16)
    cond = models.CharField(blank=True, null=True, max_length=16)
    b = models.CharField(blank=True, null=True, max_length=16)
    ir = models.CharField(blank=True, null=True, max_length=16)
    
    def __int__(self):
        return self.name
	
class MEM(models.Model):
    cycle = models.IntegerField(default=0)
    row = models.IntegerField(default=0)
    lmd = models.CharField(blank=True, null=True, max_length=16)
    aluoutput = models.CharField(blank=True, null=True, max_length=16)
    memoryrange = models.CharField(blank=True, null=True, max_length=32)
    ir = models.CharField(blank=True, null=True, max_length=16)
    
    def __int__(self):
        return self.name
	
class WB(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(default=0)
	result = models.CharField(blank=True, null=True, max_length=16)
	def __int__(self):
		return self.name
	
class Stall(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(blank=True, null=True, max_length=16)
	
	def __int__(self):
		return self.name

class Table(models.Model):
	CIF = models.IntegerField(default=0)
	CID = models.IntegerField(default=0)
	CEX = models.IntegerField(default=0)
	CMEM = models.IntegerField(default=0)
	CWB = models.IntegerField(default=0)
	CYCLE = models.IntegerField(default=0)
	CSTALL = models.IntegerField(default=0)
	POSITION = models.IntegerField(default=0)
	SPACE = models.IntegerField(default=0)

	def __init__(self):
		return self.name