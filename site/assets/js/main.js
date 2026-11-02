// Mobile nav toggle
const toggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".nav-links");
if (toggle && links) {
  toggle.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open);
  });
}

// Highlight the current page in the nav
const page = location.pathname.split("/").pop().replace(".html", "") || "index";
document.querySelectorAll(".nav-links a").forEach((a) => {
  const target = a.getAttribute("href").replace(".html", "").replace("/", "") || "index";
  if (target === page) a.classList.add("active");
});

// Fade sections in as they scroll into view
const io = new IntersectionObserver(
  (entries) => entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
  }),
  { threshold: 0.12 }
);
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

// Photo carousels: arrows, dots and gentle autoplay (paused on hover)
document.querySelectorAll(".carousel").forEach((carousel) => {
  const track = carousel.querySelector(".carousel-track");
  const slides = [...track.children];
  const dots = carousel.querySelector(".carousel-dots");
  let index = 0;

  const go = (i) => {
    index = (i + slides.length) % slides.length;
    track.scrollTo({ left: index * track.clientWidth });
  };

  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.setAttribute("aria-label", `Photo ${i + 1}`);
    dot.addEventListener("click", () => go(i));
    dots.appendChild(dot);
  });

  const sync = () => {
    index = Math.round(track.scrollLeft / track.clientWidth);
    [...dots.children].forEach((d, i) => d.classList.toggle("active", i === index));
  };
  track.addEventListener("scroll", sync, { passive: true });
  sync();

  carousel.querySelector(".prev").addEventListener("click", () => go(index - 1));
  carousel.querySelector(".next").addEventListener("click", () => go(index + 1));

  const delay = Number(carousel.dataset.autoplay);
  if (delay && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    let timer = setInterval(() => go(index + 1), delay);
    carousel.addEventListener("mouseenter", () => clearInterval(timer));
    carousel.addEventListener("mouseleave", () => (timer = setInterval(() => go(index + 1), delay)));
  }
});

// Footer year
const year = document.getElementById("year");
if (year) year.textContent = new Date().getFullYear();
