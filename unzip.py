import os
import glob
import zipfile
import shutil


base_path = os.getcwd()
path = base_path + '/changed_opening'
zips = glob.glob('./zip_dir/*.zip')

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('작업 폴더 생성')
    else:
        # 해당 디렉토리 삭제
        shutil.rmtree(r'%s' %base_path +'/changed_opening')
        print('작업 폴더 삭제')
 
createFolder('./changed_opening')

# print(zips)

# 모든 zip파일을 원하는 경로에 압축 풀기
def unziped(zipFile, path):
    with zipfile.ZipFile(zipFile, 'r') as existing_zip:
            existing_zip.extractall(path)


for i in range(len(zips)):
    os.makedirs(path + '/' + zips[i].replace("./zip_dir\\","").replace(".zip",""))

    
all_dir = glob.glob(path + '/*')
# print(all_dir)

for j in range(len(all_dir)):
     unziped(zips[j], all_dir[j])


opening_dir = base_path + '/opening'
changed_dir = base_path + '/changed_opening'

reading_dir = base_path + '/reading'

opening_list = os.listdir(opening_dir)
changed_list = os.listdir(changed_dir)

reading_list = os.listdir(reading_dir)

rm_dir_path = changed_dir 
rm_dir_list = os.listdir(changed_dir)

# print(changed_list)

def removeDirs(index_path, list_path):
    for dir in range(4):

      if dir == 2:
         os.remove(index_path + '/' + list_path[dir])
      else: 
         shutil.rmtree(index_path + '/' + list_path[dir])


def removeReadingDirs(index_path, list_path):
   
    for dir in range(6):
      
      if dir == 1:
          continue
      elif dir == 3:
         os.remove(index_path + '/' + list_path[dir])
      elif dir == 4:
          continue
      else: 
         shutil.rmtree(index_path + '/' + list_path[dir])


def copyDirs(index_path, list_path):
    for dir in range(4):
 
      if dir == 2:
         shutil.copy(opening_dir + '/' + opening_list[dir], index_path + '/' + list_path[dir])
      else: 
         shutil.copytree(opening_dir + '/' + opening_list[dir], index_path +'/'+ opening_list[dir])


def copyReadingDirs(index_path, list_path):
    for dir in range(6):
      if dir == 1:
          continue
      elif dir == 3:
         shutil.copy(reading_dir + '/' + reading_list[dir], index_path + '/' + list_path[dir])
      elif dir == 4:
          continue
      else: 
         shutil.copytree(reading_dir + '/' + reading_list[dir], index_path +'/'+ reading_list[dir])


def checkDirLastName(list):
    for idx, val in enumerate(changed_list):
        change_path = path + '/' + val
        change_list = os.listdir(change_path)

        for jdx, wal in enumerate(change_list):

            if '_01' in wal:
                rm_dir_path = changed_dir + '/' + changed_list[idx] + '/' + change_list[jdx]
                rm_dir_list = os.listdir(changed_dir + '/' + changed_list[idx] + '/' + change_list[jdx])
                removeDirs(rm_dir_path, rm_dir_list)
                copyDirs(rm_dir_path, rm_dir_list)
                print( wal + ' 책 열기 교체 완료')
            elif '_s.png' in wal:
                continue    
            else:
                rm_dir_path = changed_dir + '/' + changed_list[idx] + '/' + change_list[jdx]
                rm_dir_list = os.listdir(changed_dir + '/' + changed_list[idx] + '/' + change_list[jdx])
                removeReadingDirs(rm_dir_path, rm_dir_list)
                copyReadingDirs(rm_dir_path, rm_dir_list)
                print( wal + ' 책 읽기 교체 완료')


checkDirLastName(changed_list)

owd = os.getcwd()
print('모든 폴더 교체 완료')

def zip_all_dir(need_dir):
    os.chdir(path)
    fantasy_zip = zipfile.ZipFile( base_path + '/finish_zip/' + need_dir + '.zip', 'w')
    
    for folder, subfolders, files in os.walk(path + '/' + need_dir):
        for file in files:
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), path + '/' + need_dir), compress_type = zipfile.ZIP_DEFLATED)
    fantasy_zip.close()
    os.chdir(owd)


def print_asking():
    print('----------------------------')
    print('모든 폴더를 압축 하시겠습니까?')
    print('Yes = 1 입력', 'No = 2 입력')


def ask_fix():
    print_asking()
    asking = input()
    if asking == '1':
        for kdx in range(len(changed_list)):
            zip_all_dir(changed_list[kdx])
            print(changed_list[kdx] + ' 압축 완료')
    else:
        ask_fix();

ask_fix()
print('모든 폴더 압축 완료')




    



