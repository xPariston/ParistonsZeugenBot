from discord.ext.commands import Bot
import discord
import random
import asyncio
import datetime
import os
import rrDamage
import numpy as np

BOT_PREFIX = ("!")

client = Bot(command_prefix=BOT_PREFIX)

profildict={}
nonpartyroles = ["Präsident", "Händler", "Vize-Präsident","verifiziert","@everyone","AdminTeam","Minister","Kandidat","Abgeordneter"]

WarProzent= 30.
SpendenProzent = 30.
WahlProzent = 40.

Antwort1='Pariston' #Wer wacht über dich tagein tagaus?
Antwort2='Leuchtturm' #
Antwort3='Raion' #Zu wem sagte Pariston auf seinen Reisen: Fürchte dich nicht mein Sohn. Wir werden großes vollbringen.?
Antwort4='Unendlichen' #Wo treffen sich Parallele Linien
Antwort5='Klebt' #Das dritte K in KKKK steht für welches Wort?
Antwort6='Moderator' #Der einzig wahre Pariston ist nicht nur Parteiführer, Staatsführer und Gottheit, sondern auch...
Antwort7='Mecklenburg-Vorpommern'
Antwort8='Kuras'
Antwort9='Niemand' #Vorbild
Antwort10='Pirat' #Früheres Leben


@client.command(name="MakeHändler",
                description='!MakeHändler @Pariston. Nur AdminTeam Mitglieder können dies.',
                brief='!MakeHändler @Pariston. Nur AdminTeam Mitglieder können dies.',
                pass_context=True)

async def MakeHändler(context):
    msg = context.message.content
    autor = context.message.author
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 = ""

    for role in serverroles:
        if role.name == "AdminTeam":
            targetrole = role
        if role.name == "Händler":
            targetrole2 = role

    if "@" in msg:
        if targetrole in autor.roles:
            for member in mentions:
                await client.add_roles(member,targetrole2)
                await client.say(member.name + " ist nun Händler!")
                break
        else:
            await client.say("Du musst Teil des AdminTeams sein um Händler zu ernnen")
    else:
        await client.say("Bitte ernenne einen Händler mit '!MakeHändler @Member'")

@client.command(name="RemoveHändler",
                description='!RemoveHändler @Pariston. Nur AdminTeam Mitglieder können dies.',
                brief='!RemoveHändler @Pariston. Nur AdminTeam Mitglieder können dies.',
                pass_context=True)

async def RemoveHändler(context):
    msg = context.message.content
    autor = context.message.author
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 = ""

    for role in serverroles:
        if role.name == "AdminTeam":
            targetrole = role
        if role.name == "Händler":
            targetrole2 = role

    if "@" in msg:
        if targetrole in autor.roles:
            for member in mentions:
                await client.remove_roles(member,targetrole2)
                await client.say(member.name + " ist nun nicht mehr Händler!")
                break
        else:
            await client.say("Du musst Teil des AdminTeams sein um Händler zu entfernen")
    else:
        await client.say("Bitte entferne einen Händler mit '!RemoveHändler @Member'")


@client.command(name="MakeVize",
                description='!MakeVize @Pariston. Nur Präsidenten könn dies.',
                brief='!MakeVize @Pariston. Nur Präsidenten könn dies.',
                pass_context=True)

async def MakeVize(context):
    msg = context.message.content
    autor = context.message.author
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 =""

    for role in serverroles:
        if role.name == "Präsident":
            targetrole = role
        if role.name == "Vize-Präsident":
            targetrole2 = role

    if "@" in msg:
        if targetrole in autor.roles:
            oldVize=""
            memberlist = client.get_all_members()
            for member in memberlist:
                if targetrole2 in member.roles:
                    await client.remove_roles(member,targetrole2)

            for member in mentions:
                await client.add_roles(member,targetrole2)
                await client.say(member.name + " ist nun neuer Vize-Präsident!")
                break
        else:
            await client.say("Du musst Präsident sein um einen Vize-Präsident ernennen")
    else:
        await client.say("Bitte ernenne einen Vize-Präsidenten mit '!MakeVize @Member'")

@client.command(name="MakeMinister",
                description='!MakeMinister @Pariston. Nur Präsidenten und Vize-Präsidenten können dies.',
                brief='!MakeMinister @Pariston. Nur Präsidenten und Vize-Präsidenten können dies.',
                pass_context=True)

async def MakeMinister(context):
    msg = context.message.content
    autor = context.message.author
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 = ""
    targetrole3 = ""

    for role in serverroles:
        if role.name == "Präsident":
            targetrole = role
        if role.name == "Vize-Präsident":
            targetrole2 = role
        if role.name == "Minister":
            targetrole3 = role

    if "@" in msg:
        if targetrole in autor.roles or targetrole2 in autor.roles:
            for member in mentions:
                await client.add_roles(member,targetrole3)
                await client.say(member.name + " ist nun neuer Minister!")
                break
        else:
            await client.say("Du musst Präsident oder Vize-Präsident sein um einen Minister zu ernennen")
    else:
        await client.say("Bitte ernenne einen Minister mit '!MakeMinister @Member'")




@client.command(name="RemoveMinister",
                description='!RemoveMinister @Pariston. Nur Präsidenten und Vize-Präsidenten können dies.',
                brief='!RemoveMinister @Pariston. Nur Präsidenten und Vize-Präsidenten können dies.',
                pass_context=True)

async def RemoveMinister(context):
    msg = context.message.content
    autor = context.message.author
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 = ""
    targetrole3 = ""

    for role in serverroles:
        if role.name == "Präsident":
            targetrole = role
        if role.name == "Vize-Präsident":
            targetrole2 = role
        if role.name == "Minister":
            targetrole3 = role

    if "@" in msg:
        if targetrole in autor.roles or targetrole2 in autor.roles:
            for member in mentions:
                if targetrole3 in member.roles:
                    await client.remove_roles(member,targetrole3)
                    await client.say(member.name + " ist nun nicht mehr Minister!")
                    break
                else:
                    await client.say("Der Spieler ist kein Minsiter")
        else:
            await client.say("Du musst Präsident oder Vize-Präsident sein um einen Minister zu entfernen")
    else:
        await client.say("Bitte entferne einen Minister mit '!RemoveMinister @Member'")


@client.command(name="EditPartyName",
                description='Ändere den Namen einer Partei. Schreibe dazu !EditPartyName AlterParteiname,NeuerParteiname.',
                brief='!EditPartyName AlterParteiname,NeuerParteiname.',
                pass_context=True)


