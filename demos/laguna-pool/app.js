"use strict";
const $ = (id) => document.getElementById(id);
let current;
let step = 0;
let receiptUrl;
async function request(path, data) {
  const options =
    data === undefined
      ? {}
      : {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        };
  const response = await fetch(path, options);
  const result = await response.json();
  if (!response.ok) throw new Error(result.error);
  return result;
}
async function act(task) {
  $("error").hidden = true;
  try {
    await task();
  } catch (error) {
    $("error").textContent = error.message;
    $("error").hidden = false;
  }
}
function showValues(target) {
  target.replaceChildren();
  const dl = document.createElement("dl");
  for (const [key, value] of Object.entries(current.fields)) {
    const dt = document.createElement("dt");
    dt.textContent = key.replaceAll("_", " ");
    const dd = document.createElement("dd");
    dd.textContent = value || "Unknown — required before demo submission";
    dl.append(dt, dd);
  }
  target.append(dl);
  for (const category of ["Application", "Plans"]) {
    const p = document.createElement("p");
    const file = current.attachments[category];
    p.textContent = file
      ? `${category}: ${file.name} (${file.size} bytes) · SHA-256 ${file.sha256}`
      : `${category}: MISSING`;
    p.className = "file-detail";
    target.append(p);
  }
}
function render() {
  const submitted = current?.status === "demo_submitted";
  $("start").hidden = !!current;
  $("workflow").hidden = !current || submitted;
  $("receipt").hidden = !submitted;
  if (!current) return;
  $("case-id").textContent = current.id;
  $("save-status").textContent = submitted
    ? "Demo receipt saved"
    : "Draft saved on this computer";
  ["project", "documents", "review-panel"].forEach(
    (id, i) => ($(id).hidden = i !== step),
  );
  document
    .querySelectorAll("[data-step]")
    .forEach((button) =>
      button.setAttribute(
        "aria-current",
        Number(button.dataset.step) === step ? "step" : "false",
      ),
    );
  for (const [key, value] of Object.entries(current.fields))
    $("project").elements[key].value = value || "";
  for (const [id, category] of [
    ["application-file", "Application"],
    ["plans-file", "Plans"],
  ])
    $(id).textContent =
      current.attachments[category]?.name || "No file uploaded";
  showValues($("review-data"));
  if (submitted) {
    $("receipt-id").textContent = current.receipt.record_number;
    showValues($("receipt-data"));
    if (receiptUrl) URL.revokeObjectURL(receiptUrl);
    receiptUrl = URL.createObjectURL(
      new Blob([JSON.stringify(current, null, 2)], {
        type: "application/json",
      }),
    );
    $("download").href = receiptUrl;
    $("download").download = current.id + "-sample-receipt.json";
  }
}
async function save() {
  current = await request(`/api/cases/${current.id}/save`, {
    fields: Object.fromEntries(new FormData($("project"))),
  });
}
async function switchStep(next) {
  await save();
  step = next;
  render();
}
$("create").onclick = () =>
  act(async () => {
    // Persist identity in the URL, so refreshing or revisiting resumes the same case.
    current = await request("/api/cases", {});
    history.replaceState(null, "", `?case=${encodeURIComponent(current.id)}`);
    render();
  });
$("project").onsubmit = (event) => {
  event.preventDefault();
  act(() => switchStep(1));
};
document
  .querySelectorAll("[data-step]")
  .forEach(
    (button) =>
      (button.onclick = () =>
        act(() => switchStep(Number(button.dataset.step)))),
  );
$("review").onclick = () => act(() => switchStep(2));
for (const [id, category] of [
  ["application", "Application"],
  ["plans", "Plans"],
]) {
  $(id).onchange = () =>
    act(async () => {
      const file = $(id).files[0];
      if (!file) return;
      if (file.size > 16 * 1024 * 1024)
        throw new Error("Choose a PDF of at most 16 MB");
      const encoded = await new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.split(",")[1]);
        reader.onerror = reject;
        reader.readAsDataURL(file);
      });
      current = await request(`/api/cases/${current.id}/upload`, {
        category,
        name: file.name,
        base64: encoded,
      });
      render();
    });
}
$("submit").onclick = () =>
  act(async () => {
    $("submit").disabled = true;
    try {
      await save();
      current = await request(`/api/cases/${current.id}/submit`, {});
      render();
    } finally {
      $("submit").disabled = false;
    }
  });
act(async () => {
  const id = new URLSearchParams(location.search).get("case");
  if (id) {
    current = await request(`/api/cases/${encodeURIComponent(id)}`);
    render();
  }
});
