#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator für "Klausens Märchenwelt".
Erzeugt index.html und je eine Seite pro Geschichte (geschichte-N.html).
Der volle Text steht direkt im HTML -> barrierefrei, funktioniert ohne JavaScript.
"""

import html
import os

HIER = os.path.dirname(os.path.abspath(__file__))

# --- Die neun Geschichten --------------------------------------------------
# absatz = Liste von Absätzen (für gute Lesbarkeit)
GESCHICHTEN = [
    {
        "symbol": "🧵",
        "titel": "Der Fadenweber am Rande der Welt",
        "kurz": "Ein alter Mann webt aus dünner Luft den Faden, der jene verbindet, die einander nie begegnen.",
        "absaetze": [
            "Es lebte einmal ein alter Mann, den niemand sah. Er saß am Rande der Welt, dort wo die Farben langsam verblassen, und webte aus dünner Luft einen unendlich langen Faden.",
            "Jeden Morgen begann er von Neuem, denn der Faden riss jede Nacht. Ein Wanderer kam vorbei und fragte: Was webst du da, Alter?",
            "Der Alte sagte: Ich webe die Verbindung zwischen denen, die einander nie begegnen werden. Zwischen einem Kind, das im Dunkeln weint, und einem Erwachsenen, der denselben Schmerz kennt aber vergessen hat.",
        ],
    },
    {
        "symbol": "✨",
        "titel": "Die Sternenstaubsammlerin",
        "kurz": "Lina fürchtet die Dunkelheit – bis ein goldener Staubkorn in ihr Zimmer tanzt und sie um Hilfe bittet.",
        "absaetze": [
            "Es war einmal ein kleines Mädchen namens Lina, das schlief nie richtig ein, weil es Angst vor der Dunkelheit hatte.",
            "Eines Nachts, als der Himmel besonders klar war, erschien ein winziger, goldener Staubkorn in ihrem Zimmer. Es tanzte und flüsterte: Ich bin ein verlorener Gedanke von jemandem, der gerade friedlich eingeschlafen ist. Sammelst du mich?",
            "Lina setzte sich auf und nahm den Staubkorn in ihre hohle Hand. Er war warm und leicht wie eine Feder.",
        ],
    },
    {
        "symbol": "🌉",
        "titel": "Die Brücke aus Sternenstaub",
        "kurz": "Zwischen den Ufern Gestern und Morgen hängt eine Brücke, unter der ein Fischer Träume aus Mondlicht fängt.",
        "absaetze": [
            "Es war einmal eine kleine Brücke aus vergessenem Sternenstaub, die zwischen zwei Ufern hing, die niemand mehr kannte.",
            "Das eine Ufer hieß Gestern, das andere Morgen, und dazwischen floss ein Fluss aus lauter ungelebten Augenblicken.",
            "Unter der Brücke wohnte ein alter Fischer, der mit einem Netz aus Mondlicht die verlorenen Träume der Menschen fing.",
        ],
    },
    {
        "symbol": "🪔",
        "titel": "Die kleine Laterne am Rand der Welt",
        "kurz": "Ein warmes, goldenes Licht am Rand der dunklen Ebene, an dem müde Wanderer Rast finden.",
        "absaetze": [
            "Es war einmal eine kleine Laterne, die stand ganz allein am Rand einer weiten, dunklen Ebene.",
            "Jede Nacht zündete ein alter Laternenwärter ihr Licht an, und dieses Licht war nicht hell und grell, sondern warm und golden, wie die Farbe von Erinnerungen an einen Sommertag.",
            "Jeden Abend kamen Menschen vorbei, müde von der weiten Reise, und setzten sich neben die Laterne.",
        ],
    },
    {
        "symbol": "🗿",
        "titel": "Der Steinmetz",
        "kurz": "In einem Land mit wolkenhohen Bergen schnitzt ein Steinmetz aus Liebe – keine Helden, sondern Tiere.",
        "absaetze": [
            "Es war einmal in einem Land, wo die Berge so hoch waren, dass ihre Spitzen in den Wolken verschwanden, und wo der Wind nie aufhörte zu flüstern, dass ein kleiner Steinmetz lebte.",
            "Er hielt es nicht für einen Beruf, sondern für eine Liebe. Jeden Morgen ging er zum Fluss, wählte den schönsten glatten Stein und trug ihn nach Hause, um ihn zu bearbeiten.",
            "Er schnitzte keine Statuen von Helden oder Königen, er schnitzte Tiere.",
        ],
    },
    {
        "symbol": "🌙",
        "titel": "Der kleine Mond Luma",
        "kurz": "Ein verlorener Mond, der zu keinem Planeten gehört, hört eines Nachts das Meer zu sich sprechen.",
        "absaetze": [
            "Es war einmal ein kleiner Mond namens Luma, der es leid war, jede Nacht allein am Himmel zu hängen.",
            "Alle anderen Monde hatten ihre Planeten, um die sie kreisten, aber Luma gehörte zu keinem, er war ein verlorener Mond, der durch die Dunkelheit irrte.",
            "Eines Nachts hörte er unter sich ein leises Flüstern. Es war das Meer, das zu ihm sprach: Komm näher, kleiner Mond, und wirf dein Licht auf meine Wellen.",
        ],
    },
    {
        "symbol": "🌊",
        "titel": "Der alte Mann und das Meer",
        "kurz": "Ein alter Mann wirft seine Sorgen ins Meer – und ein Kind versteht, warum gerade das funktioniert.",
        "absaetze": [
            "Es war einmal ein alter Mann der am Meer saß und Steine ins Wasser warf. Jeden Tag kam ein Kind vorbei und fragte ihn warum er das tue. Der Mann antwortete nicht, er warf nur weiter.",
            "Nach vielen Wochen fragte das Kind wieder, diesmal lauter, und der Mann sagte leise, ich werfe meine Sorgen ins Meer.",
            "Das Kind setzte sich neben ihn und sagte, aber Großvater, das Meer ist so groß und deine Sorgen sind so klein. Da lächelte der Mann und erwiderte, genau deshalb funktioniert es ja.",
        ],
    },
    {
        "symbol": "⏳",
        "titel": "Der Uhrmacher Eldwin",
        "kurz": "In einem vergessenen Tal baut Eldwin keine Uhren, die die Zeit zählen – sondern das Verstehen.",
        "absaetze": [
            "Es war einmal in einem Tal, das so abgelegen lag, dass niemand mehr wusste, wer es einst benannt hatte. Dort, am Rand eines stillen Sees, lebte ein alter Uhrmacher namens Eldwin.",
            "Seine Hände waren nicht mehr die schnellsten, aber seine Augen sahen Dinge, die jüngere längst übersehen hatten.",
            "Eldwin baute keine gewöhnlichen Uhren. Er baute Uhren, die nicht die Zeit zählten, sondern das Verstehen.",
        ],
    },
    {
        "symbol": "💫",
        "titel": "Der Sternenstaubmacher",
        "kurz": "Hoch über den Wolken macht Orin den Staub für die Sternschnuppen – aus den stillen Wünschen der Menschen.",
        "absaetze": [
            "Hoch über den Wolken, dort wo die Luft so dünn ist, dass Vögel nicht mehr fliegen können, lebt ein alter Mann namens Orin.",
            "Er wohnt in einer Hütte aus Nebel und Mondlicht, und sein Beruf ist der schönste der Welt: Er macht den Staub für die Sternschnuppen.",
            "Jeden Abend sitzt Orin vor seiner Hütte und fängt die stillen Gedanken der Menschen ein, all die unausgesprochenen Wünsche, die vergessenen Träume, die leisen Sehnsüchte, die sich niemand zu sagen traut.",
        ],
    },
]

NUM_WORT = ["", "Eins", "Zwei", "Drei", "Vier", "Fünf",
            "Sechs", "Sieben", "Acht", "Neun"]


def kopf(titel, beschreibung, in_unterseite=False):
    """Gemeinsamer <head> + Sternen-Container + Mond."""
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{html.escape(beschreibung)}">
<title>{html.escape(titel)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip-link" href="#inhalt">Zum Inhalt springen</a>
<div id="sterne" aria-hidden="true"></div>
<div class="mond" aria-hidden="true"></div>
<div class="seite">
"""


