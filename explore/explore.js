// Filters the module list in the page. No network request; without JavaScript every module is simply listed.
(function () {
  var q = document.getElementById("q"), area = document.getElementById("area");
  var chips = [].slice.call(document.querySelectorAll("[data-chip]"));
  var cards = [].slice.call(document.querySelectorAll(".mod"));
  var out = document.getElementById("count"), empty = document.getElementById("empty");
  var status = "all";
  function apply() {
    var t = q.value.trim().toLowerCase(), a = area.value, n = 0;
    cards.forEach(function (c) {
      var ok = (!t || c.dataset.text.indexOf(t) > -1) && (!a || c.dataset.area === a) && (status === "all" || c.dataset.status === status);
      c.hidden = !ok; if (ok) n++;
    });
    out.textContent = n + " of " + cards.length + " modules";
    empty.hidden = n > 0;
  }
  q.addEventListener("input", apply);
  area.addEventListener("change", apply);
  chips.forEach(function (b) {
    b.addEventListener("click", function () {
      status = b.dataset.chip;
      chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      apply();
    });
  });
  try { var p = new URLSearchParams(location.search); if (p.get("q")) q.value = p.get("q"); } catch (e) {}
  apply();
})();
