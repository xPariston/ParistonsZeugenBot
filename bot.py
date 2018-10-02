from discord.ext.commands import Bot
import discord
import random
import asyncio
import os

BOT_PREFIX = ("!")

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

@client.command(name='Vote',
                description='Stelle etwas zur Wahl',
                brief='Stelle etwas zur Wahl',
                pass_context=True)

async def Vote(context):
    msg= context.message.content
    msg= msg[6:-1]
    await client.say(msg)

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




client.run(os.getenv('TOKEN'))


