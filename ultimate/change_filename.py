import os
from pickle import TRUE
import random
# importing all the
# functions defined in test.py
#from test import *

#try https://pypi.org/project/grammar-check/ after generating the title to fix it.

#todo for each file in dir, run generate_title and rename file to that, then copy to upload folder. for now I will hard code a title name to return so it can work. later implement
#youtube api to upload. for me, python can always be running, and triggered when I drag files to that folder. drag files to folder, they get put in upload folder with names. then manually upload 
#them to youtube. when I design desktop app, people can drag files into app, or browse for them. it will work the same way though. use a temp folder then bring them to upload.
#later can upload them automatically. maybe have a preset scheduling options, and customizeable way. 1 a day at x. 1 every 15 minutes starting at x. max of 8? with api
#for now do everything in here, later organize

#test code
#os.chdir(r"title_staging")
#old_file_name = "new2.txt"
#new_file_name = "new2.txt"
#os.rename(old_file_name, new_file_name)
#print(old_file_name + " renamed to " + new_file_name);
# end test code

staging_dir="title_staging"
file_list = ""
subject = "putt"
titles = []

def get_files(staging_dir):       # 1.Get file names from directory
    file_list=os.listdir(staging_dir)
    print (file_list)
    return (file_list)

#2 options. generate and rename each at a time, or generate all titles, and then rename all files. Test later what quicker. start with gen all, rename all
def generate_title_main(file_count):
  print("There are "+ str(file_count) + " video file(s)")
  #generate file_count titles
  #create and return array or something of titles
  demo_titles = ["Craziest putt you'll ever see #shorts.mp4", "Wildest Putt this century #shorts.mp4", "Luckiest Hole in One #shorts.mp4", "Coolest Putt this Decade #shorts.mp4", "Best Shot of the Year #shorts.mp4"]
  for x in range(file_count):
    titles.append(random.choice(demo_titles))    
  return titles

#better to just select random name at renaming step?
def rename_files(files, new_titles):
    index = 0
    #overwrite bc issue
    files = os.listdir(staging_dir)
    os.chdir(r"title_staging")
    for i in files:
        print(i)
        print(index)
        print("current files:"+files[index])
        print("new titles:"+new_titles[index])
        os.rename(files[index], new_titles[index])
        index += 1
    return TRUE


file_list = get_files(staging_dir)
titles = generate_title_main(len(file_list))
Success = rename_files(file_list, titles)







#for file in os.listdir('title_staging'):
#    exit;



