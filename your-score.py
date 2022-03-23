score = int (input("Enter your score :"))

if score >= 90:
    if score >= 95:
        Score_letter="A+"
    else:
        Score_letter="A"
elif score >= 80:
    if score >= 85:
        Score_letter="B+"
    else:
        Score_letter="B"
if score >= 70 :
      if score >= 75 :
        Score_letter="B+"
      else :
       score_letter= "B"


print ("Your degree: %s" % Score_letter)
