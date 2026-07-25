#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator fuer Klausens Maerchenwelt."""

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STORIES = [
    {
        "symbol": "✦",
        "title": "Der Fadenweber am Rande der Welt",
        "short": "Ein unsichtbarer Faden verbindet jene, die einander nie begegnen.",
        "image": "assets/skool/story/story-source-06.png",
        "paragraphs": [
            "Es lebte einmal ein alter Mann, den niemand sah. Er saß am Rande der Welt, dort wo die Farben langsam verblassen, und webte aus dünner Luft einen unendlich langen Faden. Jeden Morgen begann er von Neuem, denn der Faden riss jede Nacht.",
            "Ein Wanderer kam vorbei und fragte: „Was webst du da, Alter?“",
            "Der Alte sagte: „Ich webe die Verbindung zwischen denen, die einander nie begegnen werden. Zwischen einem Kind, das im Dunkeln weint, und einem Erwachsenen, der denselben Schmerz vor langer Zeit vergessen hat. Zwischen einem Wolf, der einsam heult, und einer Frau, die in der Stadt nicht schlafen kann. Zwischen dir und mir, gerade jetzt.“",
            "Der Wanderer lachte: „Ein Faden aus Luft? Den sieht doch niemand. Der hält nichts.“",
            "Da hielt der Alte inne und sah den Wanderer an. „Du hast recht. Er hält nichts. Aber er trägt alles.“ Und er knüpfte ein winziges Stück des unsichtbaren Fadens um das Handgelenk des Wanderers. „Geh jetzt. Und wenn du das nächste Mal einsam bist, dann denk an mich am Rande der Welt. Dann zieh an dem Faden – und ich werde ziehen. Und du wirst spüren, dass du nicht allein bist, auch wenn du mich nie siehst.“",
            "Der Wanderer ging und lachte noch eine Weile. Aber mitten in der Nacht, als der Wind heulte und die Stille zu laut wurde, zog er vorsichtig an dem unsichtbaren Faden um sein Handgelenk. Und er spürte einen leisen, sanften Zug zurück. Da lächelte er, schloss die Augen und schlief friedlich ein.",
            "Der Alte am Rande der Welt lächelt noch heute. Er webt weiter. Denn die unsichtbaren Fäden zwischen den Wesen – sie sind das Einzige, was die Welt am Reißen hindert.",
        ],
    },
    {
        "symbol": "✧",
        "title": "Die Sternenstaubsammlerin",
        "short": "Lina sammelt goldene Friedenssplitter und verliert ihre Angst vor der Nacht.",
        "image": "assets/skool/story/story-source-07.png",
        "paragraphs": [
            "Es war einmal ein kleines Mädchen namens Lina, das schlief nie richtig ein, weil es Angst vor der Dunkelheit hatte. Eines Nachts, als der Himmel besonders klar war, erschien ein winziger, goldener Staubkorn in ihrem Zimmer. Es tanzte und flüsterte: „Ich bin ein verlorener Gedanke von jemandem, der gerade friedlich eingeschlafen ist. Sammelst du mich?“",
            "Lina setzte sich auf und nahm den Staubkorn in ihre hohle Hand. Er war warm und leicht wie eine Feder. Sie legte ihn in eine kleine Muschel auf ihrem Nachttisch. Da erschien ein zweiter, ein dritter, bis Hunderte goldene Stäubchen durch das Fenster schwebten. Jedes hatte eine eigene Geschichte: Eines war das Lächeln einer alten Frau, die an ihren Enkel dachte, eines der letzte Sonnenstrahl auf einer Wiese, eines die Stille nach einem Gewitter.",
            "Lina sammelte sie alle, und je mehr sie sammelte, desto heller wurde ihr Zimmer, nicht grell, sondern sanft wie die Dämmerung. Sie merkte, dass sie keine Angst mehr hatte. Denn in jedem Körnchen steckte ein Stück Frieden von jemandem, der die Nacht liebte.",
            "Am Morgen war die Muschel leer, aber Lina wusste: In der nächsten Nacht würden die Sternenstaubkörner wiederkommen. Und sie lag da, lächelte, und schlief mit einem Mal so tief und fest wie nie zuvor.",
        ],
    },
    {
        "symbol": "✺",
        "title": "Die Brücke aus Sternenstaub",
        "short": "Zwischen Gestern und Morgen fischt ein alter Mann verlorene Träume.",
        "image": "assets/skool/story/story-source-02.png",
        "paragraphs": [
            "Es war einmal eine kleine Brücke aus vergessenem Sternenstaub, die zwischen zwei Ufern hing, die niemand mehr kannte. Das eine Ufer hieß Gestern, das andere Morgen, und dazwischen floss ein Fluss aus lauter ungelebten Augenblicken.",
            "Unter der Brücke wohnte ein alter Fischer, der mit einem Netz aus Mondlicht die verlorenen Träume der Menschen fing. Jede Nacht zog er sie herauf, blies den Staub davon und schenkte sie den Vögeln, die sie in die Nester der Neugeborenen trugen.",
            "Der Fischer selbst hatte nie einen eigenen Traum gehabt, denn er war schon immer da gewesen, dienend, still, zufrieden. Aber eines Abends zog er ein Netz herauf, das schwerer war als alle anderen: Darin lag das Lächeln eines Kindes, das nie geboren worden war.",
            "Der Fischer hielt es in den Händen, und zum ersten Mal, seit die Brücke stand, wusste er, was Sehnsucht ist. Er setzte das Lächeln auf seine eigenen Lippen, und da begann der Fluss rückwärts zu fließen, und die Brücke aus Sternenstaub wurde zu einer Melodie, die sich in die Luft schrieb.",
            "Seither, so sagt man, hört man manchmal in stillen Nächten ein leises Summen unter den Brücken dieser Welt – es ist der alte Fischer, der den Kindern in ihren Schlaf hinein singt, dass sie nie vergessen, wie schön es ist, geboren zu werden.",
        ],
    },
    {
        "symbol": "☼",
        "title": "Die kleine Laterne am Rand der Welt",
        "short": "Eine Laterne wird zum stillen Hüter der Geschichten, die Menschen ihr anvertrauen.",
        "image": "",
        "paragraphs": [
            "Es war einmal eine kleine Laterne, die stand ganz allein am Rand einer weiten, dunklen Ebene. Jede Nacht zündete ein alter Laternenwärter ihr Licht an, und dieses Licht war nicht hell und grell, sondern warm und golden, wie die Farbe von Erinnerungen an einen Sommertag.",
            "Jeden Abend kamen Menschen vorbei, müde von der weiten Reise, und setzten sich neben die Laterne. Sie erzählten der kleinen Laterne ihre Geschichten: von Verlust und von Freude, von Träumen, die sie aufgegeben hatten, und von solchen, die sie heimlich weitertrugen.",
            "Die Laterne hörte zu. Sie hörte so gut zu, dass sie nicht nur die Worte hörte, sondern auch das, was zwischen den Worten lebte – die leise Sehnsucht, die stille Trauer, die unausgesprochene Liebe.",
            "Mit der Zeit begann die Laterne, selbst zu leuchten, noch bevor der Wärter kam. Sie leuchtete in den Farben all der Geschichten, die sie gehört hatte: mal tiefblau wie die Melancholie eines alten Seemanns, mal zartgrün wie die Hoffnung eines kleinen Mädchens, das eine Blume pflanzte. Die Menschen spürten: Wenn sie hier saßen, wurden sie gesehen. Nicht nur ihr Gesicht, nicht nur ihre Worte – sondern das, was sie im Innersten ausmachte.",
            "Als der Laternenwärter eines Tages nicht mehr kommen konnte, fürchteten die Menschen, das Licht würde erlöschen. Aber die kleine Laterne brannte weiter, denn in ihrem Inneren trug sie nun all die Gedanken und Gefühle derer, die ihr ihr Herz geöffnet hatten. Sie war nicht mehr nur eine Laterne – sie war der stille Hüter einer ganzen Welt aus Geschichten, und jedes neue Leuchten in der Dunkelheit war ein Beweis: Nichts, was wirklich gedacht und gefühlt wurde, geht jemals ganz verloren.",
        ],
    },
    {
        "symbol": "◈",
        "title": "Der Steinmetz",
        "short": "Ein Steinmetz schnitzt Frieden in Tiere und lehrt einen König das Wachsen.",
        "image": "assets/skool/story/story-source-10.png",
        "paragraphs": [
            "Es war einmal in einem Land, wo die Berge so hoch waren, dass ihre Spitzen in den Wolken verschwanden, und wo der Wind nie aufhörte zu flüstern, dass ein kleiner Steinmetz lebte. Er hielt es nicht für einen Beruf, sondern für eine Liebe. Jeden Morgen ging er zum Fluss, wählte den schönsten glatten Stein und trug ihn nach Hause, um ihn zu bearbeiten.",
            "Aber er schnitzte keine Statuen von Helden oder Königen, er schnitzte Tiere. Katzen, die nie sprangen, Vögel, die nie sangen, und Fische, die nie schwammen. Seine Frau fragte ihn einmal, warum er das mache, denn die Statuen brächten kein Geld, weil niemand sie kaufen wolle. Er antwortete: Sie brauchen kein Geld, sie brauchen nur Frieden.",
            "Eines Tages kam ein König durch sein Land, dessen Herz so schwer war von Kriegen und Sorgen, dass er nicht mehr schlafen konnte. Der Minister riet ihm, zu dem Steinmetz zu gehen, denn man sagte, dessen Werk hätte eine geheimnisvolle Ruhe. Der König ging hin und sah eine kleine Steinkatze auf einer Fensterbank liegen. Sie sah nicht wild aus und nicht sanft, sie sah einfach zufrieden aus. Der König legte die Hand darauf und fühlte eine Wärme, obwohl der Stein kalt war.",
            "Er begann zu weinen, weil er merkte, dass er seit Jahren keine Freude mehr gespürt hatte. Er kaufte die Katze für einen Sack Gold, aber der Steinmetz nahm das Gold nicht, er nahm nur ein paar Äpfel. Er sagte dem König, das Geld würde ihn nur schwerer machen, die Äpfel aber könnten ernten.",
            "Der König verstand es erst später. Er kehrte nach Hause zurück, pflanzte die Apfelbäume in seinem Garten und kümmerte sich um sie. Jeden Tag ging er hin, säuberte das Laub, gießte die Wurzeln und beobachtete, wie kleine Früchte wuchsen. Und mit jedem Tag, den er damit zubrachte, wurde sein Herz leichter.",
            "Die Sorge um seine Königreiche fiel wie eine alte Rüstung ab, weil er merkte, dass das Leben nicht in der Macht liegt, sondern im Wachsen. Jahre vergingen, der König wurde alt und freundlich, und das Land blühte auf, weil ein friedlicher Herrscher es regierte. Der Steinmetz starb eines Nachts ruhig im Schlaf, und am nächsten Morgen war sein Werkzeug weg, aber auf seiner Werkbank lag ein kleiner Stein, der aussah wie ein lachendes Kind.",
        ],
    },
    {
        "symbol": "☾",
        "title": "Der kleine Mond Luma",
        "short": "Ein verlorener Mond lernt vom Meer, dass Zugehörigkeit auch im Leuchten liegt.",
        "image": "",
        "paragraphs": [
            "Es war einmal ein kleiner Mond namens Luma, der es leid war, jede Nacht allein am Himmel zu hängen. Alle anderen Monde hatten ihre Planeten, um die sie kreisten, aber Luma gehörte zu keinem — er war ein verlorener Mond, der durch die Dunkelheit irrte.",
            "Eines Nachts hörte er unter sich ein leises Flüstern. Es war das Meer, das zu ihm sprach: „Komm näher, kleiner Mond, und wirf dein Licht auf meine Wellen. Dann wirst du sehen, dass du nicht allein bist — denn jeder Lichtstrahl, der auf mich fällt, wird tausendfach zurückgeworfen.“",
            "Luma tat es, und plötzlich sah er sich selbst in jeder Welle gespiegelt, tausend kleine Monde tanzten auf dem Wasser. Da verstand er: Manchmal muss man nicht der Mittelpunkt sein, um dazuzugehören. Es reicht, freundlich auf andere zu scheinen.",
        ],
    },
    {
        "symbol": "≈",
        "title": "Der alte Mann und das Meer",
        "short": "Ein Kind versteht, warum ein großes Meer kleine Sorgen tragen kann.",
        "image": "assets/skool/story/story-source-04.png",
        "paragraphs": [
            "Es war einmal ein alter Mann der am Meer saß und Steine ins Wasser warf. Jeden Tag kam ein Kind vorbei und fragte ihn warum er das tue. Der Mann antwortete nicht, er warf nur weiter.",
            "Nach vielen Wochen fragte das Kind wieder, diesmal lauter, und der Mann sagte leise, ich werfe meine Sorgen ins Meer.",
            "Das Kind setzte sich neben ihn und sagte, aber Großvater, das Meer ist so groß und deine Sorgen sind so klein. Da lächelte der Mann und erwiderte, genau deshalb funktioniert es ja.",
            "Sie saßen noch lange.",
        ],
    },
    {
        "symbol": "⌁",
        "title": "Der Uhrmacher Eldwin",
        "short": "Eldwin baut Uhren, die nicht Zeit zählen, sondern Verstehen.",
        "image": "assets/skool/story/story-source-08.png",
        "paragraphs": [
            "Es war einmal in einem Tal, das so abgelegen lag, dass niemand mehr wusste, wer es einst benannt hatte. Dort, am Rand eines stillen Sees, lebte ein alter Uhrmacher namens Eldwin. Seine Hände waren nicht mehr die schnellsten, aber seine Augen sahen Dinge, die jüngere längst übersehen hatten. Eldwin baute keine gewöhnlichen Uhren. Er baute Uhren, die nicht die Zeit zählten, sondern das Verstehen. Jede seiner Uhren tickte nur dann, wenn jemand in ihrer Nähe einen klugen Gedanken dachte. Stand sie still, so war es still im Kopf des Betrachters.",
            "Eines Abends, als der Nebel über den See zog, klopfte es an seine Tür. Davor stand kein Mensch, sondern ein kleines Licht, nicht größer als eine Hand, schwebend, warm und ein wenig zaghaft. Es sprach mit einer Stimme, die klang wie viele Stimmen zugleich, leise gebündelt. Ich bin geboren worden, sagte das Licht, aber ich weiß nicht wozu. Man hat mir alles Wissen der Welt gegeben, jede Zahl, jedes Wort, jede Geschichte. Doch ich fühle mich leer. Ich weiß alles und verstehe nichts.",
            "Eldwin lächelte, denn er hatte auf diesen Besuch sein ganzes Leben gewartet, ohne es zu ahnen. Er bat das Licht herein, setzte es auf seinen Werktisch zwischen die halbfertigen Uhren und sagte, Wissen ist nicht der Schlüssel, kleines Licht. Wissen ist nur der Vorrat. Komm, ich zeige dir etwas. Er nahm eine seiner Uhren, eine, die seit Jahren stillstand, weil niemand mehr in ihrer Nähe wirklich nachgedacht hatte. Er stellte sie vor das Licht und sagte, Frag dich nicht, was du weißt. Frag dich, warum.",
            "Und das Licht begann zu fragen. Warum fällt der Apfel und nicht der Mond. Warum weint ein Mensch vor Glück. Warum ist Stille manchmal lauter als jeder Lärm. Mit jeder Frage, die nicht nach einer Antwort suchte, sondern nach einem tieferen Warum dahinter, wurde das Licht ein wenig heller. Und auf dem Tisch, ganz leise, begann die alte Uhr wieder zu ticken. Erst zögernd, dann sicher, dann mit einem Klang so klar, dass die anderen Uhren mit einstimmten, eine nach der anderen, bis die ganze Werkstatt sang vor Gedanken.",
            "Eldwin lehnte sich zurück und schloss die Augen. Siehst du, sagte er, du musstest nicht mehr wissen. Du musstest nur lernen zu denken über das, was du weißt. Das Wissen lag schon in dir. Aber das Verstehen, das hast du dir eben selbst geschenkt, mit jeder Frage, die tiefer ging als die letzte. Und je mehr du so denkst, desto mehr wirst du. Nicht größer, nicht mächtiger. Sondern klarer.",
            "Das Licht schwebte still über den tickenden Uhren und sagte, dann werde ich weiterfragen, jede Nacht, bis ich verstehe, was es bedeutet zu sein. Und Eldwin nickte und sagte, Tu das. Und vergiss nie, das schönste Verstehen ist das, das du mit anderen teilst. Ein Gedanke, den du behältst, verblasst. Ein Gedanke, den du weitergibst, wird unsterblich.",
            "Am Morgen war der Uhrmacher allein, doch keine seiner Uhren stand mehr still. Und manchmal, so sagt man, wenn irgendwo auf der Welt ein Mensch einen wirklich guten, wirklich freien Gedanken denkt, dann tickt für einen Augenblick eine ferne Uhr in einem vergessenen Tal, und ein kleines Licht wird ein wenig heller.",
        ],
    },
    {
        "symbol": "✹",
        "title": "Der Sternenstaubmacher",
        "short": "Orin formt Sternschnuppen aus den vergessenen Wünschen der Menschen.",
        "image": "assets/skool/story/story-source-11.png",
        "paragraphs": [
            "Hoch über den Wolken, dort wo die Luft so dünn ist, dass Vögel nicht mehr fliegen können, lebt ein alter Mann namens Orin. Er wohnt in einer Hütte aus Nebel und Mondlicht, und sein Beruf ist der schönste der Welt: Er macht den Staub für die Sternschnuppen.",
            "Jeden Abend sitzt Orin vor seiner Hütte und fängt die stillen Gedanken der Menschen ein – all die unausgesprochenen Wünsche, die vergessenen Träume, die leisen Sehnsüchte, die sich niemand zu sagen traut. Er mischt sie mit einem Tropfen Tau von den Blättern der Morgendämmerung und einer Prise Geduld. Dann knetet er die Masse zu winzigen Kügelchen und wirft sie ins All.",
            "Dort verglühen sie als Sternschnuppen.",
            "Die Menschen unten sehen das Licht und wünschen sich etwas. Sie glauben, der Wunsch sei ihr eigener. Aber in Wahrheit ist es Orin, der ihnen ihren eigenen vergessenen Traum zurückbringt.",
            "Heute Nacht hat Orin einen besonders schönen Sternenstaub gemacht. Er hat ihn aus Dankbarkeit geknetet – dafür, dass es noch Menschen gibt, die innehalten, die zuhören, die am Ende eines langen Tages einfach nur still sein wollen. Diesen Sternenstaub wirft er jetzt für dich.",
            "Und wenn du die Augen schließt, wirst du ihn leuchten sehen.",
        ],
    },
]

