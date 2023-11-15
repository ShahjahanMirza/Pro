def automted_file_creator(directory_name):
    """
    goes in the directory provided, reads the files' names and
    create new sub directories based on the names of the files,
    reads data from each file, and make directories based on the data
    inside the files in each respective directory

    Args:
        directory_name (dir_path): where the files are located 
    """
    import os
    print('Started...', end='\n\n')
# -------------------------------------------------------------------------------------------------------------------------------------
    files = [] # store .txt files in this
    for dir_path, dir_names, file_names in os.walk(directory_name):
        for i in file_names: # iterating over files
            if i[-4:] == '.txt': # if file has .txt extension 
                files.append(i)  # we need that   
    print("Files Found :" ,files )    # remove
# -------------------------------------------------------------------------------------------------------------------------------------
    for i in files: # in files names
        print("\nCurrent File : ", i, end='\n\n') # remove
        counter = 1
# -------------------------------------------------------------------------------------------------------------------------------------     
        try: 
            os.mkdir(directory_name + i.replace('.txt','/'))    # try to make a directory of that file name
            print("Made Folder named : ", (directory_name + i.replace('.txt','/'))) # remove
        except:
            os.chdir(directory_name + i.replace('.txt','/'))    # if that directory is already there, move into that
            print("Folder Already there...")
            print("Going into Folder : ", directory_name + i.replace('.txt','/'))
# -------------------------------------------------------------------------------------------------------------------------------------
        with open(directory_name+i, 'r') as f: # open the file which we are iterating through in the directory
            print("Opened File : ",i, '\n')
            for line in f: # iterate through every line in that file
                try: 
                    os.mkdir((directory_name+i.replace('.txt','/')+f"{counter}-"+line.replace('\n','').replace(' ','-').replace('|','')) ) # try to make a sub-directory with the name of the file in current files
                    print('Made Sub-Folder named : ', (i.replace('.txt','/')+f"{counter}-"+line.replace('\n','').replace(' ','-').replace('|','')) ) # remove
                except: 
                    print(f"Sub-Folder named {line} Already There...") # if we can't make a directory, then that means there is a directory already there with that name so we move to the next name in file in current files
                counter += 1 #  keep this incrementing whether we make a file or not, to number the file names
        print(f"~Created {counter-1} Sub-Folders~")
        print("\nClosed File : ", i, end='\n-----------------------------------------------------------')
# -------------------------------------------------------------------------------------------------------------------------------------
    print("\nDONE ALL FILES!")
# -------------------------------------------------------------------------------------------------------------------------------------
automted_file_creator("e:/100-Machine-Learning-Projects/")