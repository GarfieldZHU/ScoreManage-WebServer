import datetime
from django.db import models
from django.utils import timezone


class Student(models.Model):
    sid = models.CharField(max_length=15, primary_key=True)
    sname = models.CharField(max_length=20)
    spwd = models.CharField(max_length=15)
    gender = models.CharField(max_length=8)
    age = models.IntegerField(default=18)

    def __unicode__(self):
        return self.sid


class Teacher(models.Model):
    tid = models.CharField(max_length=15, primary_key=True)
    tname = models.CharField(max_length=20)
    tpwd = models.CharField(max_length=15)
    gender = models.CharField(max_length=8)
    workage = models.IntegerField(default=0)

    def __unicode__(self):
        return self.tid


class Class(models.Model):
    clsid = models.CharField(max_length=15, primary_key=True)

    def __unicode__(self):
        return self.clsid


class Course(models.Model):
    cid = models.CharField(max_length=15, primary_key=True)
    #tid = models.CharField(max_length=10)
    cname = models.CharField(max_length=20, default="")
    teacher = models.ForeignKey(Teacher, to_field='tid')
    credit = models.IntegerField(default=0)
    semester = models.CharField(max_length=8)
    period = models.IntegerField(default=0)

    def __unicode__(self):
        return self.cid


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, to_field='sid')
    course = models.ForeignKey(Course, to_field='cid')
    grade = models.CharField(max_length=8)
