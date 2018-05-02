from discord.ext.commands import Bot
import discord
import random
import asyncio

BOT_PREFIX = ("?","!")
BOT_TOKEN = "NDQwNTM3NDg1MDM1MTc1OTM2.DcjKdA.J4xpMIXR_3JZ5Pb3HgyzwlPham8"

client = Bot(command_prefix=BOT_PREFIX)

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
        'Für mich ist Zeuge der Woche Adir. Er präsentiert uns im Chat wie kein anderer.',
        'Riecht es für euch hier auch nach Heiligtum?',
        'Schließe deine Augen und erinnere dich an die letzten Worte Paristons. Welche waren diese?',
        'Manchmal werde ich gefragt ob Kuras heilig wäre. Natürlich ist er das, er ist Kaiser in Gnaden Paristons.',
        'Könnt ihr euch noch an die Gemälde von Mohnarchfalter erinnern? Für mich immer wieder ein Ort zur Entspannung.',
        'Die Begnung Raions mit Pariston fand ich sehr inspirierend. Wie fandet ihr sie?',
        'Wie die Erde, die Pflanzen, die Meere und die Völker, so hat auch mich Pariston mit seinen heiligen Fingern erschaffen.',
        'Goldenes Haar, pinker Anzug, Zeuge na klar, alles andere wär Unfug.',
        'Willst du mit mir Klinken putzen?',
        'Meine Brüder, ihr müsst euch jeden Tag fragen: Was habe ich heute bereits für Pariston getan?',
        'Angelo muss endlich mal Spenden einsammeln. Wie ssonst sollen wir das Gold für Pariston finanzieren?',
        'Wer denkst wer du bist, hier auf dem Server nicht mal deine Schuhe auszuziehen?',
        'Gibt es was zu tun, mein Bruder?',
        'Essen? Trinken? Frauen? Ich brauch nur eins im Leben und das ist der große Pariston. Parsem mein Bruder',
        'Manchmal frag ich mich, ob die Freizeitzeugen einfach nur cool sein wollen mit dem Zeugennamen dahinter. Dann sag ich mir, es sind sicher nur stumme Glaubensbrüder.',

    ]
    await client.say('Lieber Bruder ' + context.message.author.mention + ': ' + random.choice(possible_responses))

#add_roles(member,*roles)
#remove_roles(member,*roles)
role_ID= [
    '439551402994565120',
    '441135292930588672',
    '441135385850937345'
    ]

@client.command(name='Game',
                description="Die Hallen des Paristons",
                brief='Die Halen des Paristons',
                aliases=['Check','Start','Antwort'],
                pass_context=True)