def navigation():
    return """<nav class="haupt" aria-label="Hauptnavigation">
  <a class="marke" href="index.html">✦ Klausens Märchenwelt</a>
  <ul>
    <li><a href="index.html">Startseite</a></li>
    <li><a href="index.html#geschichten">Geschichten</a></li>
  </ul>
</nav>
"""


def fuss():
    return """<footer>
  <p><span class="stern-zeichen">✦</span> Klausens Märchenwelt <span class="stern-zeichen">✦</span></p>
  <p>Neun stille Geschichten für große und kleine Träumer.</p>
</footer>
</div>
<script src="sterne.js"></script>
</body>
</html>
"""


def baue_index():
    karten = []
    for i, g in enumerate(GESCHICHTEN, start=1):
        karten.append(f"""    <a class="karte" href="geschichte-{i}.html">
      <span class="symbol" aria-hidden="true">{g['symbol']}</span>
      <span class="nummer">Geschichte {NUM_WORT[i]}</span>
      <h3>{html.escape(g['titel'])}</h3>
      <p>{html.escape(g['kurz'])}</p>
      <span class="mehr">Weiterlesen &rsaquo;</span>
    </a>""")
    karten_html = "\n".join(karten)

    return (
        kopf("Klausens Märchenwelt – Neun Geschichten unter dem Sternenhimmel",
             "Klausens Märchenwelt: neun poetische Geschichten in elegantem, "
             "dunklem Design mit goldenem Sternenhimmel.")
        + navigation()
        + f"""<header class="hero">
  <h1>Klausens Märchenwelt</h1>
  <p class="untertitel">Wo die Farben verblassen und die Sterne flüstern – neun
  stille Geschichten vom Rande der Welt.</p>
  <a class="btn-gold" href="#geschichten">Die Geschichten entdecken</a>
  <div class="trenner"></div>
</header>

<main id="inhalt">
  <section id="geschichten" aria-labelledby="geschichten-titel">
    <h2 id="geschichten-titel" class="abschnitt-titel">Die neun Geschichten</h2>
    <p class="abschnitt-unter">Wähle eine Karte und tritt ein in ihre Welt.</p>
    <div class="karten">
{karten_html}
    </div>
  </section>
</main>
"""
        + fuss()
    )


