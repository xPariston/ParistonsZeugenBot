import bs4
import requests
import datetime
import asyncio
import aiohttp
import async_timeout

myheader = \
    {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=d105fdf82a23af096ce03512cfa8642d21538983504; _iub_cs-76236742=%7B%22consent%22%3Atrue%2C%22timestamp%22%3A%222018-10-08T07%3A25%3A09.341Z%22%2C%22version%22%3A%221.2.4%22%2C%22id%22%3A76236742%7D; fbm_1457231197822920=base_domain=.rivalregions.com; fbsr_1457231197822920=wkdbpbEU1Hyxvb6vNSHfiDNQlgcZXQ0CryKq_eeuXXo.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUURuVlV3cVlUaGtwNl9iLWI4N2xZcEJWY3FBY0ROZ0RvVmtQYTdzUTZwY0ttLUwxRkl2dFlXLXhyMzZZTjJFWHdISFlCZlpsaWlqdWJnX0NSQXphalhCd0d4OGdaaXZaQ2g5LURSeWMxWmRtYXhqNDZwLVVpVUVGaUhMMjRycTB1MmVIRDJiMW9DaHlJazU0cmNGSHB4WGI3TnlnWHA5TEtKcTRNdmt6VWNWTFZvallvaFpMcWlBVktuWlp6MGpKb3hWSW1jUjk2MW55Tm1RSmlvYnBMaFFoRnFMNlBocWtfNnNXck10Z0pkU2xBankySzJzN1F4TGVjdEk1SW4tQmhnY0ZjdU9ZWG1jQnRTUjF4WDlFbXBRR2NuaU9FVHVwbXZUbjN5ZEstTklwaUY3aWZhZmVKa1hwYkw2VWlKSTdzUmZtc1FETm8tVzNIdS1CdVl4M1A1T3BsZUNLa0RtUUpjNUdzdG50Qk9VTnVuU0RUV1B5aHpwdEtveFVqa2FFUzgiLCJpc3N1ZWRfYXQiOjE1Mzk3NjQ2OTMsInVzZXJfaWQiOiIxNjkwMjA0NjMxMDA0NDkzIn0; PHPSESSID=9jtvas2frpuuohogkal8etrbm5; __atuvc=1%7C42; __atuvs=5bc6f2b2607816c9000; rr=ba6e2bc500ff54218b0936480725b3ac; rr_id=2000268192; rr_add=ad867d4897d963981f86d1354c26eb7a",
        "Host": "rivalregions.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    }


async def getRawDamage(url,session):

    partys = []
    damage = []
    counter = 1

    url = url.replace("#war/details","listed/partydamage")
    html = await fetch(session, url)
    soup = await soup_d(html)

    for party in soup.find_all(attrs={"class":"list_name pointer"}):
        party=party.get_text()
        party= party[0:-14]
        partys.append(party)

    for dmg in soup.find_all(attrs={"class":"yellow"}):
        if counter%2 == 1:
            damage.append(dmg.get_text())
        counter+=1
    print("RawDamage URL: ", url)
    print("In RawDamage. damagelist: ", damage, " partylist ",partys)

    return partys,damage

async def RefineDamage(url,partylist,session):

    partys,damage= await getRawDamage(url,session)
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

async def MultiWar(urllist,partylist):
    async with aiohttp.ClientSession(headers=myheader) as session:
        Gesamtdamage = 0
        partydictRawDmg = {}
        partydictPerDmg = {}
        print("In Multiwar. URLlist: ", urllist)
        for x in urllist:
            PartDamage,PartRawDmg,PartPerDmg = await RefineDamage(x,partylist,session)
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

async def getStateWars7d(stateid):
    async with aiohttp.ClientSession(headers=myheader) as session:
        regionlist = []
        StateUrl="http://rivalregions.com/listed/state/"
        url = StateUrl + stateid
        html = await fetch(session, url)
        soup = await soup_d(html)

        print("in get statewars, stateid: ", stateid)

        for e in soup.find_all(attrs={"class": "list_name pointer small"}):
            x = str(e)
            x = x.split(" ")
            y = x[1].split("=")
            z = y[1].replace('"', '')
            ids = z.split("/")
            id = ids[2]
            id = id.strip()
            regionlist.append(id)

        now = datetime.datetime.now()
        siebenDays = now + datetime.timedelta(days=-21)
        yesterday= now + datetime.timedelta(days=-1)

        warlistState = []

        BaseUrl = "http://rivalregions.com/war/top/"
        for i in regionlist:
            RegionWarUrl = BaseUrl + i
            html = await fetch(session, RegionWarUrl)
            soup = await soup_d(html)

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
        print("WarListState: ",warlistState)
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


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def soup_d(html, display_result=False):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    if display_result:
        print(soup.prettify())
    return soup

async def RessToMoney(Ress):

    amount,TypeOfRess= Ress.split(' ')

    amount = int(amount.replace('.',''))

    PriceStateMoney = 1
    PriceStateGold = 500000
    PriceOil = 150
    PriceOre = 150
    PriceDiamonds = 840000
    PriceUranium = 1300

    Value = 0

    if "$" in TypeOfRess:
        Value = PriceStateMoney * amount
    if "G" in TypeOfRess:
        Value = PriceStateGold * amount
    if "kg" in TypeOfRess:
        Value = PriceOre * amount
    if "bbl" in TypeOfRess:
        Value = PriceOil * amount
    if "pcs" in TypeOfRess:
        Value = PriceDiamonds * amount
    if "g" in TypeOfRess:
        Value = PriceUranium * amount

    return Value

async def getMarktPreise():
    async with aiohttp.ClientSession(headers=myheader) as session:
        url = "http://rivalregions.com/storage/listed/3"
        html = await fetch(session, url)
        soup = await soup_d(html)
        print("Hallo")
        marktpreise = {}
        marktdict= {}
        marktdict["oil"] = "3"
        marktdict["ore"] = "4"
        marktdict["diamonds"] = "15"
        marktdict["uranium"] = "11"

        for stoff in marktdict:
            url = "http://rivalregions.com/storage/listed/" + marktdict[stoff]
            html = await fetch(session, url)
            soup = await soup_d(html)
            counter = 0
            wert = 0
            for e in soup.find_all(attrs={"class": "white green imp small"}):
                x = e.get_text()
                x = x.replace("$","")
                x = x.replace(".","")
                x= x.strip()
                wert += int(x)
                counter += 1
                if counter == 3:
                    marktpreise[stoff] = str(round(wert/3))
                    break

        return marktpreise

async def getProfilParty(profilid,session):
    BaseUrl = "http://rivalregions.com/slide/profile/"
    url = BaseUrl + profilid
    print("Profilurl: ",url)


    html = await fetch(session, url)
    soup = await soup_d(html)

    #r = requests.get(url, headers=myheader)
    #r = r.content
    #soup = bs4.BeautifulSoup(r, 'html.parser')
    party = ""
    counter = 1
    for party in soup.find_all(attrs={"class": "header_buttons_hover slide_profile_link tc"}):
        print( "in getProfilParty: ",party)
        if counter == 2:
            party = party.get_text()
        if counter == 3:
            party = party.get_text()
        counter +=1
    try:
        party = party.replace("Ã¼","ü")
    except:
        party = "Unaffiliated"
    #print(party + "Eintrag aus getProfilParty")
    return party


async def getRegionDonations(regionid, partylist,profildict, session):
    try:
        id,adder = regionid.split("/")
        adder = int(adder)
    except:
        adder = 0

    BaseUrl = "http://rivalregions.com/listed/donated_regions/"
    url = BaseUrl + regionid
    print(url)

    html = await fetch(session, url)
    soup = await soup_d(html)

    #r = requests.get(url, headers=myheader)
    #soup = bs4.BeautifulSoup(r)

    now = datetime.datetime.now()
    siebenDays = now + datetime.timedelta(days=-21)
    datebool=[]

    for dates in soup.find_all(attrs={"class": "list_avatar pointer small"}):
        date = dates.get_text()
        try:
            date = datetime.datetime.strptime(date, "%d %B %Y %H:%M")
            if date > siebenDays:
                datebool.append(True)
            else:
                datebool.append(False)
        except:
            datebool.append(True)

    Party=""
    Partybool=False
    Partydonations={}


    counter = 0
    listcounter = 0
    for donation in soup.find_all(attrs={"class": "list_avatar pointer imp"}):

        if counter % 2 == 0 and counter != 0: listcounter += 1
        if datebool[listcounter]== True:

            if counter % 2 == 0:
                x = str(donation)
                x = x.split(" ")
                y = x[1].split("=")
                z = y[1].replace('"', '')
                ids = z.split("/")
                id = ids[2]

                if id in profildict:
                    Party = profildict[id]
                    #print(Party + "aus Profildict")
                else:
                    Party = await getProfilParty(id,session)
                    profildict[id]=Party

                try:
                    Party = Party.strip()
                except:
                    print(id)

                if Party in partylist:
                    Partybool = True
                else:
                    Partybool = False

            if counter % 2 == 1:
                donation = donation.get_text()
                if Partybool == True:
                    #print(Party)
                    if Party in Partydonations:
                        #print(Partydonations[Party])
                        Partydonations[Party] = Partydonations[Party] + await RessToMoney(donation)
                    else:
                        Partydonations[Party] = await RessToMoney(donation)
                        #print(RessToMoney(donation))
        counter+=1
        #print(Partydonations)
    print("Datebool: " , datebool[listcounter])
    if datebool[listcounter]==True:
        adder += 25
        try:
            id,a = regionid.split("/")
            id=id.strip()
            regionid = id
        except:
            pass
        regionid = regionid + "/" + str(adder)
        print("Im if, regionid: ", regionid)
        partydict = await getRegionDonations(regionid,partylist,profildict,session)
        for x in partydict:
            if x in Partydonations:
                Partydonations[x] = Partydonations[x] + partydict[x]
            else:
                Partydonations[x] = partydict[x]

    return Partydonations

async def getStateDonations(stateid,partylist,profildict):

    async with aiohttp.ClientSession(headers=myheader) as session:

        regionlist = []
        StateUrl = "http://rivalregions.com/listed/state/"
        url = StateUrl + stateid
        html = await fetch(session, url)
        soup = await soup_d(html)
        # r = requests.get(url, headers=myheader)
        # r = r.content
        # soup = bs4.BeautifulSoup(r, 'html.parser')

        partydonations={}

        for e in soup.find_all(attrs={"class": "list_name pointer small"}):
            x = str(e)
            x = x.split(" ")
            y = x[1].split("=")
            z = y[1].replace('"', '')
            ids = z.split("/")
            id = ids[2]

            regionlist.append(id)
        counter= 1
        for region in regionlist:
            print("region nr. %d: " %counter + region)
            tempdonations = await getRegionDonations(region,partylist,profildict,session)
            for p in tempdonations:
                if p in partydonations:
                    partydonations[p] = partydonations[p] + tempdonations[p]
                else:
                    partydonations[p]=tempdonations[p]
            counter+=1

        return partydonations





