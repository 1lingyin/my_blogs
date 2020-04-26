from django.shortcuts import render
from django.http import HttpResponse
from .forms import form,data_form
import pymysql
# Create your views here.


'''
def add(request):
    # ------------------------------------------------获取到已经提交的数据，用于展示-------------------------------------------
    connect = pymysql.connect(
        host='cdb-hdoxzwau.cd.tencentcdb.com',
        port=10079,
        user='root',
        passwd='lunyang12',
        db='data',
        charset='utf8'
    )
    db = connect.cursor()
    sql = "SELECT cities,level,date_added from data_datacollect"
    db.execute(sql)
    data_show = db.fetchall()
    db.close()
    connect.close()
    # -------------------------------------------------------------------------------------------------------------------------


    if request.method == 'POST':
        data=form(request.POST)
        if data.is_valid():
            level=request.POST.get('level','')
            city=request.POST.get('cities','')
            date=request.POST.get('date','')

            #------------------------------------------------用于获取已经存在的数据----------------------------------------------------
            connect = pymysql.connect(
                host='cdb-hdoxzwau.cd.tencentcdb.com',
                port=10079,
                user='root',
                passwd='lunyang12',
                db='data',
                charset='utf8'
            )
            db = connect.cursor()
            sql1= "SELECT cities,level1,level2,level3,level4,date from DATA WHERE cities='"+str(city)+"'"+"AND"+" date='"+str(date)+"'"
            db.execute(sql1)
            data_exist = db.fetchone()
            db.close()
            connect.close()

            #------------------------------------------------用于获取已经存在的数据----------------------------------------------------
                # -------------------------------------用于更新存在的数据------------------------------------------------------------------
            if data_exist:
                data_now=data_exist[int(level)]+1
                connect = pymysql.connect(
                    host='cdb-hdoxzwau.cd.tencentcdb.com',
                    port=10079,
                    user='root',
                    passwd='lunyang12',
                    db='data',
                    charset='utf8'
                )
                db = connect.cursor()
                sql2="UPDATE DATA SET level"+str(level)+"=%s WHERE cities=%s AND date=%s"
                try:
                    db.execute(sql2,[data_now,city,date])
                    connect.commit()
                except:
                    # 有异常，回滚事务
                    connect.rollback()
                    return HttpResponse('提交失败')
                db.close()
                connect.close()
                # -------------------------------------------------------------------------------------------------------------------------

            elif not data_exist:

                # --------------------------用于创建没有的数据-----------------------------------------------------------------------------
                connect = pymysql.connect(
                    host='cdb-hdoxzwau.cd.tencentcdb.com',
                    port=10079,
                    user='root',
                    passwd='lunyang12',
                    db='data',
                    charset='utf8'
                )
                db = connect.cursor()
                sql2 = "INSERT INTO DATA(cities,level1,level2,level3,level4,date) VALUES (%s,%s,%s,%s,%s,%s)"
                try:
                    if int(level)==1:
                        db.execute(sql2, [city,1,0,0,0, date])
                    elif int(level) ==2:
                        db.execute(sql2, [city,0, 1, 0,0, date])
                    elif int(level) ==3:
                        db.execute(sql2, [city,0, 0, 1,0, date])
                    elif int(level) ==4:
                        db.execute(sql2, [city,0, 0, 0,1, date])
                    connect.commit()
                except:
                    # 有异常，回滚事务
                    connect.rollback()
                    return HttpResponse('提交失败')
                db.close()
                connect.close()
                # -------------------------------------------------------------------------------------------------------------------------
            # --------------------------------------------更新总数据-----------------------------------------------------------------------------
            connect = pymysql.connect(
                    host='cdb-hdoxzwau.cd.tencentcdb.com',
                    port=10079,
                    user='root',
                    passwd='lunyang12',
                    db='data',
                    charset='utf8'
                )
            db = connect.cursor()
            sql1 = "SELECT number from DATA_ALL WHERE cities='" + str(city) + "'"
            db.execute(sql1)
            data_exist_all = db.fetchone()
            data_exist_all_now = data_exist_all[0] + 1
            sql2 = "UPDATE DATA_ALL SET number=%s WHERE cities=%s"
            try:
                db.execute(sql2, [data_exist_all_now, city])
                connect.commit()
            except:
                # 有异常，回滚事务
                connect.rollback()
                return HttpResponse('提交失败')
                db.close()
                connect.close()

                # -------------------------------------------------------------------------------------------------------------------------
            data.save()
            return HttpResponse('提交成功')
    else:
        data=form()
    return render(request,'add.html',{'data':data,'data_show':data_show})
'''



