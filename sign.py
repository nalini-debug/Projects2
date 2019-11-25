import datetime
from datetime import timedelta, date



#Welcome text
print("Hello! "
      "\n welcome to Know your sign better website")

# to take name of the user
a=input('enter the name:-')
if a.isalpha():
        print('Welcome {} wait while we configure your sign'.format(a))
else:
     print("enter valid name")


# to take their date of birth
print('enter the date of birth in format as Ex:- March-10-2019\n')
try:
    k=input('date:-')
    o=k
    j=datetime.datetime.strptime(o, " %B-%d-%Y")
    print('your date of birth is:')
    p=j.date()
    print(p)

    if (p.strftime("%B")=="January"):
      if(p.day<=22):
        print('capricorn')
      else:
       print('Auarious')

    elif (p.strftime("%B") == "February"):
     if(p.day<= 18):
         print('Aquarious')
     else:
         print('pieces')

    elif (p.strftime("%B") == "March"):
       if (p.day <= 20):
          print('Pieces')
       else:
          print('Aries')

    elif (p.strftime("%B") == "April"):
      if (p.day <= 19):
         print('Aries')
      else:
         print('Taurus')

    elif (p.strftime("%B") == "May"):
        if (p.day <= 20):
            print('Taurus')
        else:
            print('gemini')
    elif (p.strftime("%B") == "June"):
        if (p.day <= 20):
            print('gemini')
        else:
            print('cancer')
    elif (p.strftime("%B") == "Jully"):
            if (p.day <= 22):
                print('cancer')
            else:
                print('leo')
    elif (p.strftime("%B") == "August"):
            if (p.day <= 22):
                print('leo')
            else:
                print('virgo')
    elif (p.strftime("%B") == "September"):
            if (p.day <= 22):
                print('Virgo')
            else:
                print('Libra')
    elif (p.strftime("%B") == "October"):
        if (p.day <= 22):
            print('Libra')
        else:
            print('Scorpio')
    elif (p.strftime("%B") == "November"):
        if (p.day <= 21):
            print('Scorpio')
        else:
            print('Sagittarius')
    elif (p.strftime("%B") == "December"):
        if (p.day <= 21):
            print('Sagittarius')
        else:
            print('Capricorn')



except ValueError:
    print("enter the date in valid format")

