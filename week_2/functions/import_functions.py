# Import a function from another file


from functions  import totalMarks 


maths = int(input("Maths: "))
english = int(input("English: "))
kiswahili = int(input("Kiswahili: "))



total = totalMarks(maths, english, kiswahili)
print(total)
