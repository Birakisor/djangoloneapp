from django.shortcuts import render
from datetime import datetime
from .forms import Loandata

# Create your views here.

def loancal(request):
    fm=Loandata()
    if request.method=='GET':
        loanDate =request.GET.get('loanDate')
        releaseDate=request.GET.get('releasedata')
        pamount=int(request.GET.get('principalAmount'))
        print(type(pamount))
        
        ldate = datetime.strptime(loanDate, "%m-%d-%Y").date()
        rdate = datetime.strptime(releaseDate, "%m-%d-%Y").date()
        diff_days=rdate-ldate
        int_days=diff_days.days

        if int_days>=360:
            year=int_days//360
            days=int_days-(year*360)
            if days>=30:
                month=int_days//30
                day=int_days-(month*30)
                print(month)
                print(day)
                print(year)

                if pamount<=5000  and year>=1:
                    intrestPerMonth=(pamount/100)*3
                    new_pamout=(intrestPerMonth*12)+pamount
                    newIntrestPerMonth=(new_pamout/100)*2
                    total_intrest=(newIntrestPerMonth*month)+(newIntrestPerMonth*day)
                    total_pay=total_intrest+pamount
                    print(total_pay)
                else:
                    intrestPerMonth=(pamount/100)*2
                    new_pamout=(intrestPerMonth*12)+pamount
                    newIntrestPerMonth=(new_pamout/100)*2
                    total_intrest=(newIntrestPerMonth*month)+(newIntrestPerMonth*day)
                    total_pay=total_intrest+pamount
                    print(total_pay)
        elif int_days>=30:
            month=int_days//30
            day=int_days-(month*30)
            print(month)
            print(day)
            if pamount<=5000:
                intrestPerMonth=(pamount/100)*3
                total_intrest=(intrestPerMonth*month)+((intrestPerMonth/30)*day)
                total_pay=pamount+total_intrest
                print(total_pay)
            else:
                intrestPerMonth=(pamount/100)*2
                total_intrest=(intrestPerMonth*month)+((intrestPerMonth/30)*day)
                total_pay=pamount+total_intrest
                print(total_pay)

        else:
            day=int_days
            print(day)
            if pamount<=5000:
                intrestPerMonth=(pamount/100)*3
                total_intrest=((intrestPerMonth/30)*day)
                total_pay=pamount+total_intrest
                print(total_pay)
            else:
                intrestPerMonth=(pamount/100)*2
                total_intrest=((intrestPerMonth/30)*day)
                total_pay=pamount+total_intrest
                print(total_pay)
        
    return render(request,'loanapp/base.html',{'form':fm,'tota_Amount':total_pay,'ldate':loanDate,'rdate':rdate,'total_pay':total_pay})
        
    