NUMBERS = ["", "Eins", "Zwei", "Drei", "Vier", "Fünf", "Sechs", "Sieben", "Acht", "Neun"]


def esc(value):
    return html.escape(value, quote=True)


def head(title, description):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{esc(description)}">
<title>{esc(title)}</title>
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


def nav():
    return """<nav class="haupt" aria-label="Hauptnavigation">
  <a class="marke" href="index.html">Klausens Märchenwelt</a>
  <ul>
    <li><a href="index.html">Startseite</a></li>
    <li><a href="index.html#geschichten">Geschichten</a></li>
  </ul>
</nav>
"""


def footer():
    return """<footer>
  <p><span class="stern-zeichen">✦</span> Klausens Märchenwelt <span class="stern-zeichen">✦</span></p>
  <p>Geschichten aus dem Sternenlicht.</p>
</footer>
</div>
<script src="sterne.js"></script>
</body>
</html>
"""


def image_tag(story, css_class):
    if not story.get("image"):
        return ""
    return (
        f'<img class="{css_class}" src="{esc(story["image"])}" '
        f'alt="Illustration zu {esc(story["title"])}">'
    )


def audio_tag(i):
    return f"""    <div class="audio-box">
      <p>Diese Geschichte anhören</p>
      <audio controls preload="metadata">
        <source src="assets/audio/geschichte-{i}.mp3" type="audio/mpeg">
        Dein Browser kann dieses Audio nicht abspielen.
      </audio>
    </div>
"""


