hour = int(input('Enter hour: '))
am = "am" if input('am(1) or pm(2)? ') == '1' else "pm"
ahead = int(input('How many hours ahead? '))
if ((hour + ahead)//12)%2 == 0:
    print(f"new hour {(hour + ahead)%12}  {am}")
else:
    print(f"new hour {(hour + ahead)%12}  {'am' if am == 'pm' else 'pm'}")
    