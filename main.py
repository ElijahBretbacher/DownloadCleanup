import os
import shutil
import time

while True:
    originalPath = os.path.expanduser('~/Downloads')

    files = os.listdir(originalPath)

    os.chdir(originalPath)
    print(originalPath)

    for file in files:
        filePath = originalPath + '/' + file
        file_name, file_ext = os.path.splitext(filePath)
        counter = 0
        while not os.path.exists(filePath):
            time.sleep(1)
        if os.path.isfile(filePath):
            if file_ext != '' and file_ext != '.tmp':
                filesize = os.path.getsize(file)

                time.sleep(2)

                newFileSize = os.path.getsize(file)

                if filesize == newFileSize:
                    try:
                        if file_ext == '.pdf':
                            shutil.move(filePath, originalPath + "/pdf")
                        elif file_ext == '.exe' or file_ext == '.msi':
                            shutil.move(filePath, originalPath + "/exe")
                        elif file_ext == '.rar' or file_ext == '.zip':
                            shutil.move(filePath, originalPath + "/zip")
                        elif file_ext == '.mcdx':
                            shutil.move(filePath, originalPath + "/mcdx")
                        elif file_ext == '.png' or file_ext == '.jpg' or file_ext == '.jpeg':
                            shutil.move(filePath, originalPath + "/pics")
                        elif file_ext.__contains__('.doc'):
                            shutil.move(filePath, originalPath + "/docs")
                        elif file_ext.__contains__('.ppt'):
                            shutil.move(filePath, originalPath + "/ppt")
                        elif file_ext.__contains__('.xl'):
                            shutil.move(filePath, originalPath + "/xls")
                        elif file_ext == '.mp4' or file_ext == '.mp3':
                            shutil.move(filePath, originalPath + "/music")
                        elif file_ext == '.psd' or file_ext == '.ai' or file_ext == '.prproj':
                            shutil.move(filePath, originalPath + "/medt")
                        elif file_ext == '.java' or file_ext == '.fxml' or file_ext == '.class':
                            shutil.move(filePath, originalPath + "/sew")
                        elif file_ext == '.txt':
                            shutil.move(filePath, originalPath + "/txt")
                        else:
                            shutil.move(filePath, originalPath + "/default")
                    except:
                        counter+=1
                        os.rename(filePath, file_name + str(counter) + file_ext)