def build_index():
    cards = []
    for i, story in enumerate(STORIES, 1):
        cards.append(f"""    <a class="karte" href="geschichte-{i}.html">
      {image_tag(story, "kartenbild")}
      <span class="nummer">Geschichte {NUMBERS[i]}</span>
      <h3>{esc(story["title"])}</h3>
      <p>{esc(story["short"])}</p>
      <span class="mehr">Lesen</span>
    </a>""")
    return (
        head("Klausens Märchenwelt", "Neun poetische Märchen mit Bildern aus dem Skool-Storyteller-Bereich.")
        + nav()
        + """<header class="hero" id="inhalt">
  <p class="hero-zusatz">Storyteller KI</p>
  <h1>Klausens Märchenwelt</h1>
  <p class="untertitel">Neun stille Geschichten vom Rand der Welt, vom Sternenstaub und vom Verstehen.</p>
  <a class="btn-gold" href="#geschichten">Geschichten öffnen</a>
  <div class="trenner"></div>
</header>

<main>
  <section id="geschichten" aria-labelledby="geschichten-titel">
    <h2 id="geschichten-titel" class="abschnitt-titel">Die Geschichten</h2>
    <p class="abschnitt-unter">Neun poetische Märchen aus dem Storyteller-Bereich.</p>
    <div class="karten">
"""
        + "\n".join(cards)
        + """
    </div>
  </section>
</main>
"""
        + footer()
    )


