// Builds a plain email from the form. No network request, nothing stored; the visitor sends it from their own email program.
(function () {
  var form = document.getElementById("contact");
  if (!form) return;
  try {
    var q = new URLSearchParams(location.search);
    ["region", "topic"].forEach(function (k) {
      var v = q.get(k), el = form.elements[k];
      if (v && el) for (var i = 0; i < el.options.length; i++) if (el.options[i].value === v) el.selectedIndex = i;
    });
  } catch (e) {}
  function label(el) { return el.options && el.selectedIndex > 0 ? el.options[el.selectedIndex].text : (el.value || "").trim(); }
  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var f = form.elements;
    var lines = [
      "Name: " + f.name.value.trim(), "Role: " + label(f.role), "Organisation: " + f.org.value.trim(),
      "Country: " + label(f.region), "Size: " + label(f.size), "Interest: " + label(f.topic), "Timing: " + label(f.when), "",
      f.msg.value.trim(), "", "(Sent from the ZYVORA website contact page. No patient data.)"
    ];
    var topic = label(f.topic) || "ZYVORA";
    location.href = "mailto:sales@zyvor.dev?subject=" + encodeURIComponent("ZYVORA: " + topic) + "&body=" + encodeURIComponent(lines.join("\n"));
  });
})();
