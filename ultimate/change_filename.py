import os
import os.path
from pickle import FALSE, TRUE
import random
from Generate_Title import *
import glob

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



#can be a separate product from viral title pro. Will have it's own simple GUI and will be a free bonus software

staging_dir="C:\\Users\\Brandon\\Desktop\\MINIGOLFUS\\exports\\_STAGING\\experiment-616"
#staging_dir="D:\\carmanjaro\\renamer"
file_list = ""
subject = "golf shot"
titles = []
tags = "#shorts #minigolf #golf"
file_extension = ".mp4"

def get_files(staging_dir):       # 1.Get file names from directory
    #file_list=os.listdir(staging_dir)
    #print ("Files in selected directory: "+str(file_list))
    
    # Get list of all files in a given directory sorted by name
    file_list = sorted( filter( lambda x: os.path.isfile(os.path.join(staging_dir, x)),
                        os.listdir(staging_dir) ) )
    for file_name in file_list:
      print(file_name)
    
    return (file_list)

def generate_filename_handler(subject,tags):
  new_title = generate_title(subject,tags)
  if "|" in new_title:
    new_title = new_title.replace("|", " - ")
  if "..." in new_title:
    new_title = new_title.replace("...", " - ")
  if "This World" in new_title:
    new_title = new_title.replace("This World", "The World")
  
  filename = new_title+" "+tags+file_extension
  print("New filename: "+filename)
  return filename


def rename_files_handler(files, staging_dir):
  os.chdir(staging_dir)

  print("Looping through current files in directory: "+staging_dir)
  for index, old_filename in enumerate(files):
    print (index, ",",old_filename)
    print("current filename:"+files[index])
        
    filename = generate_filename_handler(subject,tags)
    file_exists = os.path.exists(filename)

    while file_exists:
      print("File exists already, finding a different name...")
      filename = generate_filename_handler(subject,tags)
      file_exists = os.path.exists(filename)

    print("--")
    try:
      print("trying to rename files")
      os.rename(files[index], filename)   
        
    except FileExistsError:
      print("File already exists, trying different name...")
          
    except:
      print("An exception occurred")
      return False

    #iteration
    print("--------------")
  
  #End Loop
  print("Finished Changing Filenames for "+str(index+1)+" files")
  print ("DONE")
  return True
    


file_list = get_files(staging_dir)
Success = rename_files_handler(file_list, staging_dir)







#for file in os.listdir('title_staging'):
#    exit;



