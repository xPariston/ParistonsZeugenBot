import bs4
import requests
import datetime

myheader = \
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d598b2966cc48ca2629e2ba4ac08e08c61538583441; PHPSESSID=nshuej9hcv0tf9n92vf66edk15; __atuvc=1%7C40; _iub_cs-76236742=%7B%22consent%22%3Atrue%2C%22timestamp%22%3A%222018-10-03T16%3A17%3A28.774Z%22%2C%22version%22%3A%221.2.4%22%2C%22id%22%3A76236742%7D; rr=258e010b9006d17d824fdb593d5de6a3; rr_id=1690206778488139; rr_add=ad867d4897d963981f86d1354c26eb7a; fbm_1457231197822920=base_domain=.rivalregions.com; fbsr_1457231197822920=ZMZ6a3I12XsU-pa0V3RQKUgPgQh7OYblFgnizsXazjY.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNvWmxkVFNHTWdVVjd6aWNGSk1nNWVQb2RXSWYtNlE5TENfRzJvRkNDNExNbjM1NnNZNFpEMGVYSEpzbGFQejVFWnB3blhtNUd2bFN0ZmxBZ2RPcmJlUHBuT2VmWU1kcFZBUFIxOGlkNHFWaFo4QXJQb1FPd2ZZTTNiamJZQXI2OFdMeGdEUWRzcWotWW5Kc011YmFNRy1iYkNIdUktdkFQaG04MVlEY1ZtR0VodnE5NW5QT19SZkppTmRURTBFQzJ4ZjJBc1BJdm5zZFF5ZlZQeXp2OXNHUDJlYk5sSFZaZ05idWo4TGlfaHdBaGRJOEdCWnRZSW91Z1FIdjFNLUlnVV9rWF9FYmlOT2NNVTljMGwtc0lKZWxuQXFRWVZJZVM2UWRCc0JNREdRd2VmaDFQeUpjLWZLM29DYk9YZzZvaU5pVURFODZpMW0tNWtzbHRuMTQ0OTBRUkdOcmkyWmN6aEdYZVNEei1wY3AwcXF4U1NFcUtmcmhCOWU5X1Faa28iLCJpc3N1ZWRfYXQiOjE1Mzg1ODY5MTYsInVzZXJfaWQiOiIxNjkwMjA0NjMxMDA0NDkzIn0",
        "Host": "rivalregions.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }


def getRawDamage(url):

    partys = []
    damage = []
    counter = 1


    url = url.replace("#war/details","listed/partydamage")
    r=requests.get(url, headers=myheader)
    r=r.content
    soup = bs4.BeautifulSoup(r,'html.parser')

    for party in soup.find_all(attrs={"class":"list_name pointer"}):
        party=party.get_text()
        party= party[0:-14]
        partys.append(party)

    for dmg in soup.find_all(attrs={"class":"yellow"}):
        if counter%2 == 1:
            damage.append(dmg.get_text())
        counter+=1

    return partys,damage

def RefineDamage(url,partylist):

    partys,damage=getRawDamage(url)
    Gesamtdamage=0
    partydictRawDmg={}
    partydictPerDmg={}

    for n1,Rang in enumerate(partys):
        for n2,p in enumerate(partylist):
            if Rang == p:
                dmg=damage[n1].replace('.','')
                dmg=int(dmg)

                if Rang in partydictRawDmg:
                    partydictRawDmg[Rang] = partydictRawDmg[Rang] - dmg
                    Gesamtdamage = Gesamtdamage - dmg
                else:
                    partydictRawDmg[Rang]=dmg
                    Gesamtdamage += dmg

    for i in partydictRawDmg:
        Percent = partydictRawDmg[i]/Gesamtdamage * 100
        partydictPerDmg[i]=Percent

    return Gesamtdamage,partydictRawDmg,partydictPerDmg

def MultiWar(urllist,partylist):
    Gesamtdamage = 0
    partydictRawDmg = {}
    partydictPerDmg = {}

    for x in urllist:
        PartDamage,PartRawDmg,PartPerDmg = RefineDamage(x,partylist)
        Gesamtdamage += PartDamage

        for i in PartRawDmg:
            if i in partydictRawDmg:
                partydictRawDmg[i] += PartRawDmg[i]
            else:
                partydictRawDmg[i] = PartRawDmg[i]

    for i in partydictRawDmg:
        Percent = partydictRawDmg[i]/Gesamtdamage * 100
        partydictPerDmg[i]=Percent

    return Gesamtdamage,partydictRawDmg,partydictPerDmg

def getStateWars7d(stateid):
    regionlist = []
    StateUrl="http://rivalregions.com/listed/state/"
    url = StateUrl + stateid
    r = requests.get(url, headers=myheader)
    r = r.content
    soup = bs4.BeautifulSoup(r, 'html.parser')

    for e in soup.find_all(attrs={"class": "list_name pointer small"}):
        x = str(e)
        x = x.split(" ")
        y = x[1].split("=")
        z = y[1].replace('"', '')
        ids = z.split("/")
        id = ids[2]

        regionlist.append(id)

    now = datetime.datetime.now()
    siebenDays = now + datetime.timedelta(days=-7)
    yesterday= now + datetime.timedelta(days=-1)

    warlistState = []

    BaseUrl = "http://rivalregions.com/war/top/"
    for i in regionlist:
        RegionWarUrl = BaseUrl + i
        r = requests.get(RegionWarUrl, headers=myheader)
        r = r.content
        soup = bs4.BeautifulSoup(r, 'html.parser')

        warlist = []
        for w in soup.find_all(attrs={"class": "list_avatar yellow pointer"}):
            x = str(w)
            x = x.split(" ")
            y = x[1].split("=")
            z = y[1].replace('"', '')
            ids = z.split("/")
            id = ids[2]
            warlist.append(id)

        warcounter = 0
        todaycounter = 0
        datelist = []
        for i in soup.find_all(attrs={"class": "list_avatar pointer small"}):
            date = i.get_text()
            try:
                date = datetime.datetime.strptime(date, "%d %B %Y %H:%M")
                if date > yesterday:
                    todaycounter += 1
                else:
                    datelist.append(date)

            except:
                todaycounter += 1
                warcounter +=1


        for q in datelist:
            if q > siebenDays:
                warcounter += 1
        if warcounter > 0:
            for i in range(warcounter):
                if i >= todaycounter:
                    warlistState.append(warlist[i])

    return warlistState


def MakeNumber2PrettyString(number):
    number = str(number)
    length = len(number)
    newnumber = ""
    counter = 0
    for x in range(length):
        if counter % 3 == 0 and counter != 0:
            newnumber+= "."+number[length-x-1]
            counter+=1
        else:
            newnumber+= number[length-x-1]
            counter +=1

    newLength=len(newnumber)
    finalnumber=''
    for i in range(newLength):
        finalnumber += newnumber[newLength-i-1]

    return finalnumber
