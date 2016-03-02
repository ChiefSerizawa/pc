import urllib.request

f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")

while True:
    nb = f.read().decode('utf-8').split(' ')[-1]
    try:
        int(nb)
    except:
        break
    if nb == "16044":
        nb = "8022"
    f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nb)

print(nb)

