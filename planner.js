const WEEKDAY_KEYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];
const WEEKDAY_LABELS = {
  sunday: "Sonntag",
  monday: "Montag",
  tuesday: "Dienstag",
  wednesday: "Mittwoch",
  thursday: "Donnerstag",
  friday: "Freitag",
  saturday: "Samstag",
};

const CATEGORY_ORDER = ["Training", "Mental", "Alltag", "Haushalt & Selfcare"];

const state = {
  data: null,
  selectedDate: startOfDay(new Date()),
};

function startOfDay(date) {
  const clone = new Date(date);
  clone.setHours(0, 0, 0, 0);
  return clone;
}

function addDays(date, amount) {
  const clone = new Date(date);
  clone.setDate(clone.getDate() + amount);
  return startOfDay(clone);
}

function diffDays(a, b) {
  return Math.round((startOfDay(a) - startOfDay(b)) / 86400000);
}

function getCycleWeek(date, cycleStart, cycleLengthWeeks) {
  const diff = diffDays(date, cycleStart);
  const weekIndex = Math.floor(diff / 7);
  const normalized = ((weekIndex % cycleLengthWeeks) + cycleLengthWeeks) % cycleLengthWeeks;
  return normalized + 1;
}

function formatDate(date) {
  return new Intl.DateTimeFormat("de-DE", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  }).format(date);
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderTask(task, link) {
  const linkHtml = link ? `<a class="task-link" href="${link}">Quelle</a>` : "";
  return `
    <article class="task-item">
      <div class="task-head">
        <h4>${escapeHtml(task.title)}</h4>
        ${linkHtml}
      </div>
      <p>${escapeHtml(task.details || "")}</p>
    </article>
  `;
}

function collectTasks(data, date) {
  const weekdayKey = WEEKDAY_KEYS[date.getDay()];
  const cycleStart = startOfDay(new Date(data.meta.cycleStart));
  const cycleWeek = getCycleWeek(date, cycleStart, data.meta.cycleLengthWeeks);
  const items = [...data.defaults.daily, ...data.weekdays[weekdayKey].tasks];
  const cycleItems = (data.cycleWeeks[String(cycleWeek)] && data.cycleWeeks[String(cycleWeek)][weekdayKey]) || [];
  items.push(...cycleItems);

  const grouped = {};
  for (const category of CATEGORY_ORDER) {
    grouped[category] = [];
  }
  for (const item of items) {
    if (!grouped[item.category]) {
      grouped[item.category] = [];
    }
    grouped[item.category].push(item);
  }

  return {
    weekdayKey,
    weekdayLabel: WEEKDAY_LABELS[weekdayKey],
    cycleWeek,
    focus: data.weekdays[weekdayKey].focus,
    grouped,
  };
}

function renderPlanner() {
  const { data, selectedDate } = state;
  const summary = collectTasks(data, selectedDate);

  document.getElementById("planner-date").textContent = formatDate(selectedDate);
  document.getElementById("planner-meta").textContent = `Wochentag: ${summary.weekdayLabel} · Rotationswoche: ${summary.cycleWeek}/${data.meta.cycleLengthWeeks}`;
  document.getElementById("planner-focus").textContent = summary.focus;

  const notes = document.getElementById("planner-notes");
  notes.innerHTML = data.meta.notes
    .map((note) => `<div class="note"><p>${escapeHtml(note)}</p></div>`)
    .join("");

  const categories = document.getElementById("planner-categories");
  categories.innerHTML = CATEGORY_ORDER.map((category) => {
    const tasks = summary.grouped[category] || [];
    const link = data.categoryLinks[category] || "";
    return `
      <section class="planner-card panel">
        <div class="planner-card-head">
          <h3>${escapeHtml(category)}</h3>
          <span class="planner-count">${tasks.length} Aufgaben</span>
        </div>
        ${tasks.length ? tasks.map((task) => renderTask(task, link)).join("") : '<p class="small">Keine Aufgaben für diesen Bereich.</p>'}
      </section>
    `;
  }).join("");
}

async function init() {
  const response = await fetch("data/plans.json");
  if (!response.ok) {
    throw new Error("Konnte data/plans.json nicht laden.");
  }
  state.data = await response.json();
  renderPlanner();

  document.getElementById("prev-day").addEventListener("click", () => {
    state.selectedDate = addDays(state.selectedDate, -1);
    renderPlanner();
  });

  document.getElementById("next-day").addEventListener("click", () => {
    state.selectedDate = addDays(state.selectedDate, 1);
    renderPlanner();
  });

  document.getElementById("today").addEventListener("click", () => {
    state.selectedDate = startOfDay(new Date());
    renderPlanner();
  });
}

init().catch((error) => {
  document.getElementById("planner-date").textContent = "Fehler beim Laden";
  document.getElementById("planner-meta").textContent = error.message;
});
