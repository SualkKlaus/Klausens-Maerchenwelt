/* Nacht-Animation: blinkende Sterne, Sternschnuppen, vorbeifliegender Rabe mit Krächzen, Feuerfunken.
   Rein dekorativ. */
(function () {
  "use strict";

  var canvas = document.getElementById("nacht-canvas");
  if (!canvas) return;

  var ctx = canvas.getContext("2d");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var W = 0, H = 0, dpr = window.devicePixelRatio || 1;

  function resize() {
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.width = W + "px";
    canvas.style.height = H + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  window.addEventListener("resize", resize);
  resize();

  // -------- Sterne --------
  var sterne = [];
  var anzahlSterne = reduce ? 60 : 200;
  for (var i = 0; i < anzahlSterne; i++) {
    sterne.push({
      x: Math.random() * W,
      y: Math.random() * H * 0.7,
      r: Math.random() * 1.4 + 0.3,
      phase: Math.random() * Math.PI * 2,
      geschw: Math.random() * 0.02 + 0.008,
      helligkeit: Math.random() * 0.5 + 0.5
    });
  }

  // -------- Sternschnuppen --------
  var schnuppen = [];
  function erzeugeSchnuppe() {
    if (reduce) return;
    schnuppen.push({
      x: Math.random() * W * 0.7,
      y: Math.random() * H * 0.3,
      vx: Math.random() * 6 + 4,
      vy: Math.random() * 3 + 2,
      leben: 1.0,
      laenge: Math.random() * 80 + 60
    });
  }

  // -------- Raben --------
  var raben = [];
  var rabeTimer = 0;
  var rabeIntervall = 3; // Sekunden – häufiger

  function erzeugeRaben() {
    var vonLinks = Math.random() > 0.5;
    var y = Math.random() * H * 0.35 + H * 0.05;
    raben.push({
      x: vonLinks ? -60 : W + 60,
      y: y,
      startY: y,
      vx: (vonLinks ? 1 : -1) * (Math.random() * 1.2 + 0.8),
      fluegelPhase: 0,
      fluegelGeschw: Math.random() * 0.15 + 0.12,
      groesse: Math.random() * 0.4 + 0.7,
      krachezTimer: Math.random() * 2 + 1,
      gekraechzt: false,
      alpha: 0
    });
  }

  // -------- Feuerfunken (am unteren Rand, wie Lagerfeuer-Glimmer) --------
  var funken = [];
  function erzeugeFunke() {
    if (reduce) return;
    funken.push({
      x: Math.random() * W,
      y: H * 0.82 + Math.random() * H * 0.12,
      vx: (Math.random() - 0.5) * 0.5,
      vy: -Math.random() * 1.2 - 0.4,
      leben: 1.0,
      r: Math.random() * 2 + 1
    });
  }

  // -------- Audio (Krächzen via WebAudio) --------
  var audioCtx = null;
  function kraechzen() {
    if (reduce) return;
    try {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      var now = audioCtx.currentTime;
      // Krächzen: absteigender Ton mit Rauigkeit
      var osc1 = audioCtx.createOscillator();
      var osc2 = audioCtx.createOscillator();
      var gain = audioCtx.createGain();
      var filter = audioCtx.createBiquadFilter();

      osc1.type = "sawtooth";
      osc2.type = "square";
      osc1.frequency.setValueAtTime(900, now);
      osc1.frequency.exponentialRampToValueAtTime(300, now + 0.18);
      osc1.frequency.exponentialRampToValueAtTime(450, now + 0.3);
      osc1.frequency.exponentialRampToValueAtTime(200, now + 0.45);
      osc2.frequency.setValueAtTime(450, now);
      osc2.frequency.exponentialRampToValueAtTime(150, now + 0.45);

      filter.type = "bandpass";
      filter.frequency.value = 600;
      filter.Q.value = 3;

      gain.gain.setValueAtTime(0, now);
      gain.gain.linearRampToValueAtTime(0.08, now + 0.03);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);

      osc1.connect(filter);
      osc2.connect(filter);
      filter.connect(gain);
      gain.connect(audioCtx.destination);

      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + 0.5);
      osc2.stop(now + 0.5);
    } catch (e) { /* Audio nicht verfügbar */ }
  }

  // -------- Animation --------
  var lastT = performance.now();

  function draw(now) {
    var dt = Math.min((now - lastT) / 1000, 0.05);
    lastT = now;

    ctx.clearRect(0, 0, W, H);

    // Sterne
    for (var i = 0; i < sterne.length; i++) {
      var s = sterne[i];
      s.phase += s.geschw;
      var tw = 0.5 + 0.5 * Math.sin(s.phase);
      var alpha = s.helligkeit * (0.3 + 0.7 * tw);
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255, 247, 214, " + alpha + ")";
      ctx.fill();
      // Glanz bei großen Sternen
      if (s.r > 1.0 && tw > 0.7) {
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r * 3, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(255, 247, 214, " + (alpha * 0.15) + ")";
        ctx.fill();
      }
    }

    // Sternschnuppen
    if (!reduce && Math.random() < 0.003) erzeugeSchnuppe();
    for (var j = schnuppen.length - 1; j >= 0; j--) {
      var sp = schnuppen[j];
      sp.x += sp.vx;
      sp.y += sp.vy;
      sp.leben -= 0.015;
      if (sp.leben <= 0 || sp.x > W || sp.y > H) {
        schnuppen.splice(j, 1);
        continue;
      }
      var grad = ctx.createLinearGradient(sp.x, sp.y, sp.x - sp.vx * 8, sp.y - sp.vy * 8);
      grad.addColorStop(0, "rgba(255,255,255," + sp.leben + ")");
      grad.addColorStop(1, "rgba(255,247,214,0)");
      ctx.strokeStyle = grad;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(sp.x, sp.y);
      ctx.lineTo(sp.x - sp.vx * 8, sp.y - sp.vy * 8);
      ctx.stroke();
    }

    // Raben
    rabeTimer += dt;
    if (rabeTimer > rabeIntervall && raben.length < 3 && !reduce) {
      rabeTimer = 0;
      rabeIntervall = Math.random() * 4 + 2; // alle 2-6 Sekunden
      erzeugeRaben();
    }
    for (var k = raben.length - 1; k >= 0; k--) {
      var rb = raben[k];
      rb.x += rb.vx;
      // Leichtes Auf-Ab-Wippen
      rb.y = rb.startY + Math.sin(now * 0.003) * 12;
      rb.fluegelPhase += rb.fluegelGeschw;
      // Einblenden
      if (rb.alpha < 1) rb.alpha = Math.min(1, rb.alpha + dt * 1.5);

      // Krächzen
      rb.krachezTimer -= dt;
      if (rb.krachezTimer <= 0 && !rb.gekraechzt && rb.x > 0 && rb.x < W) {
        rb.gekraechzt = true;
        kraechzen();
      }

      // Rabe zeichnen
      drawRabe(rb.x, rb.y, rb.fluegelPhase, rb.groesse, rb.alpha);

      // Entfernen wenn außerhalb
      if (rb.x < -100 || rb.x > W + 100) {
        raben.splice(k, 1);
      }
    }

    // Feuerfunken
    if (!reduce && Math.random() < 0.15) erzeugeFunke();
    for (var f = funken.length - 1; f >= 0; f--) {
      var fk = funken[f];
      fk.x += fk.vx;
      fk.y += fk.vy;
      fk.vy *= 0.99;
      fk.leben -= 0.012;
      if (fk.leben <= 0) {
        funken.splice(f, 1);
        continue;
      }
      ctx.beginPath();
      ctx.arc(fk.x, fk.y, fk.r * fk.leben, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255, 160, 60, " + fk.leben + ")";
      ctx.fill();
      // Glühen
      ctx.beginPath();
      ctx.arc(fk.x, fk.y, fk.r * fk.leben * 3, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255, 160, 60, " + (fk.leben * 0.1) + ")";
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  function drawRabe(x, y, fluegelPhase, skal, alpha) {
    var fluegel = Math.sin(fluegelPhase); // -1..1
    var spanne = 22 * skal;
    var tiefe = 14 * skal * Math.abs(fluegel);

    ctx.save();
    ctx.translate(x, y);
    ctx.globalAlpha = alpha;
    ctx.fillStyle = "#0a0a0f";

    // Körper (kleiner Ellipsenfleck)
    ctx.beginPath();
    ctx.ellipse(0, 0, 6 * skal, 4 * skal, 0, 0, Math.PI * 2);
    ctx.fill();

    // Kopf
    ctx.beginPath();
    ctx.arc(spanne * 0.3 * Math.sign(1), -2 * skal, 3.5 * skal, 0, Math.PI * 2);
    ctx.fill();

    // Schnabel
    ctx.strokeStyle = "#1a1208";
    ctx.lineWidth = 1.5 * skal;
    ctx.beginPath();
    ctx.moveTo(spanne * 0.3, -2 * skal);
    ctx.lineTo(spanne * 0.3 + 5 * skal, -1 * skal);
    ctx.stroke();

    // Flügel (obere Kurve, schlägt auf/ab)
    ctx.strokeStyle = "#0a0a0f";
    ctx.lineWidth = 3 * skal;
    ctx.lineCap = "round";
    // linker Flügel
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.quadraticCurveTo(-spanne * 0.5, -tiefe, -spanne, -tiefe * 0.3);
    ctx.stroke();
    // rechter Flügel
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.quadraticCurveTo(spanne * 0.5, -tiefe, spanne, -tiefe * 0.3);
    ctx.stroke();

    // Schweif
    ctx.beginPath();
    ctx.moveTo(-3 * skal, 0);
    ctx.lineTo(-8 * skal, 3 * skal);
    ctx.lineTo(-6 * skal, 0);
    ctx.closePath();
    ctx.fill();

    ctx.restore();
  }

  // Maus-Interaktion: bei Klick Sterne aufleuchten lassen
  window.addEventListener("click", function (e) {
    if (reduce) return;
    for (var i = 0; i < sterne.length; i++) {
      var s = sterne[i];
      var d = Math.hypot(s.x - e.clientX, s.y - e.clientY);
      if (d < 150) {
        s.phase = 0; // sofort hell
        s.helligkeit = 1;
      }
    }
  });

  requestAnimationFrame(draw);
})();