async def Game(context):
    # we do not want the bot to reply to itself
    if context.message.author == client.user:
        return

    if context.message.content.startswith('!Check'):
        channel = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen')
        print(channel)
        role = discord.utils.get(context.message.server.roles, name="Halle3")
        print(role.id)
        #await client.add_roles(message.author,'Halle11')
    elif context.message.content.startswith('!Start'):
        roleID = discord.utils.get(context.message.server.roles, name="Halle1")
        channel = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen',name='halle1')
        await client.add_roles(context.message.author,roleID)
        await client.send_message(channel, content= 'Willkommen in der ersten Halle des Paristons, Bruder ' + context.message.author.mention + '. Löse das Rätsel und rücke vor von Halle zu Halle bis du die Halle der glorreichen Zeugen erreichst! Nun denn, das 1.Rätsel: Wer wacht über dich tagein tagaus? Für eine Antwort schreibe !Antwort DEINE ANTWORT . Beginne stehts mit einem Großbuchstaben. Viel Spaß!')

    elif context.message.content.startswith('!Antwort'):
        #Halle 1
        if context.message.channel.name == 'halle1':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort1):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle1")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle2")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle2')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Das war die richtige Antwort. Willkommen in Halle Nr.2. Aber das war erst der Anfang. Wirst du auch das nächste Rätsel lösen können? Es lautet folgendermaßen: Wie heißt das heilige Blatt der Zeugen Paristons?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)

        #Halle 2
        elif context.message.channel.name == 'halle2':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort2):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle2")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle3")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle3')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Erneut die richtige Antwort. Willkommen in Halle Nr.3. Das nächste wird etwas schwerer: Zu wem sagte Pariston auf seinen Reisen `Fürchte dich nicht mein Sohn. Wir werden Großes vollbringen.`?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
        #Halle 3
        elif context.message.channel.name == 'halle3':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort3):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle3")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle4")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle4')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.4. Schön dass du dich an die Worte Raions erinnern konntest. Er ist ein wahrlich würdiger Freizeitzeuge. Ich hoffe er eröffnet bald seinen eigenen Ortsverein. Aber ich schweife ab. Nächstes Rätsel: Wo treffen sich Paralellen?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)

        #Halle 4
        elif context.message.channel.name == 'halle4':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort4):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle4")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle5")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle5')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.5. Ich sehe du nimmst dir die Worte Paristons zu Herzen, das freut mich sehr mein Glaubensbruder. Dann sollte die nächste Aufgabe für dich kein Problem sein: Wofür steht das dritte K in KKKK?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)

        #Halle 5
        elif context.message.channel.name == 'halle5':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort5):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle5")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle6")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle6')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.6. Du machst guten Fortschritt. Gleich die nächste hinterher! Der einzig wahre Pariston ist nicht nur Staatsführer, Parteiführer und Gottheit, sondern auch...?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)

        #Halle 6
        elif context.message.channel.name == 'halle6':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort6):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle6")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle7")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle7')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.7. Schon wieder korrekt. Falls du noch kein Zeuge bist solltest du dich definitv bei Bruder Nico melden, dieser wird dich durch das Aufnahmeritual führen. Ab dieser Halle kommen aber nur noch die wahren Zeuge Paristons weiter: In welcher Region ist Pariston geboren worden?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
        #Halle 7
        elif context.message.channel.name == 'halle7':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort7):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle7")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle8")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle8')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.8. Das wussten sicher nicht viele, dennoch hast du es geschafft und bist der Siegerhalle ein Stückchen weitegekommen. Wirst du es bis zum Schluss schaffen? Dafür musst du folgendes wissen: Wer ist Kaiser in Paristons Namen?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)

        #Halle 8
        elif context.message.channel.name == 'halle8':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort8):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle8")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle9")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle9')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.9. Diesen Fakt haben leider viele noch nicht begriffen. Arbeite auch du im Chat daran um dies zu ändern. Auch der nächste Fakt sollte klar sein: Wer ist Paristons Vorbild?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
        #Halle 9
        elif context.message.channel.name == 'halle9':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort9):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle9")
                roleID2 = discord.utils.get(context.message.server.roles, name="Halle10")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='halle10')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' ist eine Halle aufgestiegen!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Willkommen in Halle Nr.10, der letzten Halle. Du hast es weit gebracht, doch wirst du auch die letzte Frage korrekt beantworten? Was war Pariston in seinem früheren Leben?')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)
        #Halle 10
        elif context.message.channel.name == 'halle10':
            if context.message.content.endswith('!Antwort'):
                await client.say('Bruder' + context.message.author.mention + ', nichts ist eine sehr weise Antwort, dennoch hier nicht richig. Um das Rätsel zu lösen schreibe deine Antwort hinter den !Antwort Befehl. Viel Glück!')
            elif context.message.content.endswith(Antwort10):
                roleID1 = discord.utils.get(context.message.server.roles, name="Halle10")
                roleID2 = discord.utils.get(context.message.server.roles, name="HdP-Sieger")
                channel2 = discord.utils.get(client.get_all_channels(), server__name='Paristons Zeugen', name='siegerhalle')
                await client.delete_message(context.message)
                await client.say('Bruder ' + context.message.author.mention + ' hat das Spiel erfolgreich beendet!')
                await client.add_roles(context.message.author, roleID2)
                await client.send_message(channel2,content='Gratulation Bruder' + context.message.author.mention + '! Du hast das Spiel "Die Hallen des Paristons" gewonnen! Gratulation mein Bruder. Ich hoffe es hat dir Spaß gemacht auf dieser witzigen Art und Weise ein paar Glaubensfragen aufzufrischen.')
                await client.remove_roles(context.message.author, roleID1)
            else:
                await client.say('Leider die falsche Antwort, Bruder ' + context.message.author.mention)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')




client.run(BOT_TOKEN)


