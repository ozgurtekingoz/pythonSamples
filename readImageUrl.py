import urllib.request

url1 = "https://media.geeksforgeeks.org/img-practice/banner/complete-interview-preparation-course-overview-image.png?v=1647341095"
url2 = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200711122552/Python-Programming-Language.png"

urlList = [url1, url2]
count = 1

for url in urlList:
    urllib.request.urlretrieve(url, "Img" + str(count) + ".jpg")
    count += 1
