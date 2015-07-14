#coding=utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json

def index(request):
    return render_to_response('scores/login.html', {})

@csrf_exempt
def login(request):
    #tempalte = loader.get_template('scores/login.html')
    #return render(request, 'scores/login.html', {})

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print username, password
        if username == 'admin' and password == 'admin':
            response = HttpResponseRedirect('/scores/manage')
            response.set_cookie('username', username)
            return response
        elif Student.objects.filter(sid=username, spwd=password):
            response = HttpResponseRedirect('/scores/student')
            response.set_cookie('username', username)
            return response
        elif Teacher.objects.filter(tid=username, tpwd=password):
            response = HttpResponseRedirect('/scores/teacher')
            response.set_cookie('username', username)
            return response

    return render_to_response('scores/login.html', {})

@csrf_exempt
def student(request):
    if request.method == 'GET':
        username = request.COOKIES['username']
        #print username
        msg = {}
        res = []
        msg['StudentName'] = Student.objects.get(sid=username).sname
        msg['StudentCard'] = Student.objects.get(sid=username).sid
        msg['StudentGender'] = Student.objects.get(sid=username).gender
        msg['StudentAge'] = Student.objects.get(sid=username).age
        for i in StudentCourse.objects.filter(student_id=username):
            item = []
            item.append(i.course.cid)
            item.append(i.course.cname)
            item.append(i.course.teacher.tname)
            item.append(i.course.credit)
            item.append(i.grade)
            #print item
            res.append(item)
        msg['StudentList'] = res
        response = render_to_response('scores/student.html', msg)
        return response

    return render_to_response('scores/student.html', {})