async def EditPartyName(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
       await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        server= context.message.server
        msg = context.message.content.replace("!EditPartyName","")
        NameAlt,NameNeu = msg.split(",")
        NameAlt = NameAlt.strip()
        NameNeu = NameNeu.strip()

        parteiliste = await getPartys()

        if NameAlt in parteiliste:

            parteienchannel = discord.Object(id='497356738492629013')
            async for m in client.logs_from(parteienchannel, 100):
                if NameAlt in m.content:
                    newMsg= m.content.replace(NameAlt,NameNeu)
                    await client.edit_message(m,newMsg)

            parteienchannel = discord.Object(id='498487327484543006')
            async for m in client.logs_from(parteienchannel, 100):
                if NameAlt in m.content:
                    newMsg = m.content.replace(NameAlt, NameNeu)
                    await client.edit_message(m, newMsg)

            rolelist = server.roles

            for role in rolelist:
                if NameAlt in role.name:
                    name = role.name.replace(NameAlt,NameNeu)
                    await client.edit_role(server,role,name= name)

            channellist = server.channels
            NameAlt = NameAlt.lower()
            NameNeu = NameNeu.lower()
            NameAlt = NameAlt.replace(" ","-")
            NameNeu = NameNeu.replace(" ", "-")
            for channel in channellist:
                if channel.name.startswith(NameAlt):
                    name = channel.name.replace(NameAlt,NameNeu)
                    await client.edit_channel(channel,name= name)

            await client.say("Namensänderung abgeschlossen")

        else:
            await client.say("Partei nicht gefunden.")

@client.command(name="AddMember",
                description='!AddMember @Pariston Füge ein Mitgleid deiner Partei hinzu. Nur Parteileiter und Seretäre könn dies.',
                brief='!AddMember @Pariston Füge ein Mitgleid deiner Partei hinzu. Nur Parteileiter und Seretäre könn dies.',
                pass_context=True)

async def AddMember(context):

    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""

    party = await getPartyName(context)

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if party == role.name:
                    targetrole = role
            for member in mentions:
                memberroles = member.roles
                bool = False
                for role in memberroles:
                    print(role.name)
                    if role.name in nonpartyroles:
                        pass
                    else:
                        bool = True
                if bool == False:
                    await client.add_roles(member,targetrole)
                    await client.say(member.name + " wurde der Partei hinzugefügt")
                else:
                    await client.say(member.name + " befindet sich bereits in einer anderen Partei.")
        else:
            await client.say("Du musst Parteileiter oder Sekretär sein um ein Mitglied hinzuzufügen")
    else:
        await client.say("Bitte Füge ein Mitglied mit '!AddMember @Member' hinzu")

@client.command(name="Verifizierung",
                description='!Verifizierung @user',
                brief='!Verifizierung @user',
                pass_context=True)

async def Verifizierug(context):

    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""

    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        if "@" in msg:
                for role in serverroles:
                    if "verifiziert" == role.name:
                        targetrole = role
                for member in mentions:
                    await client.add_roles(member,targetrole)
                    await client.say(member.name + " wurde erfolgreich verifiziert")
        else:
            await client.say("Bitte verifiziere mit '!Verifizierung @Member'")

@client.command(name="RemoveAbgeordneten",
                description='!RemoveAbgeordner @Pariston Entferne ein Mitgleid deiner Partei aus dem Parlament. Nur Parteileiter und Seretäre könn dies.',
                brief='!RemoveAbgeordneter @Pariston Eintferne ein Mitgleid deiner Partei aus dem Parlament. Nur Parteileiter und Seretäre könn dies.',
                pass_context=True)

async def RemoveAbgeordneten(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 =""
    party = await getPartyName(context)
    partyseatsmax = 0
    parteienchannel = discord.Object(id='497356738492629013')
    partyseatsnow = 0

    logchannel = discord.Object(id='500952715917000715')

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if "Abgeordneter" == role.name:
                    targetrole = role
                if party == role.name:
                    targetrole2 = role

            for member in mentions:
                if targetrole2 in member.roles:
                    await client.remove_roles(member,targetrole)
                    await client.say(member.name + " repräsentiert nun nicht mehr die Partei im Parlament!")
                    await client.send_message(logchannel, member.name + " wurde als Repräsentant entfernt")
                    await RemoveVotes()
                    break
                else:
                    await client.say("Abgeordneter muss aus deiner Partei sein.")
        else:
            await client.say("Du musst Parteileiter oder Sekretär sein um ein Abgeordneten zu ernennen")
    else:
        await client.say("Bitte entferne ein Abgeordneten mit '!RemoveAbgeordneter @Member'")

@client.command(name="MakeAbgeordneten",
                description='!MakeAbgeordnet @Pariston Füge ein Mitgleid deiner Partei ins Parlament hinzu. Nur Parteileiter und Seretäre könn dies.',
                brief='!MakeAbgeordneten @Pariston Füge ein Mitgleid deiner Partei ins Parlament hinzu. Nur Parteileiter und Seretäre könn dies.',
                pass_context=True)

async def MakeAbgeordneten(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 =""

    party = await getPartyName(context)
    partyseatsmax = 0
    parteienchannel = discord.Object(id='497356738492629013')
    partyseatsnow = 0

    logchannel = discord.Object(id='500952715917000715')

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if "Abgeordneter" == role.name:
                    targetrole = role
                if party == role.name:
                    targetrole2 = role

            async for m in client.logs_from(parteienchannel, 100):
                p, seats = m.content.split(":")
                p = p.strip()
                seats = seats.strip()
                seats = int(seats)
                print("partei: ",p)
                print("seats: ",seats)
                if p == party:
                    partyseatsmax = seats

            memberlist = client.get_all_members()
            for member in memberlist:
                if targetrole2 in member.roles:
                    if targetrole in member.roles:
                        partyseatsnow += 1

            print (partyseatsmax)
            print (partyseatsnow)
            if partyseatsnow == partyseatsmax:
                await client.say("Maximale Anzahl an Abgeordneten bereits erreicht. Kicke einen Abgeordneten um einen neuen zu ernennen oder erhalte mehr Sitze.")
            else:
                for member in mentions:
                    if targetrole2 in member.roles:
                        await client.add_roles(member,targetrole)
                        await client.say(member.name + " repräsentiert nun die Partei im Parlament!")
                        await client.send_message(logchannel, member.name + " wurde als Repräsentant hinzugefügt")
                        break
                    else:
                        await client.say("User muss in deiner Partei sein um Abgeordneter zu werden.")
        else:
            await client.say("Du musst Parteileiter oder Sekretär sein um ein Abgeordneten zu ernennen")
    else:
        await client.say("Bitte ernenne ein Abgeordneten mit '!MakeAbgeordneter @Member'")

@client.command(name="MakeKandidat",
                description='!MakeKandidat @Pariston. Nur Parteileiter könn dies.',
                brief='!MakeKandidat @Pariston. Stelle ein Präsikandidaten auf. Nur Parteileiter könn dies.',
                pass_context=True)

async def MakeKandidat(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 =""

    party = await getLPartyName(context)

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if "Kandidat" == role.name:
                    targetrole = role
                if party == role.name:
                    targetrole2 = role

            oldKandidat=""
            memberlist = client.get_all_members()
            for member in memberlist:
                if targetrole2 in member.roles:
                    if targetrole in member.roles:
                        await client.remove_roles(member,targetrole)

            for member in mentions:
                if targetrole2 in member.roles:
                    await client.add_roles(member,targetrole)
                    await client.say(member.name + " ist nun neuer Kandidat für die Präsidentschaft!")
                    break
                else:
                    await client.say("User muss in deiner Partei sein um Kandidat zu werden.")
        else:
            await client.say("Du musst Parteileiter sein um ein Präsidentschaftskandidaten zu ernennen")
    else:
        await client.say("Bitte ernenne ein Kandidaten mit '!MakeKandidat @Member'")


@client.command(name="LeaveParty",
                description='Verlasse deine Partei',
                brief='Verlasse deine Partei.',
                pass_context=True)

async def LeaveParty(context):
    parteiliste = await getPartys()
    authorroles = context.message.author.roles
    author = context.message.author
    targetrole = ""
    targetrole2 = ""
    targetrole3 = ""
    Leiterbool = False
    Abgeordneterbool = False
    Kandidatbool = False


    for partei in parteiliste:
        for role in authorroles:
            if partei == role.name:
                targetrole = role
            if "Leiter - " + partei == role.name:
                Leiterbool = True
            if "Abgeordneter" == role.name:
                Abgeordneterbool = True
                targetrole2 = role
            if "Kandidat" == role.name:
                Kandidatbool = True
    if Leiterbool == False:
        if targetrole != "":
            if Kandidatbool == False:
                if Abgeordneterbool == False:
                    await client.remove_roles(author,targetrole)
                    await client.say ("Du hast die Partei verlassen.")
                else:
                    await client.remove_roles(author,targetrole2)
                    await client.remove_roles(author, targetrole)
                    await client.say("Du hast die Partei verlassen und deinen Parlamentsitz geräumt.")
                    await RemoveVotes()
            else:
                if Abgeordneterbool == False:
                    await client.remove_roles(author,targetrole)
                    await client.remove_roles(author,targetrole3)
                    await client.say ("Du hast die Partei verlassen und bist kein Kandidat mehr.")
                else:
                    await client.remove_roles(author,targetrole2)
                    await client.remove_roles(author, targetrole)
                    await client.remove_roles(author,targetrole3)
                    await client.say("Du hast die Partei verlassen, deinen Parlamentsitz geräumt und deine Kandidatur aufgegeben. Wow, da muss es echt gekracht haben damit es soweit kommt. Kopf hoch, Spiel geht weiter! Ich wünsch dir viel Glück!")
                    await RemoveVotes()
        else:
            await client.say ("Du bist in keiner teilnehmenden Partei.")
    else:
        await client.say("Du bist Leiter dieser Partei. Gebe den Posten ab oder lass die Partei vom AdminTeam löschen.")

@client.command(name="KickMember",
                description='!KickMember @Pariston Kick ein Mitgleid aus deiner Partei. Nur Parteileiter und Seretäre könn dies.',
                brief='!KickMember @Pariston Kick ein Mitgleid aus deiner Partei. Nur Parteileiter und Seretäre könn dies.',
                pass_context=True)

async def KickMember(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    authorroles = context.message.author.roles
    serverroles = server.roles
    targetrole = ""
    targetrole2 = ""
    targetrole3 = ""
    targetrole4 = ""
    targetrole5 = ""
    party = await getPartyName(context)

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if party == role.name:
                    targetrole = role
                if "Leiter -" + party == role.name:
                    targetrole2 = role
                if "Sekretär -" + party == role.name:
                    targetrole3 = role
                if "Abgeordneter" == role.name:
                    targetrole4 = role
                if "Kandidat" == role.name:
                    targetrole5 = role

            for member in mentions:
                if targetrole2 in authorroles:
                    await client.say("Ein Leader kann sich nicht aus der eigenen Partei kicken. Bitte das Admin Team die Partei zu löschen oder wechsel den Parteileiter mit !ChangeLeader")
                elif targetrole3 in authorroles:
                    await client.remove_roles(member,targetrole3)
                    await client.remove_roles(member, targetrole)
                    await client.remove_roles(member, targetrole4)
                    await client.remove_roles(member, targetrole5)
                    await client.say(member.name + " wurde aus der Partei gegickt")
                else:
                    await client.remove_roles(member, targetrole)
                    await client.remove_roles(member, targetrole4)
                    await client.remove_roles(member, targetrole5)
                    await client.say(member.name + " wurde aus der Partei gegickt")
        else:
            await client.say("Du musst Parteileiter oder Sekretär sein um ein Mitglied zu kicken")
    else:
        await client.say("Bitte kicke ein Mitglied mit '!AddMember @Member' hinzu")

    await RemoveVotes()

@client.command(name="RemoveSekretär",
                description='!RemoveSekretär @Pariston Kick ein Sekretär aus deiner Partei. Nur Parteileiter können dies.',
                brief='!RemoveSekretär @Pariston Kick ein Sekretär aus deiner Partei. Nur Parteileiter können dies.',
                pass_context=True)

async def RemoveSekretär(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""

    party = await getLPartyName(context)

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if "Sekretär - " + party == role.name:
                    targetrole = role
            for member in mentions:
                await client.remove_roles(member, targetrole)
                await client.say(member.name + "wurde als Sekretär entfernt")
        else:
            await client.say("Du musst Parteileiter sein um ein Sekretär zu entfernen")
    else:
        await client.say("Bitte entferne ein Sekretär mit '!RemoveSekretär @Member'.")

@client.command(name="MakeSekretär",
                description='!MakeSekretär @Pariston Ernenne einen Sekretär aus deiner Partei. Nur Parteileiter können dies.',
                brief='!MakeSekretär @Pariston Ernenne einen Sekretär aus deiner Partei. Nur Parteileiter können dies.',
                pass_context=True)

async def MakeSekretär(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    targetrole = ""
    targetrole2 = ""

    party = await getLPartyName(context)

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if "Sekretär - " + party == role.name:
                    targetrole = role
                if party == role.name:
                    targetrole2 = role
            for member in mentions:
                sek_roles = member.roles
                if targetrole2 in sek_roles:
                    await client.add_roles(member, targetrole)
                    await client.say(member.name + " wurde als Sekretär hinzugefügt")
                else:
                    await client.say("User muss Teil der Partei sein.")
        else:
            await client.say("Du musst Parteileiter sein um ein Sekretär hinzuzufügen.")
    else:
        await client.say("Bitte füge ein Sekretär mit '!MakeSekretär @Member' hinzu.")

@client.command(name="ChangeLeader",
                description='!ChangeLeader @Pariston Ernenne einen neuen Leader aus deiner Partei. Nur Parteileiter können dies.',
                brief='!ChangeLeader @Pariston Ernenne einen neune Leader aus deiner Partei. Nur Parteileiter können dies.',
                pass_context=True)

async def ChangeLeader(context):
    msg = context.message.content
    mentions = context.message.mentions
    server = context.message.server
    serverroles = server.roles
    author = context.message.author
    targetrole = ""
    targetrole2 = ""
    targetrole3 = ""

    party = await getLPartyName(context)

    if "@" in msg:
        if party != "":
            for role in serverroles:
                if party == role.name:
                    targetrole3 = role
                if "Leiter - " + party == role.name:
                    targetrole = role
                if "Sekretär - " + party == role.name:
                    targetrole2 = role
            for member in mentions:
                if targetrole3 in member.roles:
                    await client.add_roles(member, targetrole)
                    await client.remove_roles(member, targetrole2)
                    await client.remove_roles(author, targetrole)
                    await client.add_roles(author, targetrole2)
                    await client.say(member.name + " ist neuer Parteileiter!")
                    break
                else:
                    await client.say("User muss Mitglied in der Partei sein.")
        else:
            await client.say("Du musst Parteileiter sein um den Leader zu wechseln.")
    else:
        await client.say("Bitte ändere den Leader mit '!ChangeLeader @Member'.")

async def getLPartyName(context):
    authorroles = context.message.author.roles
    party = ""

    for roles in authorroles:
        if "Leiter" in roles.name:
            party = roles.name.replace("Leiter -", "")
            party = party.strip()
    return party

async def getPartyName(context):
    authorroles = context.message.author.roles
    party = ""

    for roles in authorroles:
        if "Leiter" in roles.name:
            party = roles.name.replace("Leiter -", "")
            party = party.strip()
        if "Sekretär" in roles.name:
            party = roles.name.replace("Sekretär -", "")
            party = party.strip()
    return party


async def getPartyNameNormal(context):
    authorroles = context.message.author.roles
    party = ""

    for roles in authorroles:
        if roles.name in nonpartyroles:
            pass
        elif "Leiter" in roles.name:
            pass
        elif "Sekretär" in roles.name:
            pass
        else:
            party = roles.name

    return party


@client.command(name="DeleteParty",
                description='Lösche eine Partei.',
                brief='Lösche eine Partei.',
                pass_context=True)

async def DeleteParty(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        server= context.message.server
        msg = context.message.content.replace("!DeleteParty","")
        partei = msg.strip()

        parteiliste = await getPartys()

        if partei in parteiliste:
            parteienchannel = discord.Object(id='497356738492629013')
            async for m in client.logs_from(parteienchannel, 100):
                if partei in m.content:
                    await client.delete_message(m)
            parteienchannel = discord.Object(id='498487327484543006')
            async for m in client.logs_from(parteienchannel, 100):
                if partei in m.content:
                    await client.delete_message(m)

            rolelist = server.roles
            targetrole = ""
            targetrole2 = ""
            targetrole3 = ""
            DeleteList = []
            for role in rolelist:
                if partei in role.name:
                    DeleteList.append(role)
                if partei == role.name:
                    targetrole2 = role
                if "Abgeordneter" == role.name:
                    targetrole = role
                if "Kandidat" == role.name:
                    targetrole3 = role


            memberlist = client.get_all_members()
            for member in memberlist:
                if targetrole2 in member.roles:
                    if targetrole in member.roles:
                        await client.remove_roles(member,targetrole)
                    if targetrole3 in member.roles:
                        await client.remove_roles(member,targetrole3)


            for role2 in DeleteList:
                await client.delete_role(server, role2)

            await RemoveVotes()

            channellist = server.channels
            partei = partei.lower()
            partei = partei.replace(" ","-")
            for channel in channellist:
                if channel.name.startswith(partei):
                    await client.delete_channel(channel)
                    await client.say("Partei wurde gelöscht.")
                    break

        else:
            await client.say("Partei nicht gefunden.")

@client.command(name="AddParty",
                description='Füge eine Partei ins System hinzu. Achte auf die Schreibung!',
                brief='Fügt neue Partei hinzu.',
                pass_context=True)

async def AddParty(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        msg = context.message.content
        partei = context.message.content.replace("!AddParty", "")
        try :
            partei,müll = partei.split("<")
        except:
            pass
        partei = partei.strip()
        mention = context.message.mentions
        server = context.message.server
        parteiliste = await getPartys()


        counter = 0
        for i in msg:
            if i == "@":
                counter += 1

        if counter == 1:
            if partei in parteiliste:
                await client.say("Partei exestiert bereits")
            else:

                r= lambda: random.randint(0,255)
                R=r()
                G=r()
                B=r()

                c1= R*65536 + G* 256 + B
                c2 = R*65536 + G * 256 + B
                c3 = R*65536 + G * 256 + B

                #cMitglied= "%d%d%d" %(c1,c2,c3)
                #cSekretär= "%d%d%d" %(c1+50,c2+50,c3+50)
                #cChef= "%d%d%d" %(c1+100,c2+100,c3+100)

                nSekretär= "Sekretär - " + partei
                nChef = "Leiter - " + partei

                await client.send_message(client.get_channel('497356738492629013'),partei + ": 0")
                await client.send_message(client.get_channel('498487327484543006'), partei + ": 0")
                rMitglied = await client.create_role(context.message.server, name= partei, colour=discord.Colour(value= c1))
                rSekretär = await client.create_role(context.message.server, name= nSekretär, colour=discord.Colour(value= c2))
                rChef = await client.create_role(context.message.server, name=nChef , colour=discord.Colour(value= c3))


                everyone_perms = discord.PermissionOverwrite(read_messages=False)
                my_perms = discord.PermissionOverwrite(read_messages=True)
                everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
                pMitglied = discord.ChannelPermissions(target= rMitglied , overwrite=my_perms)
                pSekretär = discord.ChannelPermissions(target= rSekretär, overwrite=my_perms)
                pChef = discord.ChannelPermissions(target= rChef, overwrite=my_perms)
                await client.create_channel(server, partei + ' - Chat', everyone, pMitglied, pSekretär, pChef)


                await client.add_roles(mention[0], rChef)
                print("rChef wurde hinzugefügt")
                await asyncio.sleep(1)
                await client.add_roles(mention[0], rMitglied)
                print("rMitglied wurde hinzugefügt")

                await client.say("Partei " + partei + " wurde erfolgreich erstellt")
        else:
            await client.say("Nenne einen Parteileiter der Partei mit der Form !AddParty Partei XY @Parteileiter")


async def getPartys():
    parteienchannel = discord.Object(id='497356738492629013')
    parteiliste = []
    async for m in client.logs_from(parteienchannel, 100):
        p,rest = m.content.split(":")
        p = p.strip()
        parteiliste.append(p)
    return parteiliste



# @client.command(name="WarAnalyse",
#                 description='Analysiere einen Krieg auf Teilnahme unserer Parteien. Poste dafür den Link des Krieges hinter dem Befehl.',
#                 brief='Einzelkrieganalyse',
#                 pass_context=True)

async def WarAnalyse(context):
    msg = context.message.content.strip()
    msg = msg.replace("WarAnalyse","")
    if msg == "":
        await client.say("Füge hinter dem Befehl einen Kriegslink ein, welcher kein mobiler ist.")
    else:
        parteiliste= await getPartys()
        warurl = context.message.content
        warurl = warurl.replace('!WarAnalyse','')
        warurl = warurl.strip()

        GesamtDamage,partydictRawDmg,partydictPerDmg = rrDamage.RefineDamage(warurl,parteiliste)

        Msg1= "Gesamtschaden des Staatenbundes: " + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2= "Roher Schaden der Parteien:\n"
        Msg3= "\nProzentualer Schaden der Parteien:\n"
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j])+ '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i],2)) + "%\n"
        await client.say(Msg1 + Msg2 + Msg3)

# @client.command(name="WarListAnalyse",
#                 description='Analysiere Kriege aus Datenbank auf Teilnahme unserer Parteien.',
#                 brief='Kriegsanalyse von allen Kriegen',
#                 pass_context=True)

async def WarListAnalyse(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        parteiliste = await getPartys()

        warchannel = discord.Object(id='497356837679529994')
        warliste = []
        async for n in client.logs_from(warchannel, 100):
            warliste.append(n.content)

        GesamtDamage,partydictRawDmg,partydictPerDmg = await rrDamage.MultiWar(warliste,parteiliste)

        #for x in partydictRawDmg:
        #    if partydictRawDmg[x] > 100000000:
        #        await client.say(x + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[x]) + "\n")
        Msg1= "Gesamtschaden des Staatenbundes: " + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2= "Roher Schaden der Parteien:\n"
        Msg3= "\nProzentualer Schaden der Parteien:\n"
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j])+ '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i],2)) + "%\n"
        await client.say(Msg1 + Msg2 + Msg3)

@client.command(name="StateWars",
                description='Analysiere Kriege die in den letzten 21 Tage beendet wurden in unseren Regionen.',
                brief='Kriegsanalyse von allen Kriegen in unseren Regionen letzten 21 Tage',
                pass_context=True)


async def StateWars(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    days= 21

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        parteiliste = await getPartys()

        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        async for n in client.logs_from(stateschannel, 100):
            n=n.content
            n=n.split(":")
            n=n[1].strip()
            stateids.append(n)

        warbase= "http://rivalregions.com/listed/partydamage/"



        TotalWars=0
        Totalwarurllist= await rrDamage.getAllStateWars(stateids,days)
        # for id in stateids:
        #     warlist= await rrDamage.getStateWars(id,days)
        #     for war in warlist:
        #         warurl= warbase + war
        #         Totalwarurllist.append(warurl)
        #         TotalWars+=1

        GesamtDamage, partydictRawDmg, partydictPerDmg = await rrDamage.MultiWar(Totalwarurllist, parteiliste)

        #for x in partydictRawDmg:
        #    if partydictRawDmg[x] > 100000000:
        #        await client.say(x + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[x]) + "\n")
        Msg1 = "Gesamtschaden des Staatenbundes in eigenen Kriegen(%d) während der letzten %d Tage: "%(TotalWars ,days) + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2 = "Roher Schaden der Parteien:\n"
        Msg3 = "\nProzentualer Schaden der Parteien:\n"
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j]) + '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i], 2)) + "%\n"
        await client.say(Msg1 + Msg2 + Msg3)

# @client.command(name="AllDonations21d",
#                 description='Analysiere alle Spenden in unseren Regionen in den letzten 21 Tagen.',
#                 brief='Spendenanalyse aller Regionen in den letzten 21 Tagen',
#                 pass_context=True)


async def AllDonations21d(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    days = 21
    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        parteiliste = await getPartys()

        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        async for n in client.logs_from(stateschannel, 100):
            n=n.content
            n=n.split(":")
            n=n[1].strip()
            stateids.append(n)

        partydon={}
        counter=1
        Gesamtspendenvolumen=0

        marktdict = await readMarktPreise()
        await client.say("Starte Analyse")
        for state in stateids:
            await client.say("Analysiere Staat %d"%counter)
            print("Staat Nr.%d: " %counter + state)
            tempdict = await rrDamage.getStateDonations(state,parteiliste,profildict,marktdict,days)
            print("Staat beendet")
            counter +=1
            for p in tempdict:
                Gesamtspendenvolumen= Gesamtspendenvolumen + tempdict[p]
                if p in partydon:
                    partydon[p] = partydon[p] + tempdict[p]
                else:
                    partydon[p] = tempdict[p]
        await client.say("Analyse abgeschlossen")
        print("Alle Staaten beendet")
        partydonPro={}

        Msg1 = "Gesamtspenden des Staatenbundes während der letzten 21 Tage: " + rrDamage.MakeNumber2PrettyString(Gesamtspendenvolumen) + "\n\n"
        Msg2 = "Spendenvolumen der Parteien:\n"
        Msg3 = "\nProzentuale Spenden der Parteien:\n"
        for j in partydon:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydon[j]) + '\n'
        for i in partydon:
            partydonPro[i] = partydon[i]/Gesamtspendenvolumen * 100
            Msg3 += i + ": " + str(round(partydonPro[i], 2)) + "%\n"

        Spendensitze = partydonPro

        Msg4 = "\nAufteilung der Sitze nach Spenden im Parlament (%d Prozent nach Spenden verteilen):\n" %SpendenProzent

        for s in Spendensitze:
            Spendensitze[s] = Spendensitze[s] / 100 * SpendenProzent

        for o in Spendensitze:
            Msg4 += o + ": " + str(round(Spendensitze[o],2)) + "%\n"

        print("Jetzt müsst er was sagen")
        print(Msg1 + Msg2 + Msg3 + Msg4)
        await asyncio.shield(client.send_message(context.message.channel, Msg1 + Msg2 + Msg3 + Msg4))

@client.command(name='AnalyseWar',
                description='Analysiere einen Krieg',
                brief='Analysiere einen Krieg',
                pass_context=True)

async def AnalyseWar(context):

    msg = context.message.content.replace("!AnalyseWar","")
    if msg == "":
        await client.say("Setze hinter den Befehl einen Kriegslink (nicht mobil).")
    else:
        msg = msg.replace("#war/details","graph/damage")
        msg = msg.strip()
        dmg1h, dmg30min, dmg10min = await rrDamage.KriegsAnalyse(msg)
        await client.say(dmg1h + "\n" + dmg30min + "\n" + dmg10min )



# @client.command(name="StateAndListWars",
#                 description='Analysiere Kriege die in den letzten 21 Tage beendet wurden in unseren Regionen und alle Links aus der Datenbank.',
#                 brief='Kriegsanalyse von allen Kriegen in unseren Regionen letzten 21 Tage und aus der Datenbank',
#                 pass_context=True)


async def StateAndListWars(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        TotalWars = 0
        parteiliste = await getPartys()

        warchannel = discord.Object(id='497356837679529994')
        warliste = []
        async for n in client.logs_from(warchannel, 100):
            warliste.append(n.content)
            TotalWars+=1

        GesamtDamage, partydictRawDmg, partydictPerDmg = await rrDamage.MultiWar(warliste, parteiliste)

        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        async for n in client.logs_from(stateschannel, 100):
            n = n.content
            n = n.split(":")
            n = n[1].strip()
            stateids.append(n)

        warbase = "http://rivalregions.com/listed/partydamage/"

        days = 21
        Totalwarurllist = await rrDamage.getAllStateWars(stateids, days)
        TotalWars = len(Totalwarurllist)
        # for id in stateids:
        #     warlist = await rrDamage.getStateWars(id)
        #     for war in warlist:
        #         warurl = warbase + war
        #         Totalwarurllist.append(warurl)
        #         TotalWars += 1

        GesamtDamage2, partydictRawDmg2, partydictPerDmg2 = await rrDamage.MultiWar(Totalwarurllist, parteiliste)
        GesamtDamage += GesamtDamage2

        for i in partydictRawDmg2:
            if i in partydictRawDmg:
                partydictRawDmg[i] += partydictRawDmg2[i]
            else:
                partydictRawDmg[i] = partydictRawDmg2[i]

        for i in partydictPerDmg2:
            if i in partydictPerDmg:
                partydictPerDmg[i] = partydictRawDmg[i]/GesamtDamage*100
            else:
                partydictPerDmg[i] = partydictPerDmg2[i]/GesamtDamage*100

        Kriegssitze = partydictPerDmg

        Msg1 = "Gesamtschaden des Staatenbundes in eigenen Kriegen während der letzten 21 Tagen und aus der Kriegsliste (insgesamt:%d): "%TotalWars + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2 = "Roher Schaden der Parteien:\n"
        Msg3 = "\nProzentualer Schaden der Parteien:\n"
        Msg4 = "\nAufteilung der Sitze nach Schaden im Parlament (%d Prozent nach Schaden verteilen):\n" %WarProzent
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j]) + '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i], 2)) + "%\n"

        for s in Kriegssitze:
            Kriegssitze[s] = Kriegssitze[s] / 100 * WarProzent

        for o in Kriegssitze:
            Msg4 += o + ": " + str(round(Kriegssitze[o],2)) + "%\n"
        await client.say(Msg1 + Msg2 + Msg3 + Msg4)




@client.command(name='Vote',
                description='Stelle etwas zur Wahl',
                brief='Stelle etwas zur Wahl',
                pass_context=True)

async def Vote(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    nummer=""

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:

        nrchannel = discord.Object(id='501309453358989322')
        async for m in client.logs_from(nrchannel,100):
            content = m.content
            if "Anzahl Gesetze" in content:
                content = content.replace("Anzahl Gesetze:","")
                nummer = int(content.strip())
                nummer = nummer + 1
                nummer = str(nummer)
                await client.edit_message(m, "Anzahl Gesetze: " + nummer)

        msg= context.message.content
        time= context.message.timestamp + datetime.timedelta(hours=25)
        time= time.strftime("%d.%m.%Y %H:%M:%S")
        msg= msg.replace("!Vote ","")
        autor= context.message.author.name
        output= "Gesetzesvorschlag Nr." + nummer +" von " + author.mention + ":\n" + msg + "\nDie Wahl geht bis " + time +"\n Ja-Stimmen: \n Nein-Stimmen: \n"
        newmsg_id = await client.send_message(client.get_channel('496295597632913410'), output)
        #await client.add_reaction(newmsg_id,emoji='👍')
        #await client.add_reaction(newmsg_id,emoji='👎')

@client.command(name='VoteMisstrauen',
                description='Stelle ein Misstrauensvotum gegen den amtierenden Präsidenten',
                brief='Stelle ein Misstrauensvotum gegen den amtierenden Präsidenten',
                pass_context=True)

async def VoteMisstrauen(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    nummer=""

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:

        nrchannel = discord.Object(id='501309453358989322')
        async for m in client.logs_from(nrchannel,100):
            content = m.content
            if "Anzahl Gesetze" in content:
                content = content.replace("Anzahl Gesetze:","")
                nummer = int(content.strip())
                nummer = nummer + 1
                nummer = str(nummer)
                await client.edit_message(m, "Anzahl Gesetze: " + nummer)

        msg= context.message.content
        time= context.message.timestamp + datetime.timedelta(hours=25)
        time= time.strftime("%d.%m.%Y %H:%M:%S")
        msg= "Misstrauensvotum gegen den amtierenden Präsidenten. Stimme mit Ja wenn der Präsident abgesetzt werden soll. Bei Erfolg wird eine Neuwahl eingeleitet. Während dieser Zeit bleibt der Präsident im Amt."
        autor= context.message.author.name
        output= "Gesetzesvorschlag Misstrauensvotum Nr." + nummer +" von " + author.mention + ":\n" + msg + "\nDie Wahl geht bis " + time +"\n Ja-Stimmen: \n Nein-Stimmen: \n"
        newmsg_id = await client.send_message(client.get_channel('496295597632913410'), output)
        #await client.add_reaction(newmsg_id,emoji='👍')
        #await client.add_reaction(newmsg_id,emoji='👎')

@client.command(name='Vote66',
                description='Stelle etwas zur Wahl was mit mehr als 66% bestätigt werden muss',
                brief='Stelle etwas zur Wahl was mit mehr als 66% bestätigt werden muss',
                pass_context=True)

async def Vote66(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    nummer=""

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:

        nrchannel = discord.Object(id='501309453358989322')
        async for m in client.logs_from(nrchannel,100):
            content = m.content
            if "Anzahl Gesetze" in content:
                content = content.replace("Anzahl Gesetze:","")
                nummer = int(content.strip())
                nummer = nummer + 1
                nummer = str(nummer)
                await client.edit_message(m, "Anzahl Gesetze: " + nummer)

        msg= context.message.content
        time= context.message.timestamp + datetime.timedelta(hours=25)
        time= time.strftime("%d.%m.%Y %H:%M:%S")
        msg= msg.replace("!Vote66 ","")
        autor= context.message.author.name
        output= "Gesetzesvorschlag Art66 Nr." + nummer +" von " + author.mention + ":\n" + msg + "\nDie Wahl geht bis " + time +"\n Ja-Stimmen: \n Nein-Stimmen: \n"
        newmsg_id = await client.send_message(client.get_channel('496295597632913410'), output)
        #await client.add_reaction(newmsg_id,emoji='👍')
        #await client.add_reaction(newmsg_id,emoji='👎')

@client.command(name='Vote80',
                description="Stelle etwas zur Wahl was mit mehr als 80% bestätigt werden muss",
                brief="Stelle etwas zur Wahl was mit mehr als 80% bestätigt werden muss",
                pass_context=True)

async def Vote80(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    nummer=""

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:

        nrchannel = discord.Object(id='501309453358989322')
        async for m in client.logs_from(nrchannel,100):
            content = m.content
            if "Anzahl Gesetze" in content:
                content = content.replace("Anzahl Gesetze:","")
                nummer = int(content.strip())
                nummer = nummer + 1
                nummer = str(nummer)
                await client.edit_message(m, "Anzahl Gesetze: " + nummer)

        msg= context.message.content
        time= context.message.timestamp + datetime.timedelta(hours=25)
        time= time.strftime("%d.%m.%Y %H:%M:%S")
        msg= msg.replace("!Vote80 ","")
        autor= context.message.author.name
        output= "Gesetzesvorschlag Art80 Nr." + nummer +" von " + author.mention + ":\n" + msg + "\nDie Wahl geht bis " + time +"\n Ja-Stimmen: \n Nein-Stimmen: \n"
        newmsg_id = await client.send_message(client.get_channel('496295597632913410'), output)
        #await client.add_reaction(newmsg_id,emoji='👍')
        #await client.add_reaction(newmsg_id,emoji='👎')

@client.command(name='RemoveVote',
                description='Ziehe ein Gesetzesvorschlag zurück',
                brief='Ziehe ein Gesetzesvorschlag zurück',
                pass_context=True)

async def RemoveVote(context):
    Berechtigung = False
    msg = context.message.content
    msg = msg.replace("!RemoveVote", "")
    autor = context.message.author
    authorroles = autor.roles
    nummer = int(msg.strip())

    präsichannel = discord.Object(id='504584939245797402')

    async for m in client.logs_from(präsichannel, 100):
        oautor = m.content.author
        content = m.content
        content = content.replace("Gesetzesvorschlag", "")
        content = content.replace("Art66", "")
        content = content.replace("Art80", "")
        content = content.replace("Nr.", "")
        content = content.split("von")
        votenummer = content[0].strip()

        if votenummer == nummer:
            if oautor == autor:
                await client.delete_message(m)
                await client.say("Deine Abstimmung wurde zurückgezogen")
                break
            else:
                await client.say("Du kannst nicht die Vorschläge anderer Leute löschen.")

@client.command(name='VoteP',
                description="PräsiWahl",
                brief="PräsiWahl",
                pass_context=True)

async def VoteP(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False
    nummer=""

    for role in authorroles:
        if "BundBot" in role.name:
            Berechtigung = True
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur BundBot kann diesen Befehl ausführen")
    else:
        #Alle Leiter und Kandidaten holen
        server = context.message.server
        serverroles = server.roles
        servermember = server.members
        Kandidatenlist = []
        for member in server.members:
            memberroles = member.roles
            for role in memberroles:
                if "Leiter" in role.name:
                    Kandidatenlist.append(member)
                if "Kandidat" in role.name:
                    Kandidatenlist.append(member)

        msg= "Neue Präsidentschaftswahlen! \n"
        counter = 1
        for kandidat in Kandidatenlist:
            nummer = counter
            msg = msg + "Kandidat Nr.%d: >>" %nummer + kandidat.name + "<<" +"\n Ja-Stimmen Nr.%d: \n\n" %nummer
            counter+=1

        time= context.message.timestamp + datetime.timedelta(hours=25)
        time= time.strftime("%d.%m.%Y %H:%M:%S")
        msg= msg.replace("!VoteP ","")
        msg= msg + "Die Wahl geht bis " + time
        newmsg_id = await client.send_message(client.get_channel('504584939245797402'), msg)


@client.command(name='PJa',
                description='Stimme für einen Vorschlag mit Ja',
                brief='Stimme als Abgeordneter für einen Präsidenten mit PJa und dr Kandidatennummer. Bsp: !PJa 12',
                pass_context=True)

async def PJa(context):

    Berechtigung = False
    msg = context.message.content
    msg = msg.replace ("!PJa","")
    autor = context.message.author
    authorroles = autor.roles
    nummer = int(msg.strip())
    einsatz = "Ja-Stimmen: " + autor.mention

    präsichannel = discord.Object(id='504584939245797402')

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:
        async for m in client.logs_from(präsichannel, 100):
            content = m.content
            content = content.replace("Ja-Stimmen Nr.%d:" %nummer,"Ja-Stimmen Nr.%d:" %nummer + autor.mention+ " " )
            mentions = m.mentions
            if autor in mentions:
                await client.say("Du hast bereits abgestimmt")
            else:
                await client.edit_message(m,content)
                await client.say("Abstimmung erfolgreich durchgeführt")
                break


@client.command(name='Ja',
                description='Stimme für einen Vorschlag mit Ja',
                brief='Stimme als Abgeordneter für einen Vorschlag mit Ja',
                pass_context=True)

async def Ja(context):

    Berechtigung = False
    msg = context.message.content
    msg = msg.replace ("!Ja","")
    autor = context.message.author
    authorroles = autor.roles
    nummer = msg.strip()
    einsatz = "Ja-Stimmen: " + autor.mention

    vorschlagchannel = discord.Object(id='496295597632913410')

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:
        async for m in client.logs_from(vorschlagchannel, 100):
            content = m.content
            content = content.replace("Gesetzesvorschlag","")
            content = content.replace("Art66", "")
            content = content.replace("Art80", "")
            content = content.replace("Nr.", "")
            content = content.split("von")
            votenummer = content[0].strip()
            oautormention = content[1].split(":")
            oautormention = oautormention[0].strip()
            print(str(oautormention))
            print(str(autor.mention))

            if votenummer == nummer:
                mentions = m.mentions
                autorcount = 0
                if autor in mentions:
                    if str(oautormention) == str(autor.mention):
                        for user in mentions:
                            if str(user) == str(autor.mention):
                                autorcount +=1
                    else:
                        await client.say("Du hast bereits abgestimmt")
                else:
                    if autorcount > 1:
                        await client.say("Du hast bereits abgestimmt")
                    else:
                        output = m.content
                        output1, output2 = output.split("Ja-Stimmen: ")
                        newoutput = output1 + einsatz + output2
                        await client.edit_message(m,newoutput)
                        await client.say("Abstimmung erfolgreich durchgeführt")
                        break

@client.command(name='Nein',
                description='Stimme für einen Vorschlag mit Nein',
                brief='Stimme als Abgeordneter für einen Vorschlag mit Nein',
                pass_context=True)

async def Nein(context):
    Berechtigung = False
    msg = context.message.content
    msg = msg.replace ("!Nein","")
    autor = context.message.author
    authorroles = autor.roles
    nummer = msg.strip()
    einsatz = "Nein-Stimmen: " + autor.mention

    vorschlagchannel = discord.Object(id='496295597632913410')

    for role in authorroles:
        if "Abgeordneter" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur Abgeordnete können diesen Befehl ausführen")
    else:
        async for m in client.logs_from(vorschlagchannel, 100):
            content = m.content
            content = content.replace("Gesetzesvorschlag", "")
            content = content.replace("Art66", "")
            content = content.replace("Art80", "")
            content = content.replace("Nr.", "")
            content = content.split("von")
            votenummer = content[0].strip()
            oautormention = content[1].split(":")
            oautormention = oautormention[0].strip()

            if votenummer == nummer:
                mentions = m.mentions
                autorcount = 0
                if autor in mentions:
                    if oautormention == autor:
                        autorcount += 1
                    else:
                        await client.say("Du hast bereits abgestimmt")
                elif autorcount > 1:
                    await client.say("Du hast bereits abgestimmt")

                else:
                    output = m.content
                    output1, output2 = output.split("Nein-Stimmen:")
                    newoutput = output1 + einsatz + output2
                    await client.edit_message(m,newoutput)
                    await client.say("Abstimmung erfolgreich durchgeführt")
                    break


async def RemoveVotes():
    vorschlagchannel = client.get_channel(id='496295597632913410')
    server = vorschlagchannel.server
    member = server.members

    async for m in client.logs_from(vorschlagchannel, 100):
        content = m.content
        mentions = m.mentions
        for x in member:
            if x in mentions:
                print("in mentions")
                memberroles = x.roles
                bool = False
                for roles in memberroles:
                    if "Abgeordneter" in roles.name:
                        bool = True
                    else:
                        pass
                if bool == False:
                    print (content)
                    print (x.mention)
                    newoutput = content.replace(x.mention,x.name)
                    await client.edit_message(m,newoutput)


async def update_markt_background_task():
    await client.wait_until_ready()
    while not client.is_closed:

        channel = discord.Object(id='508969715830489119')
        async for n in client.logs_from(channel, 100):
            await client.delete_message(n)

        memberlist = client.get_all_members()
        output=[]
        for member in memberlist:
            memberroles = member.roles
            partyname = ""
            for roles in memberroles:
                if "Abgeordneter" in roles.name:
                    for role in memberroles:
                        if role.name in nonpartyroles:
                            pass
                        elif "Sekretär" in role.name:
                            pass
                        elif "Leiter" in role.name:
                            pass
                        else:
                            partyname = role.name
                    output.append(partyname + ": " + member.name)
        output.sort()
        msg = "Anzahl Parlamentarier: " + str(len(output)) +"\n\n"
        msg = msg + "Liste aller Abgeordneten:\n"
        for out in output:
            msg = msg + out +"\n"

        await client.send_message(channel,msg)




        Preise = await rrDamage.getMarktPreise()
        preischannel = discord.Object(id="501786454133833731")
        async for n in client.logs_from(preischannel, 100):
            for stoff in Preise:
                if stoff in n.content:
                    NewOutput = stoff + ": " + rrDamage.MakeNumber2PrettyString(Preise[stoff])
                    await client.edit_message(n, NewOutput)

        await asyncio.sleep(14400)


async def vote_background_task():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Run Background Task")
        channel = discord.Object(id='496295597632913410')
        seatchannel = discord.Object(id='497356738492629013')
        seats = 0.0
        async for n in client.logs_from(seatchannel, 100):
            Partei, Sitze = n.content.split(":")
            Sitze = Sitze.strip()
            seats = seats + int(Sitze)
        now= datetime.datetime.now()
        async for m in client.logs_from(channel,100):
            #content = m.content
            # reaction = m.reactions
            # ups = 0
            # downs = 0
            # Ausgang = ""
            # for n in reaction:
            #     if n.emoji == '👍':
            #
            #         ups = n.count
            #     if n.emoji == '👎':
            #         downs = n.count
            content = m.content
            Gesetz, Abstimmung = content.split("Ja-Stimmen:")
            JaStimmen,NeinStimmen = Abstimmung.split("Nein-Stimmen:")
            Ja = JaStimmen.count("@")
            Nein = NeinStimmen.count("@")
            if "Art66" in content:
                if Ja > seats / 3 * 2 or Nein >= seats / 3 * 1:
                    Ausgang = ""
                    Gesamt = Ja + Nein

                    if Ja / Gesamt * 100 > 66:
                        Ausgang = "Vorschlag frühzeitig angenommen mit %d zu %d Stimmen!" % (Ja, Nein)
                    else:
                        Ausgang = "Vorschlag frühzeitig abgelehnt mit %d zu %d Stimmen" % (Ja, Nein)

                    await client.send_message(client.get_channel('496734924854919178'), Ausgang + "\n" + content)
                    await client.delete_message(m)
            elif "Art80" in content:
                if Ja > seats / 5 * 4 or Nein >= seats / 5 * 1:
                    Ausgang = ""
                    Gesamt = Ja + Nein
                    if Ja / Gesamt * 100 > 80:
                        Ausgang = "Vorschlag frühzeitig angenommen mit %d zu %d Stimmen!" % (Ja, Nein)
                    else:
                        Ausgang = "Vorschlag frühzeitig abgelehnt mit %d zu %d Stimmen" % (Ja, Nein)

                    await client.send_message(client.get_channel('496734924854919178'), Ausgang + "\n" + content)
                    await client.delete_message(m)
            else:
                if Ja > seats/2 or Nein >= seats/2:
                    Ausgang = ""
                    if Ja > Nein:
                        Ausgang = "Vorschlag frühzeitig angenommen mit %d zu %d Stimmen!" % (Ja, Nein)
                    else:
                        Ausgang = "Vorschlag frühzeitig abgelehnt mit %d zu %d Stimmen" % (Ja, Nein)

                    await client.send_message(client.get_channel('496734924854919178'), Ausgang + "\n" + content)
                    await client.delete_message(m)
            try:
                if m.timestamp + datetime.timedelta(hours=24) <= now :
                    content= m.content
                    getMisstrauen = content.split("Nr.")
                    getMisstrauen = getMisstrauen[0]
                    misstrauen = False
                    Ausgang = ""
                    JaCounter = Ja
                    NeinCounter = Nein
                    if "Misstrauensvotum" in getMisstrauen:
                        misstrauen = True
                    if "Art66" in content:
                        if Ja /3 * 1 > Nein / 3 * 2:
                            Ausgang = "Vorschlag angenommen mit %d zu %d Stimmen!" % (Ja, Nein)
                        else:
                            Ausgang = "Vorschlag abgelehnt mit %d zu %d Stimmen" % (Ja, Nein)

                    elif misstrauen == True:
                        if Ja / 3 * 1 > Nein / 3 * 2:
                            Ausgang = "Vorschlag angenommen mit %d zu %d Stimmen!" % (Ja, Nein)
                        else:
                            Ausgang = "Vorschlag abgelehnt mit %d zu %d Stimmen" % (Ja, Nein)
                        await client.send_message(client.get_channel('496295550895783937'), "!PVote")

                    elif "Art80" in content:
                        if Ja / 5 * 1 > Nein / 5 * 4:
                            Ausgang = "Vorschlag frühzeitig angenommen mit %d zu %d Stimmen!" % (Ja, Nein)
                        else:
                            Ausgang = "Vorschlag frühzeitig abgelehnt mit %d zu %d Stimmen" % (Ja, Nein)

                    elif JaCounter > NeinCounter:
                        Ausgang= "Vorschlag angenommen mit %d zu %d Stimmen!" % (JaCounter,NeinCounter)
                    else:
                        Ausgang= "Vorschlag abgelehnt mit %d zu %d Stimmen" % (JaCounter,NeinCounter)

                    # reaction= m.reactions
                    # ups=0
                    # downs=0
                    # Ausgang=""
                    # for n in reaction:
                    #     if n.emoji=='👍':
                    #         ups=n.count
                    #     if n.emoji=='👎':
                    #         downs=n.count
                    #
                    # if ups > downs:
                    #     Ausgang= "Vorschlag angenommen mit %d zu %d Stimmen!" % (ups,downs)
                    # else:
                    #     Ausgang= "Vorschlag abgelehnt mit %d zu %d Stimmen" % (ups,downs)

                    await client.send_message(client.get_channel('496734924854919178'), Ausgang + "\n" + content )
                    await client.delete_message(m)
            except:
                raise


        präsichannel = discord.Object(id='504584939245797402')
        async for m in client.logs_from(präsichannel, 100):
            if m.timestamp + datetime.timedelta(hours=24) <= now:

                print(m.content)

                server = client.get_server("496286798624849921")
                memberlist = client.get_all_members()
                serverroles = server.roles


                targetrole = ""
                targetrole2=""
                targetrole3=""

                for role in serverroles:
                    if role.name == "Präsident":
                        targetrole = role
                    if role.name == "Vize-Präsident":
                        targetrole2 = role
                    if role.name == "Minister":
                        targetrole3 = role

                namen = []
                stimmen= []

                msg = m.content.split("Kandidat Nr.")
                count = 0
                for i in msg:
                    if count != 0:
                        name = i.split(">>")
                        name = name[1].split("<<")
                        name = name[0]
                        namen.append(name)

                    count += 1
                print(namen)

                content = m.content
                content = content.split("Ja-Stimmen Nr.")
                counter= 0
                for s in content:
                    if counter != 0:
                        votes = s.count("@")
                        stimmen.append(int(votes))
                    counter += 1

                merge ={}

                print(stimmen)
                for count, n in enumerate(namen):
                    print(count)
                    print(len(stimmen))
                    merge[n]=int(stimmen[count])


                Gewinner=[]
                max = 0
                for e in merge:
                    print(merge[e])
                    if merge[e] == max:
                        Gewinner.append(e)
                    elif merge[e]>max:
                        max = merge[e]
                        Gewinner.clear()
                        Gewinner.append(e)

                ergebnischannel = discord.Object(id='496734924854919178')


                if len(Gewinner)>1:
                    winner = random.choice(Gewinner)
                    for member in memberlist:
                        if targetrole in member.roles:
                            await client.remove_roles(member, targetrole)
                        if targetrole2 in member.roles:
                            await client.remove_roles(member, targetrole2)
                        if targetrole3 in member.roles:
                            await client.remove_roles(member, targetrole3)
                        if member.name == winner:
                            await client.add_roles(member, targetrole)

                    output = "Ergebnisse der Präsidentschaftswahlen! \n"
                    for n in merge:
                        output = output + n + ": %d Stimmen \n" % merge[n]

                    output = output + "\n Gleichstand! Es wurde durch Zufall der zwischen den Gewinnern entschieden. Gewinner der Wahl ist " + winner
                    await client.send_message(ergebnischannel, output)
                else:
                    for member in memberlist:
                        if targetrole in member.roles:
                            await client.remove_roles(member, targetrole)
                        if targetrole2 in member.roles:
                            await client.remove_roles(member, targetrole2)
                        if targetrole3 in member.roles:
                            await client.remove_roles(member, targetrole3)
                        if member.name == Gewinner[0]:
                            await client.add_roles(member, targetrole)

                    output = "Ergebnisse der Präsidentschaftswahlen! \n"
                    for n in merge:
                        output = output + n + ": %d Stimmen \n" %merge[n]

                    output = output + "\nGewinner der Wahl ist " + Gewinner[0]

                    await client.send_message(ergebnischannel,output)

                await client.delete_message(m)






        await asyncio.sleep(120) # task runs every 60 seconds

# @client.event
# async def on_reaction_add(reaction,user):
#     channel = reaction.message.channel
#     print(channel.id)
#     abstimmungschannel = discord.Object(id='496295597632913410')
#     print(abstimmungschannel.id)
#     reactionlogchannel = discord.Object(id='500952632265801730')
#     if channel.id == abstimmungschannel.id:
#         await client.send_message(reactionlogchannel, user.mention + " hat abgestimmt zur nachrichtenid " + reaction.message.id + " mit " + reaction.emoji)
#
# @client.event
# async def on_reaction_remove(reaction,user):
#     channel = reaction.message.channel
#     abstimmungschannel = discord.Object(id='496295597632913410')
#     reactionlogchannel = discord.Object(id='500952632265801730')
#     if channel.id == abstimmungschannel.id:
#         await client.send_message(reactionlogchannel, user.mention + " hat zur nachrichtenid " + reaction.message.id + " sein " + reaction.emoji + " zurückgenommen.")
#

# @client.command(name= "Reset",
#                  description = 'Reset vom Counter Channel',
#                  brief = 'Reset vom Counter Channel',
#                  pass_context = True)
#
# async def Reset(context):
#      counterchannel = discord.Object(id='501309453358989322')
#      await client.send_message(counterchannel,"Anzahl Parlamentsbildungen: 1")
#      await client.send_message(counterchannel, "Anzahl Gesetze: 7")
#      await client.send_message(counterchannel, "Anzahl Käufe: 0")
#      await client.send_message(counterchannel, "Anzahl Verkäufe: 0")
#
# @client.command(name= "ResetMarkt",
#                 description = 'Reset vom Counter Channel',
#                 brief = 'Reset vom Counter Channel',
#                 pass_context = True)
#
# async def ResetMarkt(context):
#     counterchannel = discord.Object(id='501786454133833731')
#     await client.send_message(counterchannel,"Staatsgold: 5")
#     await client.send_message(counterchannel, "Staatsgeld: 0.8")
#     await client.send_message(counterchannel, "Öl: 155")
#     await client.send_message(counterchannel, "Erz: 155")
#     await client.send_message(counterchannel, "Diamanten: 850000")
#     await client.send_message(counterchannel, "Uran: 1400")

# @client.command(name= "UpdateMarkt",
#                 description = 'Reset vom Counter Channel',
#                 brief = 'Reset vom Counter Channel',
#                 pass_context = True)

async def UpdateMarkt(context):
    Preise = await rrDamage.getMarktPreise()
    preischannel = discord.Object(id="501786454133833731")
    async for n in client.logs_from(preischannel, 100):
        for stoff in Preise:
            if stoff in n.content:
                NewOutput = stoff + ": " + rrDamage.MakeNumber2PrettyString(Preise[stoff])
                await client.edit_message(n,NewOutput)


async def readMarktPreise():
    preischannel = discord.Object(id="501786454133833731")
    marktdict = {}
    print("hello")
    async for n in client.logs_from(preischannel, 100):
        stoff, preis = n.content.split(":")
        stoff = stoff.strip()

        preis = preis.strip()
        if len(preis) < 4 :
            pass
        else:
            preis = preis.replace(".", "")
        marktdict[stoff]= preis
    return marktdict

@client.command(name='Wahlergebnisse',
                description='!Wahlergebnisse Partei 1: 33, Partei 3: 144, Partei x: 231',
                brief='!Wahlergebnisse Partei 1: 33, Partei 3: 144, Partei x: 231',
                pass_context=True)

async def Wahlergebnisse(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:

        msg = context.message.content
        msg = msg.replace("!Wahlergebnisse","")
        msg = msg.split(",")
        print (msg)

        wahldict = {}
        for p in msg:
            partei,stimmen = p.split(":")
            partei = partei.strip()
            stimmen = stimmen.strip()
            wahldict[partei]=stimmen

        Wahlchannel = discord.Object(id='498487327484543006')
        async for n in client.logs_from(Wahlchannel, 100):
            parteien, stimmen = n.content.split(":")
            parteien = parteien.strip()
            stimmen = stimmen.strip()

            if parteien in wahldict:
                stimmen = wahldict[parteien]
                nachricht = parteien + ": " + stimmen
                await client.edit_message(n, nachricht)
            else:
                await client.say(parteien + " nicht gefunden.")
        await client.say("Wahlergebnisse wurden eingetragen")

@client.command(name='RessKauf',
                description='Gib an wenn Ressourcen via Budget Transfer gekauft hast',
                brief='Gib an wenn Ressourcen via Budget Transfer gekauft hast. Bsp: !RessKauf 33.000.000 bbl Achte auf die korrekte Einheit!',
                pass_context=True)

async def RessKauf(context):
    content = context.message.content
    Ress = content.replace("!RessKauf","")
    Ress = Ress.strip()
    if Ress == "":
        await client.say("Du musst einen betrag und die Einheit für den Betrag angebene. Gold: G, Geld: $, Öl: bbl, Erz: kg, Diamanten: pcs, Uran: g. Beispiel: !RessKauf 32.000 pcs")
    elif "$" in Ress or "kg" in Ress or "pcs" in Ress or "G" in Ress or "g" in Ress or "bbl" in Ress:
        Ress = Ress.replace("kkkkk", ".000.000.000.000.000")
        Ress = Ress.replace("kkkk", ".000.000.000.000")
        Ress = Ress.replace("kkk", ".000.000.000")
        Ress = Ress.replace("kk", ".000.000")
        Ress = Ress.replace("k", ".000")
        Ress = Ress.replace("KKKKK", ".000.000.000.000.000")
        Ress = Ress.replace("KKKK", ".000.000.000.000")
        Ress = Ress.replace("KKK", ".000.000.000")
        Ress = Ress.replace("KK", ".000.000")
        Ress = Ress.replace("K", ".000")
        Ress = Ress.replace(".000g", "kg")
        Ress = Ress.strip()

        autor = context.message.author
        authorroles = autor.roles
        autorpartei = ""

        parteiliste = await getPartys()
        for partei in parteiliste:
            for role in authorroles:
                if partei == role.name:
                    autorpartei = partei

        if autorpartei == "":
            await client.say("Du musst einer Partei angehören")
        else:

            counterchannel = discord.Object(id='501309453358989322')
            async for n in client.logs_from(counterchannel, 100):
                if "Käufe" in n.content:
                    müll,anzahl = n.content.split(":")
                    anzahl = anzahl.strip()
                    anzahl = int(anzahl)
                    anzahl = anzahl + 1
                    new_output= "Anzahl Käufe: " + str(anzahl)
                    await client.edit_message(n,new_output)

            KaufChannel = discord.Object(id='501420199723925504')
            await client.send_message(KaufChannel,"Kauf Nr.:" + str(anzahl) + " --- Gekaufte Ressourcen: " + Ress + " --- eingereicht von: " + autor.mention +" --- Partei: " + autorpartei + " --- Check: 0")

    else:
        await client.say("Du musst einen betrag und die Einheit für den Betrag angebene. Gold: G, Geld: $, Öl: bbl, Erz: kg, Diamanten: pcs, Uran: g. Beispiel: !RessKauf 32.000 pcs")

@client.command(name='RessVerkauf',
                description='Gib an wenn Ressourcen via Budget Transfer verkauft hast',
                brief='Gib an wenn Ressourcen via Budget Transfer verkauft hast. Bsp: !RessKauf 33.000.000 bbl Achte auf die korrekte Einheit!',
                pass_context=True)


async def RessVerkauf(context):
    content = context.message.content
    Ress = content.replace("!RessVerkauf","")
    Ress = Ress.strip()
    if Ress == "":
        await client.say("Du musst einen betrag und die Einheit für den Betrag angebene. Gold: G, Geld: $, Öl: bbl, Erz: kg, Diamanten: pcs, Uran: g. Beispiel: !RessKauf 32.000 pcs")
    elif "$" in Ress or "kg" in Ress or "pcs" in Ress or "G" in Ress or "g" in Ress or "bbl" in Ress:
        Ress = Ress.replace("kkkkk", ".000.000.000.000.000")
        Ress = Ress.replace("kkkk", ".000.000.000.000")
        Ress = Ress.replace("kkk", ".000.000.000")
        Ress = Ress.replace("kk", ".000.000")
        Ress = Ress.replace("k", ".000")
        Ress = Ress.replace(".000g", "kg")
        Ress = Ress.strip()
        autor = context.message.author
        authorroles = autor.roles
        autorpartei = ""

        parteiliste = await getPartys()
        for partei in parteiliste:
            for role in authorroles:
                if partei == role.name:
                    autorpartei = partei

        if autorpartei == "":
            await client.say("Du musst einer Partei angehören")
        else:
            counterchannel = discord.Object(id='501309453358989322')
            async for n in client.logs_from(counterchannel, 100):
                if "Verkäufe" in n.content:
                    müll,anzahl = n.content.split(":")
                    anzahl = anzahl.strip()
                    anzahl = int(anzahl)
                    anzahl = anzahl + 1
                    new_output= "Anzahl Verkäufe: " + str(anzahl)
                    await client.edit_message(n,new_output)

            VerkaufChannel = discord.Object(id='501420255416025088')
            await client.send_message(VerkaufChannel,"Verkauf Nr.:" + str(anzahl) + " --- Gekaufte Ressourcen: " + Ress + " --- eingereicht von: " + autor.mention +" --- Partei: " + autorpartei + " --- Check: 0")

    else:
        await client.say("Du musst einen betrag und die Einheit für den Betrag angebene. Gold: G, Geld: $, Öl: bbl, Erz: kg, Diamanten: pcs, Uran: g. Beispiel: !RessKauf 32.000 pcs")

@client.command(name='CheckVerkauf',
                description='AdminTeam verifiziert hiermit eingereichte Verkäufe.',
                brief='AdminTeam verifiziert hiermit eingereichte Verkäufe. Bsp.: !CheckVerkauf 5 - Verifiziert eingereichter Verkauf Nummer 5',
                pass_context=True)

async def CheckVerkauf(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        VerkaufChannel = discord.Object(id='501420255416025088')
        msg = context.message.content.replace("!CheckVerkauf","")
        msg= msg.strip()
        async for n in client.logs_from(VerkaufChannel, 100):
            teile = n.content.split(":")
            Nummer = teile[1].split("---")
            Nummer = Nummer[0].strip()
            if msg == Nummer:
                newOutput = n.content.replace("Check: 0","Check: 1")
                await client.edit_message(n,newOutput)
                await client.say(context.message.author.mention + " hat Kauf Nr." + Nummer + " verifiziert")
                break

@client.command(name='CheckKauf',
                description='AdminTeam verifiziert hiermit eingereichte Käufe.',
                brief='AdminTeam verifiziert hiermit eingereichte Käufe. Bsp.: !CheckKauf 5 - Verifiziert eingereichter Verkauf Nummer 5',
                pass_context=True)

async def CheckKauf(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        KaufChannel = discord.Object(id='501420199723925504')
        msg = context.message.content.replace("!CheckKauf","")
        msg= msg.strip()
        async for n in client.logs_from(KaufChannel, 100):
            teile = n.content.split(":")
            Nummer = teile[1].split("---")
            Nummer = Nummer[0].strip()
            if msg == Nummer:
                newOutput = n.content.replace("Check: 0","Check: 1")
                await client.edit_message(n,newOutput)
                await client.say(context.message.author.mention +  " hat Kauf Nr." + Nummer + " verifiziert")
                break

@client.command(name='DeleteVerkauf',
                description='AdminTeam löscht hiermit eingereichte Verkäufe.',
                brief='AdminTeam löscht hiermit eingereichte Verkäufe. Bsp.: !DeleteVerkauf 5 - Löscht eingereichter Verkauf Nummer 5',
                pass_context=True)

async def DeleteVerkauf(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        VerkaufChannel = discord.Object(id='501420255416025088')
        msg = context.message.content.replace("!DeleteVerkauf","")
        msg= msg.strip()
        async for n in client.logs_from(VerkaufChannel, 100):
            teile = n.content.split(":")
            Nummer = teile[1].split("---")
            Nummer = Nummer[0].strip()
            if msg == Nummer:
                await client.say(context.message.author.mention + " hat Kauf Nr." + Nummer + " gelöscht.\n" + n.content)
                await client.delete_message(n)

                break

@client.command(name='DeleteKauf',
                description='AdminTeam löscht hiermit eingereichte Käufe.',
                brief='AdminTeam löscht hiermit eingereichte Käufe. Bsp.: !DeleteKauf 5 - Löscht eingereichter Verkauf Nummer 5',
                pass_context=True)

async def DeleteKauf(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        KaufChannel = discord.Object(id='501420199723925504')
        msg = context.message.content.replace("!DeleteKauf","")
        msg= msg.strip()
        async for n in client.logs_from(KaufChannel, 100):
            teile = n.content.split(":")
            Nummer = teile[1].split("---")
            Nummer = Nummer[0].strip()
            if msg == Nummer:
                await client.say(context.message.author.mention + " hat Kauf Nr." + Nummer + " gelöscht.\n"+n.content)
                await client.delete_message(n)
                break


@client.command(name='DonationsExtern',
                description='Spenden aus extrenen Käufen und Verkäufen werden hier erfasst und verrechnet.',
                brief='Spenden aus extrenen Käufen und Verkäufen werden hier erfasst und verrechnet.',
                pass_context=True)

async def DonationsExtern(context):
    KaufChannel = discord.Object(id='501420199723925504')
    VerkaufChannel = discord.Object(id='501420255416025088')

    spendendict = {}

    async for n in client.logs_from(KaufChannel, 100):
        msg = n.content.split("---")
        check,nummer = msg[-1].split(":")
        nummer = nummer.strip()
        print("nummer: ", nummer)
        if nummer == "1":
            müll,partei = msg[3].split(":")
            partei = partei.strip()
            müll,spende = msg[1].split(":")
            spende = spende.strip()
            print (partei, spende)
            spende = await rrDamage.RessToMoney(spende)
            print("Calculation= ", spende)
            if partei in spendendict:
                spendendict[partei] = spendendict[partei] + spende
            else:
                spendendict[partei] = spende


    async for n in client.logs_from(VerkaufChannel, 100):
        msg = n.content.split("---")
        check,nummer = msg[-1].split(":")
        nummer = nummer.strip()
        if nummer == "1":
            müll,partei = msg[3].split(":")
            partei = partei.strip()
            müll,spende = msg[1].split(":")
            spende = spende.strip()
            print(partei, spende)
            spende = await rrDamage.RessToMoney(spende)
            print("Calculation= ", spende)
            if partei in spendendict:
                spendendict[partei] = spendendict[partei] - spende
            else:
                spendendict[partei] = 0 - spende

    await client.say(spendendict)

@client.command(name='NewParliamentReal',
                description='Berechne neues Parlament',
                brief='Berechne neues Parlament',
                pass_context=True)

async def NewParliamentReal(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        days = 21
        #Wahl
        Wahlchannel = discord.Object(id='498487327484543006')
        Stimmliste = []
        Parteienliste = []
        msg1= "---WAHLERGEBNISSE---\n\n"
        msg2="Abgegebene Stimmen: "
        msg3="Aufteilung der Stimmen: \n"
        msg4="Stimmen aufgeteilt auf 40% Wahlanteil:\n"
        async for n in client.logs_from(Wahlchannel, 100):
            parteien, stimmen = n.content.split(":")
            parteien = parteien.strip()
            stimmen = stimmen.strip()
            stimmen = int(stimmen)
            Stimmliste.append(stimmen)
            Parteienliste.append(parteien)

        Gesamtstimmen = 0
        for i in Stimmliste:
            Gesamtstimmen += i
        msg2= msg2 + str(Gesamtstimmen) + "\n"
        ParteiStimmenProzente = {}
        for count,partei in enumerate(Parteienliste):
            ParteiStimmenProzente[partei] = round (Stimmliste[count] / Gesamtstimmen * 100,2)
            msg3= msg3 + partei + ": " + str(ParteiStimmenProzente[partei]) + "% \n"
        msg3 = msg3 + "\n"
        for p in ParteiStimmenProzente:
            ParteiStimmenProzente[p] = WahlProzent/100 * ParteiStimmenProzente[p]
            msg4 = msg4 + p + ": " + str(ParteiStimmenProzente[p]) + "% \n"
        msg4 = msg4 + "\n"

        await client.say(msg1 + msg2 + msg3 + msg4 +"\n")

        #Krieg
        TotalWars = 0
        parteiliste = await getPartys()

        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        seats = 0
        async for n in client.logs_from(stateschannel, 100):
            seats += 6
            n = n.content
            n = n.split(":")
            n = n[1].strip()
            stateids.append(n)

        warbase = "http://rivalregions.com/listed/partydamage/"

        Totalwarurllist = await rrDamage.getAllStateWars(stateids, days)
        TotalWars = TotalWars + len(Totalwarurllist)
        # for id in stateids:
        #     warlist = await rrDamage.getStateWars(id)
        #     for war in warlist:
        #         warurl = warbase + war
        #         Totalwarurllist.append(warurl)
        #         TotalWars += 1

        GesamtDamage2, partydictRawDmg2, partydictPerDmg2 = await rrDamage.MultiWar(Totalwarurllist, parteiliste)

        warchannel = discord.Object(id='497356837679529994')
        warliste = []
        async for n in client.logs_from(warchannel, 100):
            wurl = n.content.replace("#", "")
            wurl = wurl.replace("m.", "")
            warliste.append(wurl)
            TotalWars += 1

        for e in warliste:
            if e in Totalwarurllist:
                print("Remove url aus listwars: ", e)
                warliste.remove(e)
        GesamtDamage, partydictRawDmg, partydictPerDmg = await rrDamage.MultiWar(warliste, parteiliste)

        GesamtDamage += GesamtDamage2

        print("Damage vor Verrrechnung: PartydictRawDmg1", partydictRawDmg, " PartydictRawDmg2: ", partydictRawDmg2)
        for i in partydictRawDmg2:
            if i in partydictRawDmg:
                partydictRawDmg[i] += partydictRawDmg2[i]
            else:
                partydictRawDmg[i] = partydictRawDmg2[i]


        for i in partydictRawDmg:
            partydictPerDmg[i] = partydictRawDmg[i] / GesamtDamage * 100

        Kriegssitze = partydictPerDmg
        Msg = "\n---KRIEGSERGEBNISSE---\n\n"
        Msg1 = "Gesamtschaden des Staatenbundes in eigenen Kriegen während der letzten %d Tagen und aus der Kriegsliste (insgesamt:%d): " % (days,TotalWars) + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2 = "Roher Schaden der Parteien:\n"
        Msg3 = "\nProzentualer Schaden der Parteien:\n"
        Msg4 = "\nAufteilung der Sitze nach Schaden im Parlament (%d Prozent nach Schaden verteilen):\n" % WarProzent
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j]) + '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i], 2)) + "%\n"

        for s in Kriegssitze:
            Kriegssitze[s] = Kriegssitze[s] / 100 * WarProzent

        for o in Kriegssitze:
            Msg4 += o + ": " + str(round(Kriegssitze[o], 2)) + "%\n"
        await client.say(Msg + Msg1 + Msg2 + Msg3 + Msg4 + "\n")

        #Spenden
        parteiliste = await getPartys()
        marktdict = await readMarktPreise()
        print(marktdict)

        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        async for n in client.logs_from(stateschannel, 100):
            n = n.content
            n = n.split(":")
            n = n[1].strip()
            stateids.append(n)

        partydon = {}
        counter = 1
        Gesamtspendenvolumen = 0

        for state in stateids:
            print("Staat Nr.%d: " % counter + state)
            tempdict = await rrDamage.getStateDonations(state, parteiliste, profildict,marktdict,days)
            print("Staat beendet")
            counter += 1
            for p in tempdict:
                Gesamtspendenvolumen = Gesamtspendenvolumen + tempdict[p]
                if p in partydon:
                    partydon[p] = partydon[p] + tempdict[p]
                else:
                    partydon[p] = tempdict[p]

        KaufChannel = discord.Object(id='501420199723925504')
        VerkaufChannel = discord.Object(id='501420255416025088')

        async for n in client.logs_from(KaufChannel, 100):
            msg = n.content.split("---")
            check, nummer = msg[-1].split(":")
            nummer = nummer.strip()
            print("nummer: ", nummer)
            if nummer == "1":
                müll, partei = msg[3].split(":")
                partei = partei.strip()
                müll, spende = msg[1].split(":")
                spende = spende.strip()
                print(partei, spende)
                spende = await rrDamage.RessToMoney(spende, marktdict)
                print("Calculation= ", spende)
                Gesamtspendenvolumen = Gesamtspendenvolumen + spende
                if partei in partydon:
                    partydon[partei] = partydon[partei] + spende
                else:
                    partydon[partei] = spende

        async for n in client.logs_from(VerkaufChannel, 100):
            msg = n.content.split("---")
            check, nummer = msg[-1].split(":")
            nummer = nummer.strip()
            if nummer == "1":
                müll, partei = msg[3].split(":")
                partei = partei.strip()
                müll, spende = msg[1].split(":")
                spende = spende.strip()
                print(partei, spende)
                spende = await rrDamage.RessToMoney(spende,marktdict)
                print("Calculation= ", spende)
                Gesamtspendenvolumen = Gesamtspendenvolumen - spende
                if partei in partydon:
                    partydon[partei] = partydon[partei] - spende
                else:
                    partydon[partei] = 0 - spende

        print("Alle Staaten beendet")
        partydonPro = {}

        Msg = "\n---SPENDENERGEBNISSE---\n\n"
        Msg1 = "Gesamtspenden des Staatenbundes während der letzten %d Tagen: " %days + rrDamage.MakeNumber2PrettyString(
            Gesamtspendenvolumen) + "\n\n"
        Msg2 = "Spendenvolumen der Parteien:\n"
        Msg3 = "\nProzentuale Spenden der Parteien:\n"
        for j in partydon:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydon[j]) + '\n'
        for i in partydon:
            partydonPro[i] = partydon[i] / Gesamtspendenvolumen * 100
            Msg3 += i + ": " + str(round(partydonPro[i], 2)) + "%\n"

        Spendensitze = partydonPro

        Msg4 = "\nAufteilung der Sitze nach Spenden im Parlament (%d Prozent nach Spenden verteilen):\n" % SpendenProzent

        for s in Spendensitze:
            Spendensitze[s] = Spendensitze[s] / 100 * SpendenProzent

        for o in Spendensitze:
            Msg4 += o + ": " + str(round(Spendensitze[o], 2)) + "%\n"

        print(Msg + Msg1 + Msg2 + Msg3 + Msg4)
        await asyncio.shield(client.send_message(context.message.channel, Msg + Msg1 + Msg2 + Msg3 + Msg4 + "\n"))

        msg = "\n\n---GESAMTERGEBNISS---\n\n"
        msg1 = "Addierte Prozente der Parteien: \n"
        for partei in ParteiStimmenProzente:
            try:
                ParteiStimmenProzente[partei] += Kriegssitze[partei]
            except:
                pass
            try:
                ParteiStimmenProzente[partei] += Spendensitze[partei]
            except:
                pass

            msg1 = msg1 + partei + ": " + str(round(ParteiStimmenProzente[partei], 2)) + "% \n"
        msg1 = msg1 + "\n"

        # Sitzverteilung
        Gesamtsitze = seats
        Sitzverteilung = {}
        AnzahlParteien = len(parteiliste)
        SaintLoireDivisor = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5,
                             17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5]
        LengthSLD = len(SaintLoireDivisor)
        PlatzArray = np.zeros((LengthSLD, AnzahlParteien))
        RangArray = np.zeros((LengthSLD, AnzahlParteien))

        for count, divisor in enumerate(SaintLoireDivisor):
            for count2, Partei in enumerate(ParteiStimmenProzente):
                PlatzArray[count, count2] = ParteiStimmenProzente[Partei] / divisor

        print(PlatzArray)
        times = Gesamtsitze
        for i in range(times):
            max = 0
            maxindex1 = 0
            maxindex2 = 0
            for count, divisor in enumerate(SaintLoireDivisor):
                for count2, Partei in enumerate(ParteiStimmenProzente):
                    if PlatzArray[count, count2] > max:
                        max = PlatzArray[count, count2]
                        maxindex1 = count
                        maxindex2 = count2
            PlatzArray[maxindex1, maxindex2] = 0
            RangArray[maxindex1, maxindex2] = i + 1

        print(RangArray)

        sitzeliste = np.zeros(AnzahlParteien)
        for count, divisor in enumerate(SaintLoireDivisor):
            for count2, Partei in enumerate(ParteiStimmenProzente):
                if RangArray[count, count2] > 0:
                    sitzeliste[count2] += 1

        for j, partei in enumerate(ParteiStimmenProzente):
            Sitzverteilung[partei] = int(sitzeliste[j])

        msg2 = "Sitzverteilung im Parlament bei %d Sitzen\n" % Gesamtsitze

        # for sitze in ParteiStimmenProzente:
        #     Sitzverteilung[sitze] = round(Gesamtsitze / 100 * ParteiStimmenProzente[sitze])
        #
        # VerschenkteProzente = 0.0
        # for sitze in ParteiStimmenProzente:
        #     if Sitzverteilung[sitze] == 0:
        #         VerschenkteProzente += ParteiStimmenProzente[sitze]

        # print("VerschenkteProzente: ", VerschenkteProzente)
        # AnzahlParteien = 0
        # for sitze in ParteiStimmenProzente:
        #     if Sitzverteilung[sitze] > 0:
        #         AnzahlParteien += 1
        #
        # for sitze in ParteiStimmenProzente:
        #     if Sitzverteilung[sitze] > 0:
        #         ParteiStimmenProzente[sitze] += VerschenkteProzente / AnzahlParteien

        for partei in Sitzverteilung:
            msg2 = msg2 + "Sitze " + partei + ": " + str(Sitzverteilung[partei]) + "\n"

        await client.say(msg + msg1 + msg2 + "\n")

        Sitzchannel = discord.Object(id='497356738492629013')
        Neuesitze=""
        parlamentsparteien = []
        alteSitze = []
        server = context.message.server
        memberlist = server.members
        serverroles = server.roles
        async for n in client.logs_from(Sitzchannel, 100):
            parteiold,sitzeold = n.content.split(":")
            parteiold = parteiold.strip()
            sitzeold = sitzeold.strip()
            parlamentsparteien.append(parteiold)
            alteSitze.append(int(sitzeold))
            await client.delete_message(n)
        parteirole = ""
        targetrole = ""
        counter=0
        AbgeordnetenWatch = discord.Object(id='500952715917000715')

        for oldPartei in parlamentsparteien:
            for Partei in Sitzverteilung:
                if oldPartei == Partei:
                    diff = alteSitze[counter]-Sitzverteilung[Partei]
                    AnzahlAbgeordnete = 0
                    if diff > 0:
                        parteimember = []
                        for roles in serverroles:
                            if Partei == roles.name:
                                parteirole = roles
                            if "Abgeordneter" in roles.name:
                                targetrole = roles
                        for member in memberlist:
                            if parteirole in member.roles:
                                if targetrole in member.roles:
                                    AnzahlAbgeordnete +=1
                                    parteimember.append(member)
                                    print("Parteimembername: ",member.name)
                        diff = Sitzverteilung[Partei]-AnzahlAbgeordnete
                        print("diff = ", diff)
                        if diff < 0 and diff != 0:
                            count = 0
                            while diff < 0:
                                print("Lösche Abgeordnetenrolle von Partei: ", Partei)
                                await client.remove_roles(parteimember[count],targetrole)
                                await client.send_message(AbgeordnetenWatch,parteimember[count].mention + "wurde in Folge der Wahl aus dem Parlamet entlassen")
                                count += 1
                                diff += 1
        await RemoveVotes()

        for Sitze in Sitzverteilung:
            await client.send_message(Sitzchannel,Sitze + ": " + str(Sitzverteilung[Sitze]))

        await client.say("Parlament wurde neu erstellt.")
        channel = discord.Object('496295550895783937')
        await client.send_message(channel,"!VoteP")

@client.command(name='NewParliamentDemo',
                description='Simuliere neues Parlament',
                brief='Simuliere neues Parlament',
                pass_context=True)

async def NewParliamentDemo(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        days = 21
        #Wahl
        Wahlchannel = discord.Object(id='498487327484543006')
        Stimmliste = []
        Parteienliste = []
        msg1= "---WAHLERGEBNISSE---\n\n"
        msg2="Abgegebene Stimmen: "
        msg3="Aufteilung der Stimmen: \n"
        msg4="Stimmen aufgeteilt auf 40% Wahlanteil:\n"
        async for n in client.logs_from(Wahlchannel, 100):
            parteien, stimmen = n.content.split(":")
            parteien = parteien.strip()
            stimmen = stimmen.strip()
            stimmen = int(stimmen)
            Stimmliste.append(stimmen)
            Parteienliste.append(parteien)

        Gesamtstimmen = 0
        for i in Stimmliste:
            Gesamtstimmen += i
        msg2= msg2 + str(Gesamtstimmen) + "\n"
        ParteiStimmenProzente = {}
        for count,partei in enumerate(Parteienliste):
            ParteiStimmenProzente[partei] = round (Stimmliste[count] / Gesamtstimmen * 100,2)
            msg3= msg3 + partei + ": " + str(ParteiStimmenProzente[partei]) + "% \n"
        msg3 = msg3 + "\n"
        for p in ParteiStimmenProzente:
            ParteiStimmenProzente[p] = round(WahlProzent/100 * ParteiStimmenProzente[p],2)
            msg4 = msg4 + p + ": " + str(ParteiStimmenProzente[p]) + "% \n"
        msg4 = msg4 + "\n"

        await client.say(msg1 + msg2 + msg3 + msg4 +"\n")

        #Krieg
        TotalWars = 0
        parteiliste = await getPartys()




        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        seats = 0
        async for n in client.logs_from(stateschannel, 100):
            seats += 6
            n = n.content
            n = n.split(":")
            n = n[1].strip()
            stateids.append(n)

        warbase = "http://rivalregions.com/listed/partydamage/"

        Totalwarurllist = await rrDamage.getAllStateWars(stateids, days)
        TotalWars = TotalWars + len(Totalwarurllist)
        # for id in stateids:
        #     warlist = await rrDamage.getStateWars(id)
        #     for war in warlist:
        #         warurl = warbase + war
        #         Totalwarurllist.append(warurl)
        #         TotalWars += 1

        GesamtDamage2, partydictRawDmg2, partydictPerDmg2 = await rrDamage.MultiWar(Totalwarurllist, parteiliste)

        warchannel = discord.Object(id='497356837679529994')
        warliste = []
        async for n in client.logs_from(warchannel, 100):
            wurl = n.content.replace("#","")
            wurl = wurl.replace("m.","")
            warliste.append(wurl)
            TotalWars += 1

        for e in warliste:
            if e in Totalwarurllist:
                print("Remove url aus listwars: ",e)
                warliste.remove(e)

        GesamtDamage, partydictRawDmg, partydictPerDmg = await rrDamage.MultiWar(warliste, parteiliste)

        GesamtDamage += GesamtDamage2

        print("Damage vor Verrrechnung: PartydictRawDmg1", partydictRawDmg, " PartydictRawDmg2: ", partydictRawDmg2)
        for i in partydictRawDmg2:
            if i in partydictRawDmg:
                partydictRawDmg[i] += partydictRawDmg2[i]
            else:
                partydictRawDmg[i] = partydictRawDmg2[i]


        for i in partydictRawDmg:
            partydictPerDmg[i] = partydictRawDmg[i] / GesamtDamage * 100

        Kriegssitze = partydictPerDmg
        Msg = "\n---KRIEGSERGEBNISSE---\n\n"
        Msg1 = "Gesamtschaden des Staatenbundes in eigenen Kriegen während der letzten %d Tagen und aus der Kriegsliste (insgesamt:%d): " % (days,TotalWars) + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2 = "Roher Schaden der Parteien:\n"
        Msg3 = "\nProzentualer Schaden der Parteien:\n"
        Msg4 = "\nAufteilung der Sitze nach Schaden im Parlament (%d Prozent nach Schaden verteilen):\n" % WarProzent
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j]) + '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i], 2)) + "%\n"

        for s in Kriegssitze:
            Kriegssitze[s] = Kriegssitze[s] / 100 * WarProzent

        for o in Kriegssitze:
            Msg4 += o + ": " + str(round(Kriegssitze[o], 2)) + "%\n"
        await client.say(Msg + Msg1 + Msg2 + Msg3 + Msg4 + "\n")

        #Spenden
        marktdict = await readMarktPreise()
        print(marktdict)
        parteiliste = await getPartys()

        stateschannel = discord.Object(id='497356879840935936')
        stateids = []
        async for n in client.logs_from(stateschannel, 100):
            n = n.content
            n = n.split(":")
            n = n[1].strip()
            stateids.append(n)

        partydon = {}
        counter = 1
        Gesamtspendenvolumen = 0

        for state in stateids:
            print("Staat Nr.%d: " % counter + state)
            tempdict = await rrDamage.getStateDonations(state, parteiliste, profildict,marktdict,days)
            print("Staat beendet")
            counter += 1
            for p in tempdict:
                Gesamtspendenvolumen = Gesamtspendenvolumen + tempdict[p]
                if p in partydon:
                    partydon[p] = partydon[p] + tempdict[p]
                else:
                    partydon[p] = tempdict[p]

        print(partydon)
        KaufChannel = discord.Object(id='501420199723925504')
        VerkaufChannel = discord.Object(id='501420255416025088')

        async for n in client.logs_from(KaufChannel, 100):
            msg = n.content.split("---")
            check, nummer = msg[-1].split(":")
            nummer = nummer.strip()
            print("nummer: ", nummer)
            if nummer == "1":
                müll, partei = msg[3].split(":")
                partei = partei.strip()
                müll, spende = msg[1].split(":")
                spende = spende.strip()
                print(partei, spende)
                spende = await rrDamage.RessToMoney(spende,marktdict)
                print("Calculation= ", spende)
                Gesamtspendenvolumen = Gesamtspendenvolumen + spende
                if partei in partydon:
                    partydon[partei] = partydon[partei] + spende
                else:
                    partydon[partei] = spende

        async for n in client.logs_from(VerkaufChannel, 100):
            msg = n.content.split("---")
            check, nummer = msg[-1].split(":")
            nummer = nummer.strip()
            if nummer == "1":
                müll, partei = msg[3].split(":")
                partei = partei.strip()
                müll, spende = msg[1].split(":")
                spende = spende.strip()
                print(partei, spende)
                spende = await rrDamage.RessToMoney(spende,marktdict)
                print("Calculation= ", spende)
                Gesamtspendenvolumen = Gesamtspendenvolumen - spende
                if partei in partydon:
                    partydon[partei] = partydon[partei] - spende
                else:
                    partydon[partei] = 0 - spende

        print("Alle Staaten beendet")
        partydonPro = {}

        Msg = "\n---SPENDENERGEBNISSE---\n\n"
        Msg1 = "Gesamtspenden des Staatenbundes während der letzten %d Tagen: " %days + rrDamage.MakeNumber2PrettyString(
            Gesamtspendenvolumen) + "\n\n"
        Msg2 = "Spendenvolumen der Parteien:\n"
        Msg3 = "\nProzentuale Spenden der Parteien:\n"
        for j in partydon:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydon[j]) + '\n'
        for i in partydon:
            partydonPro[i] = partydon[i] / Gesamtspendenvolumen * 100
            Msg3 += i + ": " + str(round(partydonPro[i], 2)) + "%\n"

        Spendensitze = partydonPro

        Msg4 = "\nAufteilung der Sitze nach Spenden im Parlament (%d Prozent nach Spenden verteilen):\n" % SpendenProzent

        for s in Spendensitze:
            Spendensitze[s] = Spendensitze[s] / 100 * SpendenProzent

        for o in Spendensitze:
            Msg4 += o + ": " + str(round(Spendensitze[o], 2)) + "%\n"

        print(Msg + Msg1 + Msg2 + Msg3 + Msg4)
        await asyncio.shield(client.send_message(context.message.channel, Msg + Msg1 + Msg2 + Msg3 + Msg4 + "\n"))

        msg = "\n\n---GESAMTERGEBNISS---\n\n"
        msg1 = "Addierte Prozente der Parteien: \n"
        for partei in ParteiStimmenProzente:
            try:
                ParteiStimmenProzente[partei] += Kriegssitze[partei]
            except:
                pass
            try:
                ParteiStimmenProzente[partei] += Spendensitze[partei]
            except:
                pass

            msg1 = msg1 + partei + ": " + str(round(ParteiStimmenProzente[partei], 2)) + "% \n"
        msg1 = msg1 + "\n"

        # Sitzverteilung
        Gesamtsitze = seats
        Sitzverteilung = {}
        AnzahlParteien = len(parteiliste)
        SaintLoireDivisor = [0.5 , 1.5 , 2.5 , 3.5, 4.5 , 5.5, 6.5, 7.5, 8.5, 9.5 , 10.5, 11.5, 12.5, 13.5 ,14.5 ,15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5,29.5,30.5]
        LengthSLD = len(SaintLoireDivisor)
        PlatzArray = np.zeros((LengthSLD, AnzahlParteien))
        RangArray = np.zeros((LengthSLD, AnzahlParteien))

        for count, divisor in enumerate(SaintLoireDivisor):
            for count2,Partei in enumerate(ParteiStimmenProzente):
                PlatzArray[count,count2]= ParteiStimmenProzente[Partei] / divisor

        print (PlatzArray)
        times = Gesamtsitze
        for i in range(times):
            max = 0
            maxindex1 = 0
            maxindex2 = 0
            for count, divisor in enumerate(SaintLoireDivisor):
                for count2, Partei in enumerate(ParteiStimmenProzente):
                    if PlatzArray[count, count2] > max:
                        max = PlatzArray[count,count2]
                        maxindex1 = count
                        maxindex2 = count2
            PlatzArray[maxindex1,maxindex2] = 0
            RangArray [maxindex1,maxindex2] = i + 1

        print(RangArray)

        sitzeliste = np.zeros(AnzahlParteien)
        for count, divisor in enumerate(SaintLoireDivisor):
            for count2, Partei in enumerate(ParteiStimmenProzente):
                if RangArray[count, count2] > 0:
                    sitzeliste[count2] += 1

        for j,partei in enumerate(ParteiStimmenProzente):
            Sitzverteilung[partei] = int(sitzeliste[j])

        msg2 = "Sitzverteilung im Parlament bei %d Sitzen\n" % Gesamtsitze

        # for sitze in ParteiStimmenProzente:
        #     Sitzverteilung[sitze] = round(Gesamtsitze / 100 * ParteiStimmenProzente[sitze])
        #
        # VerschenkteProzente = 0.0
        # for sitze in ParteiStimmenProzente:
        #     if Sitzverteilung[sitze] == 0:
        #         VerschenkteProzente += ParteiStimmenProzente[sitze]

        # print("VerschenkteProzente: ", VerschenkteProzente)
        # AnzahlParteien = 0
        # for sitze in ParteiStimmenProzente:
        #     if Sitzverteilung[sitze] > 0:
        #         AnzahlParteien += 1
        #
        # for sitze in ParteiStimmenProzente:
        #     if Sitzverteilung[sitze] > 0:
        #         ParteiStimmenProzente[sitze] += VerschenkteProzente / AnzahlParteien

        for partei in Sitzverteilung:
            msg2 = msg2 + "Sitze " + partei + ": " + str(Sitzverteilung[partei]) + "\n"

        await client.say(msg + msg1 + msg2 + "\n")



# @client.command(name='Bayern14D',
#                 description='Simuliere Bayern in den letzten 14D',
#                 brief='Simuliere Bayern in den letzten 14D',
#                 pass_context=True)

async def Bayern14D(context):
    author = context.message.author
    authorroles = author.roles
    Berechtigung = False

    for role in authorroles:
        if "AdminTeam" in role.name:
            Berechtigung = True

    if Berechtigung == False:
        await client.say("Nur das Admin Team kann diesen Befehl ausführen")
    else:
        #Wahl
        Wahlchannel = discord.Object(id='498487327484543006')
        Stimmliste = []
        Parteienliste = []
        msg1= "---WAHLERGEBNISSE---\n\n"
        msg2="Abgegebene Stimmen: "
        msg3="Aufteilung der Stimmen: \n"
        msg4="Stimmen aufgeteilt auf 40% Wahlanteil:\n"
        async for n in client.logs_from(Wahlchannel, 100):
            parteien, stimmen = n.content.split(":")
            parteien = parteien.strip()
            stimmen = stimmen.strip()
            stimmen = int(stimmen)
            Stimmliste.append(stimmen)
            Parteienliste.append(parteien)

        Gesamtstimmen = 0
        for i in Stimmliste:
            Gesamtstimmen += i
        msg2= msg2 + str(Gesamtstimmen) + "\n"
        ParteiStimmenProzente = {}
        for count,partei in enumerate(Parteienliste):
            ParteiStimmenProzente[partei] = round (Stimmliste[count] / Gesamtstimmen * 100,2)
            msg3= msg3 + partei + ": " + str(ParteiStimmenProzente[partei]) + "% \n"
        msg3 = msg3 + "\n"
        for p in ParteiStimmenProzente:
            ParteiStimmenProzente[p] = WahlProzent/100 * ParteiStimmenProzente[p]
            msg4 = msg4 + p + ": " + str(ParteiStimmenProzente[p]) + "% \n"
        msg4 = msg4 + "\n"

        await client.say(msg1 + msg2 + msg3 + msg4 +"\n")

        #Krieg
        TotalWars = 0
        parteiliste = ["Haus Wittelsbach", "Haus Sachsen-Coburg und Gotha", "North Atlantic Pirates", "N SEVEN", "Demokratische Union Österreich", "Haus Montfort", "Kaiserliche Garde", "European Empire Germany", "Neue Toastregierung 2", "Midgard Security Unit", "Bund Deutscher Demokraten", "Der Widerstand", "Haus Hoch Überlegen", "☆Elite☆", "Demokratische Freiheitspartei", "Deutsche Spätzle Koalition", "Soziale Grüne Partei"]
        days = 14

        warchannel = discord.Object(id='497356837679529994')
        warliste = []
        async for n in client.logs_from(warchannel, 100):
            warliste.append(n.content)
            TotalWars += 1

        GesamtDamage, partydictRawDmg, partydictPerDmg = await rrDamage.MultiWar(warliste, parteiliste)



        stateids = ["2792"]

        warbase = "http://rivalregions.com/listed/partydamage/"

        Totalwarurllist = await rrDamage.getAllStateWars(stateids, days)
        TotalWars = TotalWars + len(Totalwarurllist)
        # for id in stateids:
        #     warlist = await rrDamage.getStateWars(id)
        #     for war in warlist:
        #         warurl = warbase + war
        #         Totalwarurllist.append(warurl)
        #         TotalWars += 1

        GesamtDamage2, partydictRawDmg2, partydictPerDmg2 = await rrDamage.MultiWar(Totalwarurllist, parteiliste)
        GesamtDamage += GesamtDamage2

        print("Damage vor Verrrechnung: PartydictRawDmg1", partydictRawDmg, " PartydictRawDmg2: ", partydictRawDmg2)
        for i in partydictRawDmg2:
            if i in partydictRawDmg:
                partydictRawDmg[i] += partydictRawDmg2[i]
            else:
                partydictRawDmg[i] = partydictRawDmg2[i]


        for i in partydictRawDmg:
            partydictPerDmg[i] = partydictRawDmg[i] / GesamtDamage * 100

        Kriegssitze = partydictPerDmg
        Msg = "\n---KRIEGSERGEBNISSE---\n\n"
        Msg1 = "Gesamtschaden in Bayern in den letzten 14 Tagen (Kriege insgesamt:%d): " % TotalWars + rrDamage.MakeNumber2PrettyString(GesamtDamage) + "\n\n"
        Msg2 = "Roher Schaden der Parteien:\n"
        Msg3 = "\nProzentualer Schaden der Parteien:\n"
        Msg4 = "\nAufteilung der Sitze nach Schaden im Parlament (%d Prozent nach Schaden verteilen):\n" % WarProzent
        for j in partydictRawDmg:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydictRawDmg[j]) + '\n'
        for i in partydictPerDmg:
            Msg3 += i + ": " + str(round(partydictPerDmg[i], 2)) + "%\n"

        for s in Kriegssitze:
            Kriegssitze[s] = Kriegssitze[s] / 100 * WarProzent

        for o in Kriegssitze:
            Msg4 += o + ": " + str(round(Kriegssitze[o], 2)) + "%\n"
        await client.say(Msg + Msg1 + Msg2 + Msg3 + Msg4 + "\n")

        #Spenden
        marktdict = await readMarktPreise()
        print(marktdict)

        partydon = {}
        counter = 1
        Gesamtspendenvolumen = 0


        for state in stateids:
            print("Staat Nr.%d: " % counter + state)
            tempdict = await rrDamage.getStateDonations(state, parteiliste, profildict,marktdict,days)
            print("Staat beendet")
            counter += 1
            for p in tempdict:
                Gesamtspendenvolumen = Gesamtspendenvolumen + tempdict[p]
                if p in partydon:
                    partydon[p] = partydon[p] + tempdict[p]
                else:
                    partydon[p] = tempdict[p]

        print("Alle Staaten beendet")
        partydonPro = {}

        Msg = "\n---SPENDENERGEBNISSE---\n\n"
        Msg1 = "Gesamtwert der Spenden im Königreich Bayern während der letzten 14 Tage: " + rrDamage.MakeNumber2PrettyString(
            Gesamtspendenvolumen) + "\n\n"
        Msg2 = "Spendenvolumen der Parteien:\n"
        Msg3 = "\nProzentuale Spenden der Parteien:\n"
        for j in partydon:
            Msg2 += j + ": " + rrDamage.MakeNumber2PrettyString(partydon[j]) + '\n'
        for i in partydon:
            partydonPro[i] = partydon[i] / Gesamtspendenvolumen * 100
            Msg3 += i + ": " + str(round(partydonPro[i], 2)) + "%\n"

        Spendensitze = partydonPro

        Msg4 = "\nAufteilung der Sitze nach Spenden im Parlament (%d Prozent nach Spenden verteilen):\n" % SpendenProzent

        for s in Spendensitze:
            Spendensitze[s] = Spendensitze[s] / 100 * SpendenProzent

        for o in Spendensitze:
            Msg4 += o + ": " + str(round(Spendensitze[o], 2)) + "%\n"

        print(Msg + Msg1 + Msg2 + Msg3 + Msg4)
        await asyncio.shield(client.send_message(context.message.channel, Msg + Msg1 + Msg2 + Msg3 + Msg4 + "\n"))

        msg= "\n\n---GESAMTERGEBNISS---\n\n"
        msg1= "Addierte Prozente der Parteien: \n"
        for partei in ParteiStimmenProzente:
            try:
                ParteiStimmenProzente[partei]+= Kriegssitze[partei]
            except:
                pass
            try:
                ParteiStimmenProzente[partei] += Spendensitze[partei]
            except:
                pass

            msg1= msg1 + partei + ": " + str(round(ParteiStimmenProzente[partei],2)) +"\n"
        msg1 = msg1 + "\n"


        await client.say(msg + msg1)
        print(ParteiStimmenProzente)





@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Willkommen {0.mention} auf dem Server des Staatenbundes! Um verifiziert zu werden poste bitte ein Screenshot deines RR Profils. Akzeptiert werden alle Bürger des Staatenbundes. Eines unserer Teammitglieder wird dann die Daten genauer prüfen und dich bei erfolgreicher Prüfung auf dem Server verifizieren.'
    await client.send_message(client.get_channel('496286798624849923'), fmt.format(member, server))

@client.command(name='Jukebox',
                description="Best of Pariston Songs",
                brief='Lass mich zu Pariston singen.',
                aliases=['Musik','Music','Song'],
                pass_context=True)



async def Jukebox(context):
    possible_responses = [
        'Julie - Der perfekte Zeuge: Das ist der perfekte Zeuge, das ist der perfekte Mann, lass dich einfach von ihm missionieren, schon bist du in Paristons Bann.',
        'Haftbefehl - Zeugen wissen wer die Gottheit ist: Zeugen wissen, wer die Gottheit ist, Gotti Pari ist der, der in Sänfte und im Himmel sitzt, Mosambik Gold Rich, Wissen, wer Safari ritzt.',
        'Scorpions - Wind of Pariston: Take me to the only true belief, in the whole world, where the zeugen of tomorrow pray ahead, in the wind of Pariston.',
        'Frei Wild - Land der Paristoten: Das ist das Land der Paristoten, die denken Gottes Plan hat noch viel parat, wir sind reine Glaubensbrüder und keine Kurasisten, wir kenn einfach den echten Weg, Parsem.',
        'Sportfreunde Stiller - Parsem Parsem: Parsem Parsem, auf deinen Glauben, er stieg hinauf, und er wacht, Parsem Parsem, Für seine Art mich zu missionieren, Hör niemals damit auf! Pariston mein Herr, hör bitte niemals damit auf.',
        'Feine Sahne Fischfilet - Ich bin komplett im Bann: Ich bin komplett im Bann, Pariston wacht über mich, Ich bin komplett im Bann, Er hat ein Plan wie es weiter geht. Ich bin komplett im Bann. Noch mehr Zeugen wünsch ich mir, Ich bin komplett im Bann, will sofort alle missionieren.',
        'Cro - Meinen Bann: Alles was ich brauch ist meinen Bann, meinen Bann, denn keiner kennt mich so wie Pariston, Pariston, Wirf deine Blicke ind die Luft! (Pahar sem Pahar sem) Bin schon lange Zeuge und hoffe du auch, auch, auch!',
        'Trailerpark - Beten kannst du überall: Junge, du sitzt immer nur zu Hause vorm Pc, Geh doch auch mal raus für Gebete. (okay) Beten kannst du überall! Morgens beim Warten im Bus, andere liegen beim heiligen Gruß NO PRAY NO LIFE!',
        'Rammstein - Käse: Eins, hier kommt der Käse. Zwei, hier kommt der Käse. Drei, Er ist der klebrigste Käse von allen. Vier, hier kommt der Käse.'
        'Helene Fischer - Pariston auch in der Nacht: Pariston auch in der Nacht, der Erlöser über uns wacht, Pariston unser Haus, Seine Famile nimmt dich auf, Pariston auch in der Nacht, spüre was sein Wort mit dir macht.',
        'Alligatoah - Willst du?: Willst du mit mir Klinken putzen? Dann wird uns Pariston beschützen. Missionieren ist unser größter Nutzen. Willst du mit mir Klinken putzen?',
        'Kraftklub - Songs an Pariston: Wenn du betest, sreibt Dean wieder Songs an Pariston. Wenn du betest! Wenn du betest, komm unsere Freunde zurück aus TSE. Wenn du betest! Wenn du betest, dann allein oder wollen wir beide? Wenn du betest!',
        'The Cranberries - Pariston: With their love and their prays, and their prays and their words, in your head in your head he`s seeing youuuu. In your heaaaaad, in your hee heeaadd, Pariston, Pariston, Pariston, ton, ton. He`s in your heaaaad, in your heee heeead! Pariston, Pariston, Pariston, ton, ton, ton oh Par Par Par Par Par Paaaar.',
        'Rabauken - Was wollen wir beten?: Was wollen wir beten, für Pariston man, was wollen wir beten, unser Gott!',
        'Comedian Harmonists - Mein kleiner frommer Zeuge: Ein kleiner frommer Zeuge, steht draußen vor der Tür, Holari, holari, holaro! Was wird er mir wohl sagen? Was bin ich schon nervös. Holari, Holari, Holaro! Nun öffne ich dir Klink, steht Paristons gutes Kind, holt einmal ganz tief Luft, und er spricht, spricht, spricht. Ein kleiner frommer Zeuge, steht draußen vor der Tür, Holari, holari, hollaro!',
        'Lynard Skynard - Sweet Home bei den Zeugen: Big wheels keep on turning. Carry me home to see my Pariston. Singing songs about the Zeugen. I miss Pariston once again. And I think its a sin, yes. Well I heard the Zeugen sing about him Well, I heard ol` Nico put him up Well, I hope every Zeuge will remember A Zeugen-man always needs him around, anyhow. Sweet home bei den Zeugen. Where the skies are so blue. Sweet Home bei den Zeugen. Pariston, I`m coming home to you!',
        'Fürstenfeld - S.T.S.: I brauch kan Gürtel i brauch kan Ring, I will z`ruck hintern Pariston. I brauch nur des bissl Göid Für die Fahrt zu Pariston. I will wieder ham, fühl mi do so allan. I brauch ka grosse Welt, i will ham zu Pariston. I will wieder ham, fühl mi do so allan. I brauch ka grosse Welt, i will ham zu Pariston.'
        ' Laudato si, o-mi Pariston. Laudato si, o-mi Pariston. Laudato si, o-mi Pariston. Laudato si, o-mi Pariston. Sei gepriesen, du hast die Welt erschaffen. Sei gepriesen, für Sonne, Mond und Sterne. Sei gepriesen, für Meer und Kontinente. Sei gepriesen, denn du bist wunderbar, Herr!'

    
    ]
    await client.say(random.choice(possible_responses))

@client.command(name='Huldigung',
                description="Konversation über den Kult führen.",
                brief='Lass mich zu Pariston huldigen',
                aliases=['Gebet','Predigt','Gespräch'],
                pass_context=True)

async def Huldigung(context):
    possible_responses = [
        'Es kann nur einen wahren Gott geben. Parsem Pariston.',
        'Ein Glaubensbruder ist für mich wie ein echter Bruder',
        'Warum Pariston der wahre Gott ist? Ich hab ihn gefragt, er verneinte. Diese Bescheidenheit hat nur ein wahrer Gott',
        'Was wären wir ohne Pariston, meine Brüder?',
        'Ritualmeister Nico macht einen zufriedenstellenden Job.',
        'Die letzte Ausgabe vom Leuchtturm hat mir ser gefallen.',
        'Für mich ist Zeuge der Woche Raion. Er präsentiert uns in den Artikeln wie kein anderer.',
        'Riecht es für euch hier auch nach Heiligtum?',
        'Schließe deine Augen und erinnere dich an die letzten Worte Paristons. Welche waren diese?',
        'Manchmal werde ich gefragt ob Kuras heilig wäre. Natürlich ist er das, er ist Kaiser in Gnaden Paristons.',
        'Könnt ihr euch noch an die Gemälde von Mohnarchfalter erinnern? Für mich immer wieder ein Ort zur Entspannung.',
        'Die Begnung Raions mit Pariston fand ich sehr inspirierend. Wie fandet ihr sie?',
        'Wie die Erde, die Pflanzen, die Meere und die Völker, so hat auch mich Pariston mit seinen heiligen Fingern erschaffen.',
        'Goldenes Haar, pinker Anzug, Zeuge na klar, alles andere wär Unfug.',
        'Willst du mit mir Klinken putzen?',
        'Meine Brüder, ihr müsst euch jeden Tag fragen: Was habe ich heute bereits für Pariston getan?',
        'Wer denkst wer du bist, hier auf dem Server nicht mal deine Schuhe auszuziehen?',
        'Gibt es was zu tun, mein Bruder?',
        'Essen? Trinken? Frauen? Ich brauch nur eins im Leben und das ist der große Pariston. Parsem mein Bruder',
        'Manchmal frag ich mich, ob die Freizeitzeugen einfach nur cool sein wollen mit dem Zeugennamen dahinter. Dann sag ich mir, es sind sicher nur stumme Glaubensbrüder.',
        'Entsagt allem weltlichen und dem Streben nach Macht, damit ihr euch komplett auf die Liebe zu unserem Heiland und Erlöser konzentrieren könnt.',
        'Vertraut auf Pariston unseren Herren. Er wird uns alle auf den richtigen Weg und in das Paradies führen.',
        'Das ewige Licht des Leuchtturms leuchte euch den Weg in die Arme unseres Erlösers.',
        'Rosen sind rot, Veilchen sind blau. Bist du kein Zeuge, wanderst du in den Bau.',
        'Vater Pariston im Himmel. Geheiligt werde deine Herrlichkeit. Dein Reich expandiere, Dein Wille geschehe. Wie bei den Zeugen, So überall auf Erden. Und vergib uns unsere Schuld, Wie auch wir vergeben unseren Schuldigern. Führe uns nicht in Kuras Arme,Sondern erlöse uns von dem Bösen. Denn du bist allwissend, gutaussehend und wunderbar. In Ewigkeit, Parsem.',
        'Ich werde nie vergessen wie Raion durch die Hallen des Paristons als erstes in wenigen Minuten durchmaschiert ist. So viel Wissen über unseren Erleuchter hätte ich auch gern.',
        'Hast du schonmal von Knäckebrot gehört? Guter Glaubensbruder.',
        'Viele Neulinge finden grad zum echten Glauben, ich denke uns stehen rosige Zeiten bevor.',
        'Es war dieser einer Tag in der Dusche. Ich hatte wieder Überstunden bei McDonalds machen müssen und Streß weil alle HappyMeal Spielzeuge alle waren. Komplett kaputt zu hause unter der Dusche dachte ich dann: Pariston, falls es dich gibt, gib mir ein Zeichen! Durch das Fenster am Duschvorhang vorbei wichen die Wolken der Berührung Paristons. Meine Haut erschien in seinem Anlitz und es wurde überall warm. Da war mir bewusst, es gibt ihn wirklich.',
        'Habt ihr schon eure Tipps für Tippspiel abgeben. Unser große Pariston weisten uns nur selten so deutlich den Weg, meine Brüder.',
        'Mal rein hypothetisch wir hätten Ungläubige hier: Düfrte ich ihren Account auf Discord sperren? Ich frag für ein Freund.',
        'Meine Zeugennummer werde ich nie vergessen. Pariston gab sie mir persönlich - in Hexadezimal <3',
        'Paristons Taten versetzen mich immer wieder ins Staunen. Mit welch einer Ausdauer und Liebe er sich seinen Söhnen und Töchtern widmet ist für mich jeden Tag aufs Neue ein Wunder.',
        'Ich kann mir gar nicht vorstellen, dass unser Pariston einst ein berühmter Bierpirat war. Sugoi!',
        'Psst, soll ich dir n Geheimnis erzählen? Der Parteiführer der BDD Barash. Das ist auch n Zeuge. Aber Undercover. Genauso wie Kuras und Daryl. Letztere können aber bei weiterm besser schauspielern.',
        'Holt Areon hierher, er soll die Leistungsträger im Chat waschen! - Oh falsche Zeit, oder?',
        'Manchmal frage ich mich, ob es schonmal Tage gab, an denen Didam und Schwüppe nicht grumpy waren. Dann denke ich mir, dass unser Pariston sicher auch mit ihnen ein höheren Plan verfolgt.',
        'Weißt du wer den Reifen erfunden hat? Ich auch nicht. Aber Pariston weiß es.',
        'Ich hab gehört Pariston kann mit einem Fingerwink Bilder,Texte und Personen bannen. Er muss ein Gott sein!',
        'Sorry hab grad n bisschen gedöst, was möchtest du?',
        'Treffen sich Costa, Kuras und Pariston beim Döner. Sagt Pariston:"Ich lad euch ein meine Söhne". Happy End.',
        'Hätte Pariston in Game of Thrones mit gespielt, wäre schon längst ein Zeuge auf dem Eisernen Thron.',
        'Hab letztens Hunter X Hunter geschaut, finde es toll wie außerordentlich clever sie Pariston dort darstellen.',
       
    ]
    await client.say('Lieber Bruder ' + context.message.author.mention + ': ' + random.choice(possible_responses))

@client.command(name='Ave',
                description="Freundliche Begrüßung",
                brief='Ave Pariston',
                aliases=['Ave Pariston'],
                pass_context=True)

async def Ave(context):
    await client.say('Ave Pariston!')


#add_roles(member,*roles)
#remove_roles(member,*roles)
role_ID= [
    '439551402994565120',
    '441135292930588672',
    '441135385850937345'
    ]

# @client.command(name='Game',
#                 description="Die Hallen des Paristons",
#                 brief='Die Halen des Paristons',
#                 aliases=['Check','Start','Antwort'],
#                 pass_context=True)
#
#
#
# async def Game(context):
#     # we do not want the bot to reply to itself
#     if context.message.author == client.user:
#         return
#
#     if context.message.content.startswith('!Check'):
#         channel = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen')
#         print(channel)
#         role = discord.utils.get(context.message.server.roles, name="Halle3")
#         print(role.id)
#         #await client.add_roles(message.author,'Halle11')
#     elif context.message.content.startswith('!Start'):
#         roleID = discord.utils.get(context.message.server.roles, name="Halle1")
#         channel = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen',name='halle1')
#         await client.add_roles(context.message.author,roleID)
#         await client.send_message(channel, content= 'Willkommen in der ersten Halle des Paristons, Bruder ' + context.message.author.mention + '. Löse das Rätsel und rücke vor von Halle zu Halle bis du die Halle der glorreichen Zeugen erreichst! Nun denn, das 1.Rätsel: Wer wacht über dich tagein tagaus? Für eine Antwort schreibe !Antwort DEINE ANTWORT . Beginne stehts mit einem Großbuchstaben. Viel Spaß!')
#
#     elif context.message.content.startswith('!Antwort'):
#         #Halle 1
#         if context.message.channel.name == 'halle1':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort1):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle1")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle2")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle2')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Das war die richtige Antwort. Willkommen in Halle Nr.2. Aber das war erst der Anfang. Wirst du auch das nächste Rätsel lösen können? Es lautet folgendermaßen: Wie heißt das heilige Blatt der Zeugen Paristons?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#
#         #Halle 2
#         elif context.message.channel.name == 'halle2':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort2):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle2")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle3")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle3')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Erneut die richtige Antwort. Willkommen in Halle Nr.3. Das nächste wird etwas schwerer: Zu wem sagte Pariston auf seinen Reisen `Fürchte dich nicht mein Sohn. Wir werden Großes vollbringen.`?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#         #Halle 3
#         elif context.message.channel.name == 'halle3':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort3):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle3")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle4")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle4')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.4. Schön dass du dich an die Worte Raions erinnern konntest. Er ist ein wahrlich würdiger Freizeitzeuge. Ich hoffe er eröffnet bald seinen eigenen Ortsverein. Aber ich schweife ab. Nächstes Rätsel: Wo treffen sich Paralellen?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#
#         #Halle 4
#         elif context.message.channel.name == 'halle4':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort4):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle4")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle5")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle5')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.5. Ich sehe du nimmst dir die Worte Paristons zu Herzen, das freut mich sehr mein Glaubensbruder. Dann sollte die nächste Aufgabe für dich kein Problem sein: Wofür steht das dritte K in KKKK?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#
#         #Halle 5
#         elif context.message.channel.name == 'halle5':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort5):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle5")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle6")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle6')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.6. Du machst guten Fortschritt. Gleich die nächste hinterher! Der einzig wahre Pariston ist nicht nur Staatsführer, Parteiführer und Gottheit, sondern auch...?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#
#         #Halle 6
#         elif context.message.channel.name == 'halle6':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort6):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle6")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle7")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle7')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.7. Schon wieder korrekt. Falls du noch kein Zeuge bist solltest du dich definitv bei Bruder Nico melden, dieser wird dich durch das Aufnahmeritual führen. Ab dieser Halle kommen aber nur noch die wahren Zeuge Paristons weiter: In welcher Region ist Pariston geboren worden?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#         #Halle 7
#         elif context.message.channel.name == 'halle7':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort7):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle7")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle8")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle8')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.8. Das wussten sicher nicht viele, dennoch hast du es geschafft und bist der Siegerhalle ein Stückchen weitegekommen. Wirst du es bis zum Schluss schaffen? Dafür musst du folgendes wissen: Wer ist Kaiser in Paristons Namen?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#
#         #Halle 8
#         elif context.message.channel.name == 'halle8':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort8):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle8")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle9")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle9')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.9. Diesen Fakt haben leider viele noch nicht begriffen. Arbeite auch du im Chat daran um dies zu ändern. Auch der nächste Fakt sollte klar sein: Wer ist Paristons Vorbild?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#         #Halle 9
#         elif context.message.channel.name == 'halle9':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort9):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle9")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="Halle10")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle10')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.10, der letzten Halle. Du hast es weit gebracht, doch wirst du auch die letzte Frage korrekt beantworten? Was war Pariston in seinem früheren Leben?')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
#         #Halle 10
#         elif context.message.channel.name == 'halle10':
#             if context.message.content.endswith('!Antwort'):
#                 await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
#             elif context.message.content.endswith(Antwort10):
#                 roleID1 = discord.utils.get(context.message.server.roles, name="Halle10")
#                 roleID2 = discord.utils.get(context.message.server.roles, name="HdP-Sieger")
#                 channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='siegerhalle')
#                 await client.delete_message(context.message)
#                 await client.say('Bruder ' + context.message.author.mention + ' hat das Spiel erfolgreich beendet!')
#                 await client.add_roles(context.message.author, roleID2)
#                 await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Du hast das Spiel "Die Hallen des Paristons" gewonnen! Gratulation mein Bruder. Ich hoffe es hat dir Spaß gemacht auf dieser witzigen Art und Weise ein paar Glaubensfragen aufzufrischen.')
#                 await client.remove_roles(context.message.author, roleID1)
#             else:
#                 await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)







@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(update_markt_background_task())
client.loop.create_task(vote_background_task())
client.run(os.getenv('TOKEN'))


