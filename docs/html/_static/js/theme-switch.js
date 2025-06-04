document.addEventListener("DOMContentLoaded", function () {
  const isDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

  const links = document.querySelectorAll("link[rel='stylesheet']");
  let lightCSS = null;
  let darkCSS = null;

  links.forEach(link => {
    if (link.href.includes("light.css")) lightCSS = link;
    if (link.href.includes("dark.css")) darkCSS = link;
  });

  if (isDarkMode) {
    if (lightCSS) lightCSS.disabled = true;
    if (darkCSS) darkCSS.disabled = false;
  } else {
    if (darkCSS) darkCSS.disabled = true;
    if (lightCSS) lightCSS.disabled = false;
  }
});