@csrf_exempt
def teacher(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        username = request.COOKIES['username']
        #print username
        msg = {}
        res = []
        msg['TeacherName'] = Teacher.objects.get(tid=username).tname
        msg['WorkCard'] = Teacher.objects.get(tid=username).tid
        msg['TeacherGender'] = Teacher.objects.get(tid=username).gender
        msg['WorkAge'] = Teacher.objects.get(tid=username).workage
        if cid == None:
            for i in Course.objects.filter(teacher_id=username):
                #查找该教师所授的所有课程
                count = 0
                for j in StudentCourse.objects.filter(course_id=i.cid):
                    #查找该课程下所有选课学生的信息
                    item = []
                    item.append(i.cid)
                    item.append(i.cname)
                    item.append(j.student.sid)
                    item.append(j.student.sname)
                    item.append(j.grade)
                    #print item
                    res.append(item)
                    count += 1
                msg['count1'] = len(StudentCourse.objects.filter(course_id=i.cid, grade__lt=60))
                msg['count2'] = len(StudentCourse.objects.filter(course_id=i.cid, grade__gte=60, grade__lt=70))
                msg['count3'] = len(StudentCourse.objects.filter(course_id=i.cid, grade__gte=70, grade__lt=80))
                msg['count4'] = len(StudentCourse.objects.filter(course_id=i.cid, grade__gte=80, grade__lt=90))
                msg['count5'] = len(StudentCourse.objects.filter(course_id=i.cid, grade__gte=90, grade__lte=100))
                msg['percent1'] = '%.3f' % (msg['count1'] / float(count))
                msg['percent2'] = '%.3f' % (msg['count2'] / float(count))
                msg['percent3'] = '%.3f' % (msg['count3'] / float(count))
                msg['percent4'] = '%.3f' % (msg['count4'] / float(count))
                msg['percent5'] = '%.3f' % (msg['count5'] / float(count))
                msg['course_name'] = i.cname
            #print count, msg['percent4']
            msg['StudentList'] = res
        else:
            count = 0
            cname = Course.objects.get(cid=cid).cname
            for j in StudentCourse.objects.filter(course_id=cid):
                #查找该课程下所有选课学生的信息
                item = []
                item.append(cid)
                item.append(cname)
                item.append(j.student.sid)
                item.append(j.student.sname)
                item.append(j.grade)
                #print item
                res.append(item)
                count += 1
            msg['count1'] = len(StudentCourse.objects.filter(course_id=cid, grade__lt=60))
            msg['count2'] = len(StudentCourse.objects.filter(course_id=cid, grade__gte=60, grade__lt=70))
            msg['count3'] = len(StudentCourse.objects.filter(course_id=cid, grade__gte=70, grade__lt=80))
            msg['count4'] = len(StudentCourse.objects.filter(course_id=cid, grade__gte=80, grade__lt=90))
            msg['count5'] = len(StudentCourse.objects.filter(course_id=cid, grade__gte=90, grade__lte=100))
            msg['percent1'] = '%.3f' % (msg['count1'] / float(count))
            msg['percent2'] = '%.3f' % (msg['count2'] / float(count))
            msg['percent3'] = '%.3f' % (msg['count3'] / float(count))
            msg['percent4'] = '%.3f' % (msg['count4'] / float(count))
            msg['percent5'] = '%.3f' % (msg['count5'] / float(count))
            msg['course_name'] = cname
        #print count, msg['percent4']
            msg['StudentList'] = res

        response = render_to_response('scores/teacher.html', msg)
        return response

    elif request.method == 'POST':

        response = render_to_response('scores/teacher.html', msg)
        return response

    return render_to_response('scores/teacher.html', {})

@csrf_exempt
def manage(request):
    if request.method == 'GET':
        username = request.COOKIES['username']
        msg = {}
        human = []
        course = []
        #根据数据表填写人员信息
        for j in Teacher.objects.all():
            item = []
            item.append(j.tid)
            item.append(j.tname)
            item.append('教师')
            item.append(j.gender)
            item.append(j.workage)
            item.append(j.tpwd)
            human.append(item)
        for i in Student.objects.all():
            item = []
            item.append(i.sid)
            item.append(i.sname)
            item.append('学生')
            item.append(i.gender)
            item.append(i.age)
            item.append(i.spwd)
            human.append(item)
        msg['HumanList'] = human
        #根据数据表填写课程信息
        for i in Course.objects.all():
            item = []
            item.append(i.cid)
            item.append(i.cname)
            item.append(i.teacher.tname)
            item.append(i.teacher.tid)
            item.append(i.credit)
            item.append(i.semester)
            item.append(i.period)
            sum_grade = 0
            count = 0
            for j in StudentCourse.objects.all():
                if j.course_id == i.cid:
                    sum_grade += j.grade
                    count += 1
            if count == 0:
                avg = 0
            else:
                avg = sum_grade / count
            item.append('%.1f' % avg)
            course.append(item)
        msg['CourseList'] = course

        response = render_to_response('scores/manage.html', msg)
        return response
    return render_to_response('scores/manage.html', {})


def logout(request):
    response = HttpResponseRedirect('login')
    response.delete_cookie("username")
    return response

@csrf_exempt
def password(request):
    if request.method == 'POST':
        old_pwd = request.POST.get('old')
        new_pwd = request.POST.get('new')
        repeat_pwd = request.POST.get('repeat')

        username = request.COOKIES['username']
        if Student.objects.filter(sid=username, spwd=old_pwd) and new_pwd == repeat_pwd:
            Student.objects.filter(sid=username).update(spwd = new_pwd)
            return HttpResponseRedirect('/scores/student')
        elif Teacher.objects.filter(tid=username, tpwd=old_pwd) and new_pwd == repeat_pwd:
            Teacher.objects.filter(tid=username).update(tpwd = new_pwd)
            return HttpResponseRedirect('/scores/teacher')

@csrf_exempt
def human(request):
    if request.method == 'POST':
        subtype = request.POST.get('subtype')
        table = request.POST.get('table')
        data = json.loads(table)
        for item in data:
            i_num = item['Num']
            i_name = item['Name']
            i_kind = item['Type']
            i_gender = item['Gender']
            i_age = item['Age']
            i_pwd = item['Passwd']
            #print num,name,kind
            if subtype == 'del':
                if Student.objects.filter(sid=i_num):
                    #删除学生时先删除选课关系
                    for choice in StudentCourse.objects.all():
                        if choice.student_id == i_num:
                            choice.delete()
                    s = Student.objects.get(sid=i_num)
                    s.delete()
                elif Teacher.objects.filter(tid=i_num):
                    #删除教师时先删除对应课程
                    for course in StudentCourse.objects.all():
                        #删课程先删除对应的选课关系
                        for sc in StudentCourse.objects.all():
                            if sc.course_id == course.cid:
                                sc.delete()
                        if course.teacher_id == i_num:
                            course.delete()
                    t = Teacher.objects.get(tid=i_num)
                    t.delete()
            elif subtype == 'change':
                if Student.objects.filter(sid=i_num):
                    #修改学生
                    s = Student.objects.get(sid=i_num)
                    s.sname = i_name
                    s.spwd = i_pwd
                    s.gender = i_gender
                    s.age = i_age
                    s.save()
                elif Teacher.objects.filter(tid=i_num):
                    #修改老师
                    t = Teacher.objects.get(tid=i_num)
                    t.tname = i_name
                    t.tpwd = i_pwd
                    t.gender = i_gender
                    t.workage = i_age
                    t.save()
                elif i_kind == u'学生':
                    #新建学生
                    s = Student(sid=i_num, sname=i_name, spwd=i_pwd, gender=i_gender, age=i_age)
                    print s.sid,s.sname,s.spwd,s.gender,s.age
                    s.save()
                elif i_kind == u'教师':
                    #新建老师
                    t = Teacher(tid=i_num,tname=i_name, tpwd=i_pwd, gender=i_gender, workage=i_age)
                    t.save()

    return HttpResponseRedirect('/scores/manage')

@csrf_exempt
def grade(request):
    if request.method == 'POST':
        res = request.POST.get('grade')
        data = json.loads(res)
        for item in data:
            i_cid = item['cid']
            i_sid = item['sid']
            i_grade = item['grade']
            #print i_cid, i_sid, i_grade
            StudentCourse.objects.filter(student_id=i_sid, course_id=i_cid).update(grade=i_grade)

    return HttpResponseRedirect('/scores/teacher')


@csrf_exempt
def course(request):
    if request.method == 'POST':
        subtype = request.POST.get('subtype1')
        table = request.POST.get('table1')
        data = json.loads(table)
        for item in data:
            i_num = item['Num']
            i_name = item['Name']
            i_teacher = item['Teacher']
            i_tid = item['Tid']
            i_credit = item['Credit']
            i_sem = item['Semester']
            i_per = item['Period']

            if subtype == 'del':
                if Course.objects.filter(cid=i_num):
                    #删除课程先删除选课关系
                    for item in StudentCourse.objects.all():
                        if item.course_id == i_num:
                            item.delete()
                    c = Course.objects.get(cid=i_num)
                    c.delete()

            elif subtype == 'change':
                if Course.objects.filter(cid=i_num):
                    #修改
                    c = Course.objects.get(cid=i_num)
                    c.cname = i_name
                    c.teacher = Teacher.objects.get(tid=i_tid)
                    c.credit = i_credit
                    c.semester = i_sem
                    c.period = i_per
                    c.save()
                else:
                    #新建
                    c = Course(cid=i_num, cname=i_name, credit=i_credit, semester=i_sem, period=i_per, teacher=Teacher.objects.get(tid=i_tid))
                    c.save()

    return HttpResponseRedirect('/scores/manage')
