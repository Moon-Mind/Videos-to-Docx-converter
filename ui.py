import os

temp="Temp/"+"test"+".md"
temo="Temp/"+"test"+".docx"

#export to file
print("Export to Word")
os.system("pandoc -o"+ temo+" "+temp )
print("complete")
# clean up
#os.rename("Temp/"+temp+".docx ", temp)
#os.system("rm Temp/"+name+'.md')
#os.system("rm Temp/audio.mp4")
#os.system('rm -r Temp/Data')