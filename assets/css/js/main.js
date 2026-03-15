const header = `
<header class="topbar">
  <div class="container navbar">
    <a class="brand" href="index.html" aria-label="DharmQuant home">
      <span class="brand-mark">DQ</span>
      <span>DharmQuant</span>
    </a>

    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="navLinks">
      Menu
    </button>

    <nav class="nav-links" id="navLinks">
      <a href="about.html">About</a>
      <a href="research.html">Research</a>
      <a href="strategies.html">Strategies</a>
      <a href="risk.html">Risk</a>
      <a href="contact.html">Contact</a>
    </nav>
  </div>
</header>`;

const footer = `
<footer class="footer">
  <div class="container footer-inner">
    <div>
      <strong>DharmQuant</strong><br>
      <span>Systematic investment research and quantitative infrastructure.</span>
    </div>
    <div class="small">
      © ${new Date().getFullYear()} DharmQuant. All rights reserved.
    </div>
  </div>
</footer>`;

document.addEventListener("DOMContentLoaded", () => {
  const headerMount = document.getElementById("site-header");
  const footerMount = document.getElementById("site-footer");

  if (headerMount) headerMount.innerHTML = header;
  if (footerMount) footerMount.innerHTML = footer;

  const toggle = document.getElementById("navToggle");
  const links = document.getElementById("navLinks");

  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
  }

  const current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((a) => {
    if (a.getAttribute("href") === current) a.classList.add("active");
  });
});