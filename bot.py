from discord.ext.commands import Bot
import random

BOT_PREFIX = ("?","!","")
BOT_TOKEN = "NDQwNTM3NDg1MDM1MTc1OTM2.DcjKdA.J4xpMIXR_3JZ5Pb3HgyzwlPham8"

client = Bot(command_prefix=BOT_PREFIX)

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
    await client.say(random.choice(possible_responses) +  ', Bruder ' + context.message.author.mention)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(BOT_TOKEN)
