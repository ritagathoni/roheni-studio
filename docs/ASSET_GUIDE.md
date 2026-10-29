# Image and asset guide

## Uploaded asset integration

The supplied `roheni-portfolio-assets.zip` contained 57 image files and the project-notes document. The updated repository uses a curated selection rather than displaying every near-duplicate image.

The public site includes first-collection photographs, Adwoa sets, bags, material/process images and eight Collection II digital or sketch-style concepts. It keeps the original logo and the founder portrait from the earlier PDF. The new `02-portrait` folder contains campaign group photographs, rather than a personal founder portrait.

All selected photographs were corrected for EXIF orientation, resized without stretching and exported to WebP. Original source files remain unchanged. Images are generally limited to 2000 pixels wide and 2200 pixels tall.

## Exact asset provenance

See `asset-provenance.json` in this documentation folder for the source filename corresponding to each new website image. The website uses descriptive filenames so later replacements remain straightforward.

| Website image group | Source folder | Use |
| --- | --- | --- |
| Logo | `01-brand` | Navigation |
| Campaign group | `02-portrait` | The Herd opening and contact |
| Denim photographs | `03-kaleidoscope` | Homepage and Kaleidoscope project |
| Cowhide/leather photographs | `04-the-herd` | The Herd project |
| Adwoa, bags and accessories | `05-acessories` | Separate Adwoa and accessory projects |
| Materials, drawing and tailoring | `06-process` | The making page and project galleries |
| Digital concepts and studies | `07-collection-two` | Development journal |

## Add or replace a photograph

1. Keep a separate backup of the original.
2. Export the selected image as WebP, preserving texture and construction detail.
3. Use a lowercase descriptive filename with hyphens. Paths are case-sensitive on GitHub Pages.
4. Place the file in `assets/images/`.
5. Update the relevant entry in `content/site.json`. Image references omit the `.webp` extension.
6. Update the caption and alternative text to describe the image accurately.
7. Run `python3 scripts/check_site.py` and review the result on desktop and mobile.

The central content file includes `projects`, `development` and `process` image arrays. Development entries also have a `type`: keep this aligned with the filter names, “Digital concept” or “Design study”.

## Development labels

Collection II photorealistic concepts are labelled “AI-assisted visualisation” and are not presented as garments already produced. Generated sketch-style sheets are labelled as AI-assisted design studies, not hand-drawn originals. The drawing from the process archive is described neutrally until its authorship is confirmed.

Add photographs of physical samples separately, with a date, development stage and maker credit. Do not remove the concept labels merely because a visual looks realistic.

## Permissions and credits

For every public image, record the creator, contributors, permission scope and credit wording. Add named credits once confirmed. Keep written permission messages and private correspondence outside the public repository. The supplied notes still contain confirmation fields; this update does not invent names or treat those fields as completed permissions.

The source ZIP and internal Word document are not copied into the public website.
