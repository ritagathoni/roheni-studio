# ROHENI Studio

A working creative portfolio for ROHENI’s first collection and upcoming work. Expressive red edition: #7A0000, cream typography, layered campaign collage, Fraunces and Archivo free font alternatives, and the original ROHENI logo.

**Status:** updated version with selected images from the uploaded asset folder and a visual development gallery for Collection II. This update is prepared for the existing ritagathoni/roheni-studio repository; it has not been published. See docs/REDESIGN.md.

## What is included

- Homepage with campaign image, studio story, selected work, process, development and milestones.
- Collections index and four project case studies.
- Studio page introducing Rita and the brand’s purpose, plus a dedicated making-process page.
- Collection II development journal with filterable digital concepts and design studies.
- Contact page with email and Instagram links.
- Responsive navigation and image viewer with keyboard support.
- Relative paths compatible with a GitHub project site.
- Automated GitHub Pages deployment, local validation and detailed editing documentation.
- No production dependencies, framework, package installation, paid plugins or backend.

Selected photographs, making images and concept studies come from the supplied asset ZIP. Their inclusion does not verify authorship or image permissions. Collection II digital and sketch-style concepts are labelled as AI-assisted development images. The founder portrait is retained from the earlier supplied PDF because the new portrait folder contains campaign group images. Confirm public credits before release. No shop, payment system, analytics or data-collection form is included.

## Start here

1. Unzip the repository folder.
2. Open a terminal inside `roheni-studio`.
3. Run `python3 -m http.server 8080` (Windows: `py -m http.server 8080`).
4. Open `http://localhost:8080`.
5. Read `docs/ASSET_GUIDE.md` to replace the provisional images.
6. Run `python3 scripts/check_site.py` before publishing.

Do not double-click `index.html`: the content is loaded from a local JSON file and needs an HTTP server. Node is optional; if installed, `npm start` runs the same server.

## Publish with GitHub Pages

1. Create a new repository called `roheni-studio` in your GitHub account.
2. Upload this folder’s **contents**, including `.github/workflows/pages.yml` and `.nojekyll`. Do not upload only the ZIP or an outer folder containing all the files.
3. Use `main` as the default branch.
4. Open repository **Settings → Pages → Build and deployment → Source → GitHub Actions**.
5. Open the **Actions** tab and run “Publish portfolio to GitHub Pages”, or commit another change to `main`.
6. Wait for the deployment job to finish and use the URL returned by GitHub.

A project site normally appears under `https://YOUR-USERNAME.github.io/roheni-studio/`. Replace the example username with yours; this is a URL pattern, not a deployed result.

On GitHub Free, use a public repository for Pages. Keep permission messages, customer records, grant letters, financial records and unpublished original files outside it.

Alternative: choose **Deploy from a branch → main → /(root)**. If you choose that option, disable the included deployment workflow so there is one publishing route. Branch publishing exposes repository files, so remove internal documentation you do not want public. The Actions workflow is preferred: it publishes only the HTML, assets and public content.

## Repository guide

| Location | Purpose |
| --- | --- |
| `index.html` | Homepage entry and metadata |
| `collections.html` | Collection index |
| `project.html?id=kaleidoscope` | Shared project template; URL chooses the project |
| `studio.html` | Founder and brand story |
| `journal.html` | Collection II in development |
| `process.html` | Materials, drawings and making |
| `contact.html` | Direct contact links |
| `404.html` | Missing-page fallback |
| `content/site.json` | Brand contact details, project content and milestone records |
| `assets/css/styles.css` | Visual system and responsive layouts |
| `assets/js/app.js` | Page rendering, navigation, lightbox and homepage/studio/journal copy |
| `assets/images/` | Public, optimised website images |
| `scripts/check_site.py` | Reference and content validation |
| `.github/workflows/pages.yml` | Validation, public-file packaging and Pages deployment |
| `docs/` | Editing, design, image and release instructions |

## Make changes

- **Project text and gallery captions:** edit `content/site.json`.
- **Email / Instagram:** edit `brand` in `content/site.json`.
- **Homepage, studio and journal narrative:** edit the named rendering functions in `assets/js/app.js`.
- **Colours, fonts, spacing:** edit `:root` and relevant rules in `assets/css/styles.css`.
- **Images:** replace corresponding `.webp` files without changing filenames, or update the image references.
- **New project:** duplicate one project record in `content/site.json`, give it a unique ID and add the referenced images. The collection grid updates automatically.
- **Browser titles and descriptions:** edit each HTML file. Project browser titles are set dynamically.

## Before the application

Read `docs/RELEASE_CHECKLIST.md`. In particular, add any future physical Collection II sample photographs, confirm image classifications, confirm all creative credits and rights, and verify the exact description of UN recognition and hotel collaborations.

The current site does not contain a final downloadable Swarovski portfolio PDF. Add an approved PDF and a visible download link when ready. Do not upload internal notes as the application portfolio by mistake.

## Verification completed

- Static check passes for nine HTML entry files, four project records and local references.
- JavaScript syntax checked with Node.
- Homepage visually inspected in the desktop browser.
- Navigation to Kaleidoscope verified.
- Image viewer opens and closes with Escape; focus returns to the opener.
- Collection II study filter verified in the browser.

Responsive rules are included for widths below 800px. A physical-device review and final browser checks with the original assets remain on the release checklist. Google Fonts is externally loaded; local font hosting is optional and documented in `docs/DESIGN_SYSTEM.md`.

## Ownership

ROHENI’s branding, copy, photographs and designs remain subject to their owners’ rights. No open-source licence is granted for the creative assets. See `RIGHTS.md`. The new layout is an original implementation inspired by the editorial direction discussed; no code or assets have been copied from oyin.design.
