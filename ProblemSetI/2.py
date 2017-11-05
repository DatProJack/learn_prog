days=float(raw_input("How many days in a year(of your imaginary planet)? "))
while days>1:
    days=days-1
global leap
global day
global years
years=int(1)
day=int(0)
leap = float(days)
while leap >0.05:
    years=years+1
    leap=leap+days
    if(leap>=1):
        day=day+1
        leap=leap-1
print "Your leap year: Add " +`day`+" day(s)" + "every" + `years` + "year(s)."
