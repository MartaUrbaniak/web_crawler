#-*- coding: utf-8 -*-

import sys

import bs4

import requests

#creating the lists and site dictonary 

links = []

keys = []

temp = []

#site dictonary kip key:url and value: site name and links

site_dict = {}


#function definicion - function get url as a value and return information about the website in form site map

def site_map(argv):
  
  #converting argv to a string
  
  temp_url =str (argv)
  
  string_temp_url = temp_url[1:-1]
  
  
  url = string_temp_url[1:-1]

  #conection to a serwer
  
  r = requests.get(url)


  r.raise_for_status()

  
  #getting data from html -title
  
  firstSoup = bs4.BeautifulSoup(r.text, "html.parser")


  elem_title = firstSoup.select('title')

  main_title = str(elem_title)   

  #getting data from html -links

  for a in firstSoup.find_all('a', href=True):
    links.append(a['href'])

 
  links_main=' '.join(links)    


  #this loop take every link from the links and using it as a new url argument

  for i in range(len(links)):
    
    temp = []
    
    #checking if link contains words below, if not continue
    
    if "tel" not in links[i]: 
      
      if "http" not in links[i]:
	
       
       #making the full url adress - url + link
       
       url_p = url[:-1]
       
       url_sec = url_p + links[i]
      
       
       #adding url adres to a dictonary as a key
       
       keys.append(url_sec)
       
        #conection to a serwer
       
       s = requests.get(url_sec + links[i])
      
      
       #getting data from html -title
       
       secondSoup = bs4.BeautifulSoup(s.text, "html.parser")
       
       elem_sub_title = secondSoup.select('title') 

      
       str_elem_sub_title =str (elem_sub_title)
      
      
       #checking if there is title or a bug
       
       
       if str_elem_sub_title.startswith('[<title>404 '):
        
        x = 'no title'
       
       
       else:
        
        x = str_elem_sub_title

      
       #getting data from html -links
      
       for a in secondSoup.find_all('a', href=True, text=True):
  
        sub_url = url_p + a['href']
        
        temp.append(sub_url)
      
      
        #making the diconary value from reach data (title and links)
        
        y = ' '.join(temp)
      
        
        dict_value = "title: " + x + " " + "\n" + "\n" + "links: " + y

      
        #adding the dictonary value
      
        site_dict[url_sec] = dict_value


  #printing the informations

  print("==============================================================================================================================================")
  print("==============================================================================================================================================")
  print("This is the URL of the site you were loking for: ",url)
  print("==============================================================================================================================================")
  print("==============================================================================================================================================")
  print("This is the title of the page from html document: ",main_title)
  print("==============================================================================================================================================")
  print("==============================================================================================================================================")
  print("Below you can see the links wich you can click for: ")
  print("  ")
  print(links_main)    
  print("====================================================================================================================")
  print("====================================================================================================================")
  print("====================================================================================================================")
  print("Below you will find map of this site:  ")
  print("====================================================================================================================")
  print(" ")
  print(" ")

  for k, v in site_dict.items():
      print("")
      print("URL: ",k)
      print("")
      print(v)
      print("")
      print("")
      print("")


if __name__=="__main__":
  site_map(sys.argv[1:])