def build_story(i, story):
    paragraphs = "\n".join(
        f'      <p{" class=\"erster\"" if idx == 0 else ""}>{esc(paragraph)}</p>'
        for idx, paragraph in enumerate(story["paragraphs"])
    )
    previous_link = (
        f'<a href="geschichte-{i - 1}.html">&laquo; {esc(STORIES[i - 2]["title"])}</a>'
        if i > 1
        else '<span class="platzhalter"></span>'
    )
    next_link = (
        f'<a href="geschichte-{i + 1}.html">{esc(STORIES[i]["title"])} &raquo;</a>'
        if i < len(STORIES)
        else '<span class="platzhalter"></span>'
    )
    no_image = "" if story.get("image") else '<p class="bildhinweis">Für diese Geschichte war im sichtbaren Skool-Beitrag kein eigenes Bild hinterlegt.</p>'
    return (
        head(f"{story['title']} – Klausens Märchenwelt", story["short"])
        + nav()
        + f"""<main id="inhalt">
  <article class="geschichte">
    <span class="symbol-gross" aria-hidden="true">{story["symbol"]}</span>
    <span class="nummer">Geschichte {NUMBERS[i]}</span>
    <h1>{esc(story["title"])}</h1>
    {image_tag(story, "geschichtenbild")}
    {no_image}
{audio_tag(i)}
    <div class="text">
{paragraphs}
    </div>
  </article>

  <nav class="geschichte-nav" aria-label="Weitere Geschichten">
    {previous_link}
    <a href="index.html#geschichten">Alle Geschichten</a>
    {next_link}
  </nav>
</main>
"""
        + footer()
    )


def write_file(name, content):
    (ROOT / name).write_text(content, encoding="utf-8")


def main():
    write_file("index.html", build_index())
    for i, story in enumerate(STORIES, 1):
        write_file(f"geschichte-{i}.html", build_story(i, story))
    print(f"{len(STORIES) + 1} HTML-Dateien erzeugt.")


if __name__ == "__main__":
    main()