def baue_geschichte(i, g):
    absaetze = []
    for k, a in enumerate(g["absaetze"]):
        klasse = ' class="erster"' if k == 0 else ""
        absaetze.append(f"      <p{klasse}>{html.escape(a)}</p>")
    absaetze_html = "\n".join(absaetze)

    # Vor / Zurück
    if i > 1:
        prev = f'<a href="geschichte-{i-1}.html">&laquo; {html.escape(GESCHICHTEN[i-2]["titel"])}</a>'
    else:
        prev = '<span class="platzhalter"></span>'
    if i < len(GESCHICHTEN):
        nxt = f'<a href="geschichte-{i+1}.html">{html.escape(GESCHICHTEN[i]["titel"])} &raquo;</a>'
    else:
        nxt = '<span class="platzhalter"></span>'

    return (
        kopf(f"{g['titel']} – Klausens Märchenwelt", g["kurz"])
        + navigation()
        + f"""<main id="inhalt">
  <article class="geschichte">
    <span class="symbol-gross" aria-hidden="true">{g['symbol']}</span>
    <span class="nummer">Geschichte {NUM_WORT[i]}</span>
    <h1>{html.escape(g['titel'])}</h1>
    <div class="text">
{absaetze_html}
    </div>
  </article>

  <nav class="geschichte-nav" aria-label="Weitere Geschichten">
    {prev}
    <a href="index.html#geschichten">Alle Geschichten</a>
    {nxt}
  </nav>
</main>
"""
        + fuss()
    )


def schreibe(name, inhalt):
    pfad = os.path.join(HIER, name)
    with open(pfad, "w", encoding="utf-8") as f:
        f.write(inhalt)
    return pfad


def main():
    erzeugt = [schreibe("index.html", baue_index())]
    for i, g in enumerate(GESCHICHTEN, start=1):
        erzeugt.append(schreibe(f"geschichte-{i}.html", baue_geschichte(i, g)))
    print(f"{len(erzeugt)} Dateien erzeugt:")
    for p in erzeugt:
        print("  -", os.path.basename(p))


if __name__ == "__main__":
    main()
