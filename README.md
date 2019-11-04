# JSONFilter

##### Author:
    Theekshana Sandaru Thilakarathne

## Step 0
Follow these only if you don't have python 3x, pip, virtualenv and virtualenvwrapper installed in your machine.
If you do, then skip to step 1
#### a) Install python 3x
	verify using 'python --version'
#### b) Install pip
	verify using 'pip --version'

## Step 1
#### 1) Create a virtual environment
	In command shell; Go to project's root directory and create a virtual environment.
	eg : virtualenv venv
	(This creates the 'venv' folder inside Project's root directory)

#### 2) To activate the virtual environment
	In command shell; Go to project's root directory
	run command 'venv\Scripts\activate'

	(when you need to deactivate run command 'deactivate')

## Start Application)
### 1) Changes Should do
    Before you start make sure to change the path of dase_dir in QueryFiler.py file according to locatoin of the main directory of your computer.
    example:
        base_dir = "C:\Users\ChampWk38\Desktop\jsonfilter"
    
## Overview
### 1) Handlers Directory:
     inside this directory theres is a File called QueryFilter.py. It is consist with four functions respectively. All the filtering
     logics are executing here.
     
     1. get_user()
        Resposible for filtering users accoring to any fieleds of the user JSON object. 
       
     2. get_organization()
        Responsible function for filtering according to any field of the organizarions JSON object.
     
     3. get_tickets()
        Responsible for finding all the ticket related data from the ticket JSON object
      
     4. get_searchable_keys()
        By using this function you able to take all the filterable keys related to users, organization and tickets
     
     All 1, 2, 3 functions are required 2 parameters called "keyword" and the "value". 
        keyword = the object key that filer should based on
        value = the value that object key consist with

### 2) Helpers Directory
       Inside this directory there is a file called Helpers.py. It has 3 different functions respectively
       
        1. filter_by_tags():
           Responsible for filtering JSON objects based on the tags keyword.
           
        2. filterd_by_status():
           Responsible for filtering JSON object based on true, false values. For execution this requires the value as true or false
           or the keyword that value consist
           
        3. filter_by_other_keys():
            This function is responsible for filtering JSON object based on other keys like _id, external_id, etc

### 3) JsonStore Directory
     All the JSON filed have stored here

### 4) Finder.py    
    For get started with the application you have run the Finder.py file.
    
    Once it runs you will see an output like below:
    Hi, Chose an option to continue
     1. Press 1 for Searching
     2. Press 2 for List of Searchable
     3. Press 0 for Exit
   
    Here you have to provide a input like 1, 2 or 0.
    Based on the input the program will continue
    
    If your input is 1, it asking the category that filer should do like below,
    
        Press '1' of Users, Press '2' for Organizations, Press '3' for Tickets: 
        
        Once you select the category it will ask the key word like below 
        
            Please enter the key word: 
            
        Once you provide the keyword it asks the value like below,
        
            Please enter the value: 
           
        Nowe you can provide the value, once ths program recieve the input,
        it start to excute and filtering.
    
    If your input is 2 the programe will show you the shearchable key words based on the cateorgires.
    
    If you ainout is 0 then the program will exit

### 5) Hub.py
     Acting as a connnector between the Finder.py file and the other required logical functions

### 6) ReadJson.py
    Helping to read the JSON files for the given path. Once read, it returns a list of dictionaries
    
### 7) formatter.py
    All the data showing functions are inclued here

### 7) Test Directory
    All test are available here
     