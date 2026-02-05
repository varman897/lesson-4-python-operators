print("Enter marks obtained in 4 subjects:")
math=int(input("math:"))
science=int(input("science:"))
english=int(input("english:"))
history=int(input("history:"))

sum=math+science+english+history
print("sum of math, science, english, and history is")
perc=(sum/400) *100
print(end="Percentage Mark=")
print(perc)