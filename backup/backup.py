import os;
import shutil;
import time;

def main():
    deleted_folder_count=0
    deleted_file_count=0
    days=30
    path=input("Enter path")

    seconds=time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder,folders,files in os.walkpath(path):
            if seconds>file_folder_age(root_folder):
                delete_folder(root_folder)
                deleted_folder_count+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    seconds>file_folder_age(folder_path)
                    delete_folder(folder)
                    deleted_folder_count+=1
                    
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    delete_file(file_path)
                    deleted_file_count+=1
        else:
            print(f'"{path}"is not found')
            print(f"Total files deleted:  {deleted_file_count}")
            print(f"Total folder deleted:  {deleted_folder_count}")
                    

            
                
def file_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime

def delete_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable TO delete "+ path)

def delete_file(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print(f"Unable To Delete "+ path)

if __name__=="main":
    main()