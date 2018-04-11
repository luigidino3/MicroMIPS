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
    
    def __int__(self):
        return self.name
    
class MemoryClearer(models.Model):
    name = models.IntegerField(default=0)
    memoryType = models.IntegerField(default=0)
    
    def __int__(self):
        return self.name
	
class IF(models.Model):
	name = models.IntegerField(default=0)
	opcode = models.CharField(blank=True, null=True, max_length=8)
	npc = models.IntegerField(default=0)
	pc = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name
	
class ID(models.Model):
	name = models.IntegerField(default=0)
	opcode = models.CharField(blank=True, null=True, max_length=8)
	a = models.IntegerField(default=0)
	b = models.IntegerField(default=0)
	imm = models.IntegerField(default=0)
	npc = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name
	
class EX(models.Model):
	name = models.IntegerField(default=0)
	opcode = models.CharField(blank=True, null=True, max_length=8)
	aluoutput = models.IntegerField(default=0)
	cond = models.IntegerField(default=0)
	b = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name
	
class MEM(models.Model):
	name = models.IntegerField(default=0)
	opcode = models.CharField(blank=True, null=True, max_length=8)
	lmd = models.IntegerField(default=0)
	aluoutput = models.IntegerField(default=0)
	memoryrange = models.CharField(blank=True, null=True, max_length=8)
	
	def __int__(self):
		return self.name
	
class WB(models.Model):
	name = models.IntegerField(default=0)
	opcode = models.CharField(blank=True, null=True, max_length=8)
	result = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name
	
class Stall(models.Model):
	name = models.IntegerField(default=0)
	
	def __int__(self):
		return self.name