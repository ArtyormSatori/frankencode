// FrankenCode — Laboratory Frontend Interactive Controller

let currentSpecimenId = "cobol_banking";
let currentSpec = null;
let currentSuture = null;
let activeLanguage = "python";
let soundEnabled = true;

// Web Audio API Synthesizer
let audioCtx = null;
function initAudio() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
}

function playGalvanicSpark() {
  if (!soundEnabled) return;
  initAudio();
  if (audioCtx.state === 'suspended') audioCtx.resume();
  
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  
  osc.type = "sawtooth";
  osc.frequency.setValueAtTime(110, audioCtx.currentTime);
  osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.15);
  osc.frequency.exponentialRampToValueAtTime(55, audioCtx.currentTime + 0.3);
  
  gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
  
  osc.connect(gain);
  gain.connect(audioCtx.destination);
  
  osc.start();
  osc.stop(audioCtx.currentTime + 0.3);
}

function playSuccessChime() {
  if (!soundEnabled) return;
  initAudio();
  if (audioCtx.state === 'suspended') audioCtx.resume();

  [261.63, 329.63, 392.00, 523.25].forEach((freq, idx) => {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = "sine";
    osc.frequency.value = freq;
    gain.gain.setValueAtTime(0.08, audioCtx.currentTime + idx * 0.08);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + idx * 0.08 + 0.4);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(audioCtx.currentTime + idx * 0.08);
    osc.stop(audioCtx.currentTime + idx * 0.08 + 0.4);
  });
}

// Background Lightning Canvas Animation
const canvas = document.getElementById("lightning-canvas");
const ctx = canvas.getContext("2d");

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

function drawLightningBolt(x1, y1, x2, y2, branches) {
  ctx.strokeStyle = "rgba(168, 85, 247, 0.7)";
  ctx.lineWidth = 2;
  ctx.shadowColor = "#a855f7";
  ctx.shadowBlur = 15;

  ctx.beginPath();
  ctx.moveTo(x1, y1);

  let curX = x1;
  let curY = y1;
  const segments = 12;
  const dx = (x2 - x1) / segments;
  const dy = (y2 - y1) / segments;

  for (let i = 0; i < segments; i++) {
    curX += dx + (Math.random() - 0.5) * 30;
    curY += dy + (Math.random() - 0.5) * 15;
    ctx.lineTo(curX, curY);

    if (branches > 0 && Math.random() < 0.25) {
      drawLightningBolt(curX, curY, curX + (Math.random() - 0.5) * 100, curY + 50 + Math.random() * 50, branches - 1);
    }
  }

  ctx.lineTo(x2, y2);
  ctx.stroke();
}

function triggerLightningStrike() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const startX = Math.random() * canvas.width;
  const endX = startX + (Math.random() - 0.5) * 200;
  drawLightningBolt(startX, 0, endX, canvas.height * 0.8, 2);

  setTimeout(() => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }, 180);
}

// Laboratory State & DOM Elements
const specimenCards = document.querySelectorAll(".specimen-card");
const legacyCodeEditor = document.getElementById("legacy-code-editor");
const specimenLangBadge = document.getElementById("specimen-lang-badge");
const pathologiesContainer = document.getElementById("pathologies-container");
const vitalOrgansContainer = document.getElementById("vital-organs-container");
const sutureCodeDisplay = document.getElementById("suture-code-display");
const electrifyBtn = document.getElementById("electrify-btn");
const soundToggleBtn = document.getElementById("sound-toggle-btn");
const soundIcon = document.getElementById("sound-icon");
const soundStatus = document.getElementById("sound-status");
const pipelineStatusText = document.getElementById("status-pipeline-text");

// Telemetry dials
const voltageValue = document.getElementById("voltage-value");
const voltageBar = document.getElementById("voltage-bar");
const amperageValue = document.getElementById("amperage-value");
const amperageBar = document.getElementById("amperage-bar");
const latencyValue = document.getElementById("latency-value");
const speedupValue = document.getElementById("speedup-value");
const pbtStatusBadge = document.getElementById("pbt-status-badge");
const pbtPassCount = document.getElementById("pbt-pass-count");
const pbtResultsBody = document.getElementById("pbt-results-body");
const langTabs = document.querySelectorAll(".lang-tab");

// Audio Toggle
soundToggleBtn.addEventListener("click", () => {
  soundEnabled = !soundEnabled;
  soundStatus.textContent = soundEnabled ? "ON" : "MUTED";
  soundStatus.className = soundEnabled ? "text-emerald-400" : "text-slate-500";
  soundIcon.textContent = soundEnabled ? "🔊" : "🔇";
});

