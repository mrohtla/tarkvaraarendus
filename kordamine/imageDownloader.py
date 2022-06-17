import requests #impordib mooduli

def download_files(url): #defineerib funktsiooni
    local_filename = url.split('/')[-1] #
    with requests.get(url, stream=True) as r:
        print("Downloading...") #väljastab teksti
        with open("C:/Users/Johan Godinho/Desktop/"+local_filename, 'wb') as f:
            print("Writing data to file") #väljastab teksti
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    f.close() #sulgeb faili
    print("Download complete") #väljastab teksti
    print("File saved as "+ local_filename)

while 1: #loop
    print("Welcome to the image downloader") #väljastab teksti
    image_url = input(str("Image url : "))
    download_files(image_url)
    print("")