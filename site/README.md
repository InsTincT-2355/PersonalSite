# Ahmed Al Touqi — Personal Website

Plain HTML/CSS/JS, no build step. Dark theme.

| Page | File |
|------|------|
| Home | `index.html` |
| About | `about.html` |
| School (coursework → GitHub) | `school.html` |
| Achievements (Studio 21, Muriya Nexus) | `projects.html` |

Shared styles live in `assets/css/style.css`, shared script in `assets/js/main.js`.

## Deploy on Vercel
1. In Vercel: **Add New → Project → Import** the `PersonalSite` repo.
2. Set **Root Directory** to `site`. Framework preset: **Other**. Leave build command and output directory empty.
3. Deploy. `vercel.json` enables clean URLs (`/about` instead of `/about.html`).

## Editing
- Course links on the School page point to `School/Courses/<course>` in this repo.
- Swap the home hero photo by replacing `assets/img/ahmed-graduation.jpg`; the About portrait is `assets/img/ahmed.jpg`.
