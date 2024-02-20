'part A:'
import requests
def  get_content(url):
    # get request -to download the content 
    response = requests.get(url,stream=True)
    
    #spliting the url into  list of strings by '/'  
    split_url = url.split('/')
    #getting the last element which is filename
    file_name = split_url[-1]
    #path where file will be saved
    pathname = f'desktop/{file_name}'
    #opening the file in write-binary mode and writing the downloaded data to it
    with open(pathname,'wb') as f:
        for chunk in response.iter_content(chunk_size=50):
            print('+', end='')                       #give ser feedback
        f.write(chunk)                          #write the bit to file
    print(f'File "{file_name}" has been downloaded and saved to "{pathname}".')
