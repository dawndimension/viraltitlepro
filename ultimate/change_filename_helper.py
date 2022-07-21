import subprocess
import os
import webbrowser
import time
import glob
import shutil

def openBrowser(url):
    webbrowser.open(url, new=2)

def openFolder(upload_dir):
  """Windows-only option that opens file explorer to upload directory"""  
  subprocess.Popen("explorer "+convert_to_win_path(upload_dir)+"")

def convert_to_win_path(orig_path):
  win_path = orig_path.replace("/", "\\")
  return win_path


def get_uploads_dir_name():
    parent_dir = get_my_documents_dir()
    # Directory name
    epoch_time = int(time.time())
    directory = "vtptemp_"+str(epoch_time)
    uploads_dir_path = os.path.join(parent_dir, directory)
    return uploads_dir_path


def create_uploads_dir(uploads_dir_name):    
    os.mkdir(uploads_dir_name)
    print("Directory '%s' created" %uploads_dir_name)
    

def get_my_documents_dir():
  """Assume vtp folder exists for now in my documents, later define logic to check if exists etc."""
  start_path = str((os.path.expanduser('~\\Documents\\vtp')))
  mydocs_path = start_path.replace("\\", "/")
  return mydocs_path


def delete_extra_folders(docs_dir):
    """If the generated temp folders exceed 3, then this function will delete 1 folder, to keep the count at 3."""
    # get a recursive list of file paths that matches pattern including sub directories
    fileList = glob.glob(convert_to_win_path(docs_dir)+"/vtptemp_*", recursive=True)
    
    if len(fileList) > 2:
        # Iterate over the list of filepaths & remove each file.
        del_counter = 0
        for filePath in fileList:
            try:
                print("deleting "+filePath)
                shutil.rmtree(filePath)
                del_counter += 1
                if del_counter == 1:
                    return
            except OSError:
                print("Error while deleting file")
        print("===")
 
