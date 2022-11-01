import requests

# collect the webpage content
def capture_url():
    url = input("Enter the url of the webpage: ")
    response = requests.get(url)
    content = response.content
    return content

# take the tile
def take_title(sl):
    title = input("Enter the title: ")
    return title

#save the content to a file
def write_file(title, content):
    file = open(title,"wb")
    file.write(content)
    file.close()
    print("Downloaded " + title)

print("Do you want to download a series of webpages or a single webpage?")

is_series = input("enter \'y' for series, \'n' for single : ")

if is_series=='y':
    sl = 1
    while(True):
        content = capture_url()
        title = take_title(sl)
        sl_in_text = str(sl)
        title = sl_in_text + "." + title + ".html"
        write_file(title, content)
        sl+=1
        print("Press \'Enter' to download more")
        close = input("or Enter any number to close the program : ")
        if close:
            break
else:
    sl = ""
    content = capture_url()
    title = take_title(sl)
    title = sl + title + ".html"
    write_file(title, content)

