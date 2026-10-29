# Design system

## Direction

An editorial portfolio with generous spacing, expressive photography and a quiet interface. The original ROHENI logo remains the signature. Typography frames the work rather than imitating the logo.

The reference site informed the desired sense of an unfolding portfolio. Its full visual behaviour could not be verified in the research browser, so this implementation is not a pixel-for-pixel reproduction.

## Type

- Instrument Serif Regular and Italic: headlines, collection names and short editorial statements.
- Manrope Regular: descriptions and long-form reading.
- Manrope Medium: navigation, captions and small section labels.
- Body text: 15px default with a 1.7 line height.
- Headlines: responsive sizes using `clamp()`.
- Avoid oversized decorative type beside the logo, dense uppercase paragraphs and excessively light text.

Google Fonts loads the families. For offline or locally hosted fonts, download the official families, retain their licence files, place WOFF2 assets under `assets/fonts/`, add `@font-face` with `font-display: swap`, and remove the external font links. Do not bundle commercial fonts without a licence.

## Colour

| Token | Value | Use |
| --- | --- | --- |
| Paper | `#f5f2ec` | Warm editorial background |
| Ink | `#2e2e2e` | Main text |
| ROHENI red | `#7a0000` | Emphasis, selection and process section |
| Line | `#cfc9bf` | Quiet separators |
| Quiet | `#645c53` | Secondary text |

The logo artwork is unchanged. Its transparent black version is used on the light background. The selected warm paper is a site surface; the original white brand colour remains valid for other applications.

## Layout

Desktop: split opening, alternating four-project collection grid, alternating narrative and visual sections. Mobile: stacked layout, expanded navigation and full-width projects. Adwoa women’s sets and accessories now have separate case studies.

## Accessibility

Skip link, semantic navigation, one main heading per page, labelled image buttons, native dialog, visible focus, Escape dismissal, focus restoration and reduced-motion support are included. Informative images carry alt text. Links remain readable without animation. No autoplay or custom cursor is used.

## Image treatment

Opening imagery can crop for composition; project openings use `object-fit: contain` so full garments remain available. Galleries also contain the image and provide an enlarged view. Check new images individually instead of assuming one crop fits every garment.
