# Expressive red edition

Background: #7A0000. Cream #FFF1D9, gold #F6CC77.
Navigation: Home, About, Collections, Studio, Upcoming, Contact. Making remains linked from the studio and home.
Collection I has individual stories and galleries for Kaleidoscope, The Herd, Adwoa and Accessories.

## Fonts
This edition loads free Fraunces and Archivo via Google Fonts. These are provisional alternatives, not Recoleta or a Berthold font. Recoleta is by Latinotype; Berthold is a foundry, so the exact desired family needs confirmation. Do not upload commercial desktop fonts to a public repository. Supply licensed webfonts and the permitted hosting terms before replacing the free families. CSS variables --serif and --sans define the stacks.

## Layered hero
The main portrait foreground is assets/images/herd-cutout.png. It is an AI-assisted background extraction from herd-portrait.webp, generated with the instruction to remove only the white background and preserve the person and clothing. The untouched original remains in the collection gallery. Compare fine details before final application submission. HTML text remains accessible and responsive behind the foreground image. No generated clothing is presented as a new completed garment.
Textbehindimage.com was tested with the same portrait; its downloaded output omitted the text, so that export is not used. No external stock photos or Resource Boy assets are included.

## Upload this update
Extract the ZIP. Upload the contents of roheni-studio to the root of ritagathoni/roheni-studio, replacing files with matching names. Include about.html and assets/images/herd-cutout.png. Commit to main. If GitHub Pages is configured from main/root it will rebuild automatically. The website uses relative paths.

## Playground refinement
Barriecito (SIL Open Font License, discovered through Free Faces) now accents navigation, collection links and the badge. Fraunces remains the editorial headline and narrative face. Uncut.wtf Redaction was researched as an alternative; its files are not bundled. Sources: https://www.freefaces.gallery/typefaces/barriecito and https://uncut.wtf/serif/redaction/.

Theme buttons select Red #7A0000, Paper #FEFEFE or Charcoal #2E2E2E; the choice persists locally in the visitor’s browser without an account or tracking. The marquee remains charcoal in every theme. Its lettering animates in CSS; a global Pause/Resume control and prefers-reduced-motion support are included. The flying play-shaped control pauses/resumes decorative motion: it does not claim to open a video. No video was supplied.

Founder introduction uses live curved SVG lettering, a decorative stylised hemisphere/map motif, and Rita’s original portrait. It is not a precise cartographic diagram. No AMOUR reference image was present among the three supplied screenshots, so the curve was interpreted from the written brief. The female cowhide digital concept is now the Collection II lead and remains explicitly labelled AI-assisted.

The supplied exact marquee screenshot was edited with the built-in image tool to create studio-banner-texture.png: charcoal, no lettering, sparse chalk stitch and panel sketches at the edges. HTML supplies the actual animated text. Generated decorative texture is not evidence of a made garment.

Validation: Python local reference checker and JavaScript syntax pass. Desktop themes and pause/resume tested; 390px iframe used for narrow layout and mobile menu checks. A physical phone review is still recommended.