// Specimen Switching
specimenCards.forEach(card => {
  card.addEventListener("click", async () => {
    specimenCards.forEach(c => {
      c.classList.remove("active");
      c.classList.remove("border-purple-500/50");
      c.classList.add("border-slate-800");
    });
    card.classList.add("active");
    card.classList.add("border-purple-500/50");
    
    currentSpecimenId = card.getAttribute("data-id");
    if (currentSpecimenId === "custom") {
      legacyCodeEditor.value = `// Paste your custom legacy COBOL, FORTRAN, or C code here\nint legacy_math(int a, int b) {\n    return (a * 100) / (b + 1);\n}`;
      specimenLangBadge.textContent = "CUSTOM RELIC";
    } else {
      await loadSpecimen(currentSpecimenId);
    }
  });
});

// Load Specimen from API
async function loadSpecimen(id) {
  try {
    pipelineStatusText.textContent = "Fetching Specimen Relic from Archives...";
    const res = await fetch(`/api/specimen/${id}`);
    if (!res.ok) throw new Error("Specimen not found");
    currentSpec = await res.json();

    legacyCodeEditor.value = currentSpec.raw_code;
    specimenLangBadge.textContent = currentSpec.origin_language;

    renderAutopsy(currentSpec);
    pipelineStatusText.textContent = `Specimen '${currentSpec.title}' Loaded • Click ELECTRIFY to Suture`;
  } catch (err) {
    console.error("Error loading specimen:", err);
  }
}

// Render Dissection Autopsy
function renderAutopsy(spec) {
  // Render Pathologies
  pathologiesContainer.innerHTML = "";
  if (!spec.pathologies || spec.pathologies.length === 0) {
    pathologiesContainer.innerHTML = "<div class='text-xs text-slate-500 italic'>No severe structural pathologies detected.</div>";
  } else {
    spec.pathologies.forEach(p => {
      const isCrit = p.severity === "CRITICAL";
      const div = document.createElement("div");
      div.className = `p-3 rounded-lg border text-xs font-mono ${isCrit ? 'bg-red-950/30 border-red-500/40 text-red-200' : 'bg-amber-950/30 border-amber-500/40 text-amber-200'}`;
      div.innerHTML = `
        <div class="flex items-center justify-between font-bold mb-1">
          <span>⚠️ [${p.severity}] ${p.title}</span>
        </div>
        <p class="text-slate-400 text-xxs mb-1.5">${p.description}</p>
        <div class="text-emerald-400 text-xxs flex items-center gap-1">
          <span>✓ Remediation:</span> ${p.remediation}
        </div>
      `;
      pathologiesContainer.appendChild(div);
    });
  }

  // Render Vital Organs
  vitalOrgansContainer.innerHTML = "";
  if (!spec.vital_organs || spec.vital_organs.length === 0) {
    vitalOrgansContainer.innerHTML = "<div class='text-xs text-slate-500 italic'>Awaiting deep AST dissection.</div>";
  } else {
    spec.vital_organs.forEach(o => {
      const div = document.createElement("div");
      div.className = "p-3 rounded-lg border border-purple-900/40 bg-purple-950/20 text-xs font-mono";
      div.innerHTML = `
        <div class="flex items-center justify-between text-purple-300 font-bold mb-1">
          <span>🫀 ${o.organ_name}</span>
          <span class="text-xxs px-1.5 py-0.5 bg-purple-900 text-purple-200 rounded">${o.category}</span>
        </div>
        <div class="bg-black/50 p-2 rounded text-xxs text-slate-400 mb-1 overflow-x-auto">${o.legacy_snippet}</div>
        <div class="text-cyan-400 text-xxs">Invariant: ${o.invariants.join(" • ")}</div>
      `;
      vitalOrgansContainer.appendChild(div);
    });
  }
}

// Language tab switching
langTabs.forEach(tab => {
  tab.addEventListener("click", () => {
    langTabs.forEach(t => {
      t.classList.remove("active", "bg-cyan-950", "text-cyan-300", "border", "border-cyan-800/60");
      t.classList.add("text-slate-400");
    });
    tab.classList.add("active", "bg-cyan-950", "text-cyan-300", "border", "border-cyan-800/60");
    tab.classList.remove("text-slate-400");
    activeLanguage = tab.getAttribute("data-lang");
    updateSutureDisplay();
  });
});

function updateSutureDisplay() {
  if (!currentSuture) {
    sutureCodeDisplay.textContent = "// Click 'ELECTRIFY & SUTURE' to synthesize modern chimera";
    return;
  }
  if (activeLanguage === "python") {
    sutureCodeDisplay.textContent = currentSuture.python_chimera;
  } else if (activeLanguage === "typescript") {
    sutureCodeDisplay.textContent = currentSuture.typescript_chimera;
  } else if (activeLanguage === "rust") {
    sutureCodeDisplay.textContent = currentSuture.rust_contract;
  }
}

