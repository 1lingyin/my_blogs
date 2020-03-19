from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import form
import pymysql
connect = pymysql.connect(
    host='cdb-hdoxzwau.cd.tencentcdb.com',
    port=10079,
    user='root',
    passwd='lunyang12',
    db='data',
    charset='utf8'
)
db=connect.cursor()
# Create your views here.
def add(request):
    sql = "SELECT cities,level,date_added from data_datacollect"
    db.execute(sql)
    data_show = db.fetchall()
    if request.method == 'POST':
        data=form(request.POST)
        if data.is_valid():
            level=request.POST.get('level','')
            city=request.POST.get('cities','')
            date=request.POST.get('date','')
            sql1= "SELECT cities,level1,level2,level3,date from DATA WHERE cities='"+str(city)+"'"+"AND"+" date='"+str(date)+"'"
            db.execute(sql1)
            data_exist=db.fetchone()
            if data_exist:
                data_now=data_exist[int(level)]+1
                sql2="UPDATE DATA SET level"+str(level)+"=%s WHERE cities=%s AND date=%s"
                db.execute(sql2,[data_now,city,date])
                connect.commit()
            elif not data_exist:
                sql2 = "INSERT INTO DATA(cities,level1,level2,level3,date) VALUES (%s,%s,%s,%s,%s)"
                if int(level)==1:
                    db.execute(sql2, [city,1,0,0, date])
                elif int(level) ==2:
                    db.execute(sql2, [city, 0, 1, 0, date])
                elif int(level) ==3:
                    db.execute(sql2, [city, 0, 0, 1, date])
                connect.commit()
            data.save()
            return HttpResponseRedirect('/add/')
    else:
        data=form()
    return render(request,'add.html',{'data':data,'data_show':data_show})
