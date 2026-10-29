# ROHENI — paper edition

## Three typefaces

- **Fraunces**: editorial headlines, italic emphasis and collection introductions. Weights 400/500/600; use its shapes rather than adding further display fonts.
- **Plus Jakarta Sans**: navigation, body copy, captions, controls and contact information. Weights 400/500/600/700.
- **League Gothic**: compact material labels, the circular badge, cultural-reference cards and marquee.

All three are available under SIL Open Font Licences and are requested through Google Fonts. No commercial demo font is embedded. The original ROHENI logo is an image asset, separate from the type system. Font loading is declared in each HTML entry page. `premium.css` defines the final family variables; `styles.css` retains the earlier layout base.

## Colour

Paper is the initial theme, including for visitors who used an earlier red-default version. Paper #F1F0ED, ink #292929, mission panel #E5E4E0, photo mount #D4D4D1, red accent #7A0000. Red and charcoal #2E2E2E remain visitor choices. Mounts remain grey. Theme preference is stored only in localStorage under roheni-theme-v3.

## Composition

The collage hero preserves readable lettering and links to real project galleries. Header links have irregular outlines with consistent typography. The mission and inspiration previews lead into dedicated pages. The founder globe is a decorative full sphere/map motif, not precise cartography. The gently bent logo is rendered from the original PNG with column sampling on a retina canvas; it is not retyped or generated. The childhood image has an AI-assisted background extraction. The original supplied photo remains outside the public site.

## Motion & interaction

CSS marquee and floating control; one-time heading entrances; subtle hover movement. Pause/Resume and prefers-reduced-motion support. The inspiration board supports mouse dragging, arrow keys, shuffle and reset. Touch users can scroll normally and use the shuffle/reset controls. The video is a nine-second silent MP4 motion study created from still textures. It plays when visible where the browser permits and pauses out of view; native controls allow manual playback. User pause is respected. It is labelled as animated stills.

## Editing

`assets/js/app.js`: homepage, mission, inspiration, interactive behaviour and logo drawing.
`assets/css/premium.css`: final design decisions and responsive styling.
`content/site.json`: collections and galleries, contacts, milestones, development archive.
`assets/video/material-study.mp4`: finished motion study.

The website is static. No account, data-collection form or paid app is required.
