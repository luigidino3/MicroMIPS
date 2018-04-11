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
	row = models.IntegerField(default=0)
	npc = models.IntegerField(default=0)
	pc = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name
	
class ID(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(default=0)
	a = models.CharField(default=0)
	b = models.CharField(default=0)
	imm = models.CharField(default=0)
	npc = models.CharField(default=0)
	
	def __int__(self):
		return self.name
	
class EX(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(default=0)
	aluoutput = models.CharField(default=0)
	cond = models.CharField(default=0)
	b = models.CharField(default=0)
	
	def __int__(self):
		return self.name
	
class MEM(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(default=0)
	lmd = models.CharField(default=0)
	aluoutput = models.CharField(default=0)
	memoryrange = models.CharField(blank=True, null=True, max_length=8)
	
	def __int__(self):
		return self.name
	
class WB(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(default=0)
	result = models.CharField(default=0)
	
	def __int__(self):
		return self.name
	
class Stall(models.Model):
	cycle = models.IntegerField(default=0)
	row = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name