def add_data(request):
    if request.method == 'POST':
        form=data_form(request.POST)
        if form.is_valid():
            city=request.POST.get('city','')
            province=request.POST.get('province','')
            level=request.POST.get('level','')
            disease = request.POST.get('disease', '')
            time=request.POST.get('time','')
            # ------------------------------------------------用于获取已经存在的数据----------------------------------------------------
            connect = pymysql.connect(
                host='cdb-hdoxzwau.cd.tencentcdb.com',
                port=10079,
                user='root',
                passwd='lunyang12',
                db='data',
                charset='utf8'
            )
            db = connect.cursor()
            sql1 = "SELECT city,province,level,disease,time,number from DATA_cq WHERE city='" + str(city) + "'" + "AND" + " time='" + str(time) +"'"+ "AND"+ " province='"+str(province)+"'"+"AND"+ " disease='"+str(disease)+"'"
            db.execute(sql1)
            data_exist = db.fetchone()
            db.close()
            connect.close()

            # ------------------------------------------------用于获取已经存在的数据----------------------------------------------------

            # -------------------------------------用于更新存在的数据------------------------------------------------------------------
            if data_exist:
                data_now = data_exist[5] + 1
                connect = pymysql.connect(
                    host='cdb-hdoxzwau.cd.tencentcdb.com',
                    port=10079,
                    user='root',
                    passwd='lunyang12',
                    db='data',
                    charset='utf8'
                )
                db = connect.cursor()
                sql2 = "UPDATE DATA_cq SET number=%s WHERE city=%s AND time=%s AND disease=%s AND province=%s"
                try:
                    db.execute(sql2, [data_now, city, time,disease,province])
                    connect.commit()
                except:
                    # 有异常，回滚事务
                    connect.rollback()
                    return HttpResponse('提交失败')
                db.close()
                connect.close()
                # -------------------------------------------------------------------------------------------------------------------------

            elif not data_exist:

                # --------------------------用于创建没有的数据-----------------------------------------------------------------------------
                connect = pymysql.connect(
                    host='cdb-hdoxzwau.cd.tencentcdb.com',
                    port=10079,
                    user='root',
                    passwd='lunyang12',
                    db='data',
                    charset='utf8'
                )
                db = connect.cursor()
                sql2 = "INSERT INTO DATA_cq(city,province,level,disease,time,number) VALUES (%s,%s,%s,%s,%s,%s)"
                try:
                    db.execute(sql2, [city, province, level, disease,time, 1])
                    connect.commit()
                except:
                    # 有异常，回滚事务
                    connect.rollback()
                    return HttpResponse('提交失败')
                db.close()
                connect.close()
                # -------------------------------------------------------------------------------------------------------------------------
#总数据

           # ------------------------------------------------用于获取已经存在的数据----------------------------------------------------
            connect = pymysql.connect(
                    host='cdb-hdoxzwau.cd.tencentcdb.com',
                    port=10079,
                    user='root',
                    passwd='lunyang12',
                    db='data',
                    charset='utf8'
                )
            db = connect.cursor()
            sql1 = "SELECT city,level,time,number from DATA_ALL WHERE city='" + str(city) + "'" + "AND" + " time='" + str(time) + "'"+ "AND" + " level='" + str(level) + "'"
            db.execute(sql1)
            data_exist_all = db.fetchone()
            db.close()
            connect.close()

                # ------------------------------------------------用于获取已经存在的数据----------------------------------------------------

                # -------------------------------------用于更新存在的数据------------------------------------------------------------------
            if data_exist_all:
                data_now_all= data_exist_all[3] + 1
                connect = pymysql.connect(
                        host='cdb-hdoxzwau.cd.tencentcdb.com',
                        port=10079,
                        user='root',
                        passwd='lunyang12',
                        db='data',
                        charset='utf8'
                    )
                db = connect.cursor()
                sql2 = "UPDATE DATA_ALL SET number=%s WHERE city=%s AND time=%s AND level=%s"
                try:
                    db.execute(sql2, [data_now_all, city, time,level])
                    connect.commit()
                except:
                        # 有异常，回滚事务
                    connect.rollback()
                    return HttpResponse('提交失败')
                db.close()
                connect.close()
                # -------------------------------------------------------------------------------------------------------------------------

            elif not data_exist_all:

                # --------------------------用于创建没有的数据-----------------------------------------------------------------------------
                connect = pymysql.connect(
                        host='cdb-hdoxzwau.cd.tencentcdb.com',
                        port=10079,
                        user='root',
                        passwd='lunyang12',
                        db='data',
                        charset='utf8'
                    )
                db = connect.cursor()
                sql2 = "INSERT INTO DATA_ALL(city,level,disease,time,number) VALUES (%s,%s,%s,%s,%s)"
                try:
                        db.execute(sql2, [city, level, disease, time, 1])
                        connect.commit()
                except:
                        # 有异常，回滚事务
                    connect.rollback()
                    return HttpResponse('提交失败')
                db.close()
                connect.close()
                    # -------------------------------------------------------------------------------------------------------------------------
            form.save()
            return HttpResponse('提交成功')
    else:
        form=data_form()
    return render(request,'add_data_cq.html',{'form':form})