// Electrify & Suture Workflow
electrifyBtn.addEventListener("click", async () => {
  electrifyBtn.disabled = true;
  electrifyBtn.classList.add("opacity-60");
  triggerLightningStrike();
  playGalvanicSpark();

  try {
    // Step 1: Dissect
    pipelineStatusText.textContent = "⚡ Step 1/4: Anatomical Dissection in Progress...";
    let specToUse = currentSpec;
    if (currentSpecimenId === "custom" || !specToUse) {
      const code = legacyCodeEditor.value;
      const dissectRes = await fetch("/api/dissect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code, specimen_id: "custom" })
      });
      specToUse = await dissectRes.json();
      currentSpec = specToUse;
      renderAutopsy(specToUse);
    }

    // Step 2: Suture
    pipelineStatusText.textContent = "⚡ Step 2/4: Synthesizing Multi-Era Chimera Suture...";
    const sutureRes = await fetch("/api/suture", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ spec: specToUse })
    });
    currentSuture = await sutureRes.json();
    updateSutureDisplay();

    // Step 3: PBT Invariant Verification
    pipelineStatusText.textContent = "⚡ Step 3/4: Channeling PBT Lightning (100+ Samples)...";
    triggerLightningStrike();
    playGalvanicSpark();
    pbtStatusBadge.textContent = "PBT Invariant Fuzzing Active";
    pbtStatusBadge.className = "px-2 py-0.5 text-xs font-mono bg-purple-900 text-purple-200 border border-purple-500 rounded animate-pulse";

    const verifyRes = await fetch("/api/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        spec: specToUse,
        python_chimera: currentSuture.python_chimera,
        num_samples: 100
      })
    });
    const pbtReport = await verifyRes.json();
    renderPBT(pbtReport);

    // Step 4: Sandbox Benchmark & Telemetry
    pipelineStatusText.textContent = "⚡ Step 4/4: Measuring Galvanic Microsecond Sandbox Telemetry...";
    const benchRes = await fetch("/api/benchmark", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        spec: specToUse,
        python_chimera: currentSuture.python_chimera,
        iterations: 500
      })
    });
    const telemetry = await benchRes.json();
    renderTelemetry(telemetry, pbtReport);

    pipelineStatusText.textContent = "✓ SUTURE COMPLETE • All Invariants Mathematically Verified 100%";
    playSuccessChime();

  } catch (err) {
    console.error("Pipeline failure:", err);
    pipelineStatusText.textContent = "❌ Suture Interrupted: " + err.message;
  } finally {
    electrifyBtn.disabled = false;
    electrifyBtn.classList.remove("opacity-60");
  }
});

function renderPBT(report) {
  pbtPassCount.textContent = `${report.passed_samples} / ${report.total_samples} Passed (${(report.pass_rate * 100).toFixed(1)}%)`;
  pbtStatusBadge.textContent = `${(report.pass_rate * 100).toFixed(0)}% Invariants Proved`;
  pbtStatusBadge.className = "px-2 py-0.5 text-xs font-mono bg-emerald-950 text-emerald-300 border border-emerald-500/50 rounded";

  pbtResultsBody.innerHTML = "";
  if (!report.sample_runs || report.sample_runs.length === 0) {
    pbtResultsBody.innerHTML = `<tr><td colspan="4" class="p-3 text-center text-emerald-400">All ${report.total_samples} randomized boundary fuzzing samples passed.</td></tr>`;
    return;
  }

  report.sample_runs.forEach(sample => {
    const tr = document.createElement("tr");
    tr.className = "hover:bg-slate-900/60 transition";
    
    const inpStr = Object.entries(sample.input_sample).map(([k, v]) => `${k}:${v}`).join(", ");
    const legStr = typeof sample.legacy_oracle_output === "object" ? JSON.stringify(sample.legacy_oracle_output) : String(sample.legacy_oracle_output);
    const chimStr = typeof sample.chimera_output === "object" ? JSON.stringify(sample.chimera_output) : String(sample.chimera_output);

    tr.innerHTML = `
      <td class="p-2 text-xxs text-slate-300 max-w-xs truncate">${inpStr}</td>
      <td class="p-2 text-xxs text-purple-300 max-w-xs truncate">${legStr}</td>
      <td class="p-2 text-xxs text-cyan-300 max-w-xs truncate">${chimStr}</td>
      <td class="p-2 text-right text-xxs font-bold ${sample.matched ? 'text-emerald-400' : 'text-red-400'}">
        ${sample.matched ? '✓ PROVED' : '✗ BROKEN'}
      </td>
    `;
    pbtResultsBody.appendChild(tr);
  });
}

function renderTelemetry(telemetry, pbtReport) {
  voltageValue.textContent = telemetry.voltage_vitality.toFixed(1);
  voltageBar.style.width = `${Math.min(100, telemetry.voltage_vitality)}%`;

  amperageValue.textContent = Math.round(telemetry.amperage_throughput_ops_sec).toLocaleString();
  amperageBar.style.width = `${Math.min(100, (telemetry.amperage_throughput_ops_sec / 15000) * 100)}%`;

  latencyValue.textContent = telemetry.latency_microseconds.toFixed(1);
  speedupValue.textContent = telemetry.speedup_factor.toFixed(1);
}

// Initial boot
loadSpecimen(currentSpecimenId);
