/* Erzeugt den animierten Sternenhimmel.
   Rein dekorativ – der Inhalt der Seite funktioniert auch ohne dieses Skript. */
(function () {
  "use strict";

  var container = document.getElementById("sterne");
  if (!container) return;

  // Bewegung reduzieren? Dann weniger / keine Animation.
  var reduce = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var anzahl = reduce ? 80 : 170;
  var frag = document.createDocumentFragment();

  for (var i = 0; i < anzahl; i++) {
    var s = document.createElement("span");
    s.className = "stern";
    var groesse = (Math.random() * 2.2 + 0.6).toFixed(2);
    s.style.width = groesse + "px";
    s.style.height = groesse + "px";
    s.style.left = (Math.random() * 100).toFixed(2) + "%";
    s.style.top = (Math.random() * 100).toFixed(2) + "%";
    s.style.setProperty("--dur", (Math.random() * 4 + 2.5).toFixed(2) + "s");
    s.style.setProperty("--delay", (Math.random() * 5).toFixed(2) + "s");
    frag.appendChild(s);
  }

  // Ein paar Sternschnuppen
  if (!reduce) {
    for (var j = 0; j < 3; j++) {
      var sch = document.createElement("span");
      sch.className = "sternschnuppe";
      sch.style.left = (Math.random() * 60).toFixed(2) + "%";
      sch.style.top = (Math.random() * 40).toFixed(2) + "%";
      sch.style.setProperty("--sdur", (Math.random() * 5 + 6).toFixed(2) + "s");
      sch.style.setProperty("--sdelay", (Math.random() * 12 + j * 4).toFixed(2) + "s");
      frag.appendChild(sch);
    }
  }

  container.appendChild(frag);
})();
