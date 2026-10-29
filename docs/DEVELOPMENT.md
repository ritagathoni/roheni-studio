# Developer notes

## Architecture

Buildless HTML/CSS/JavaScript. Each page provides its own metadata and `data-page` value. `app.js` loads `content/site.json`, renders shared navigation/footer, selects a page renderer and initialises interactive images. `project.html` uses a project ID query parameter; unknown IDs show a useful fallback.

The content loader needs HTTP. A static hosting service is sufficient; no server secrets or runtime environment variables are required.

## Path handling

All paths are relative, so the project works under a repository subdirectory on GitHub Pages. Do not change assets to leading-slash URLs unless deploying at the domain root. If introducing nested HTML directories, update relative references carefully.

## Content safety

JSON text is escaped before insertion into HTML. Do not add untrusted raw HTML fields. URL fields should contain verified HTTPS or mailto destinations. Keep the public JSON free of customer information, financial records and internal notes.

## Editing and validation

Run `python3 scripts/check_site.py` after image renames or content changes. The checker catches missing local HTML references, missing project image files, empty required content and duplicate project IDs. It does not replace visual QA or establish correctness of creative claims.

`node --check assets/js/app.js` checks JavaScript syntax when Node is available. No npm installation is needed.

## Deployment

The Actions workflow stages only public HTML, `.nojekyll`, `assets/` and `content/` into `_site` before uploading. It excludes internal docs from the published website, although those docs remain visible in a public repository.

The `.openai/hosting.json` file and `dist/` directory may exist only in the authoring workspace for internal preview. They are excluded from the deliverable ZIP and Git tracking and are not needed for GitHub Pages.

## Possible next improvements

1. Add physical Collection II sample photography when available and confirm creator credits.
2. Add the final downloadable application PDF.
3. Move remaining page narrative into JSON if nontechnical editing becomes frequent.
4. Consider static pre-rendering for no-JavaScript access and crawler reliability.
5. Add a custom domain and social-share image only when the actual domain is selected.

Avoid adding heavy animation or a framework without a concrete need. The portfolio’s job is to make the work and process easy to see.
