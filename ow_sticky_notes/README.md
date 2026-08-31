# Sticky Notes — Floating Quick Notes Widget (Odoo 16)

A Windows-Sticky-Notes-style widget for the Odoo backend.

## What it does

- A small floating **ball** sits in the corner of every backend screen —
  list, form, kanban, Settings, everywhere. It survives navigation because
  it's registered in the `main_components` registry, the same mechanism
  Odoo uses for the Discuss chat windows.
- **Click the ball** → a notes panel **slides in from the right**.
- **Click again** (or the X, or click outside on mobile) → it hides. The
  ball stays put.
- Keep **multiple** notes, not just one — click **+** to add another.
- Each note is **colour-coded** (6 colours) — click a swatch to change it.
- **Autosaves** ~0.6s after you stop typing. No save button.
- **Pin** a note to keep it at the top of the list.
- **Link a note to the current record** (🔗 icon) — switch the "This
  record" filter to see only notes tied to whatever you have open.
- **Alt+N** toggles the panel from anywhere.
- The ball is **draggable** — drag it to a spot that's out of your way;
  position is remembered per browser.
- Notes are private per user and stored server-side (`ow.sticky.note`),
  so they follow you across devices/sessions. A record rule keeps every
  user scoped to their own notes.
- A fallback list/form view is under **Settings → Technical → Sticky
  Notes** (dev mode) in case you ever need to bulk-inspect/clean up notes
  as an admin.

## Install

1. Copy the `ow_sticky_notes` folder into your Odoo 16 addons path.
2. Update Apps list, search "Sticky Notes", install.
3. No configuration needed — the ball appears immediately for every
   internal user.

## Notes on the implementation

- Ported from the Odoo 19 version. The only structural difference for 16 is
  view syntax: `<tree>` (not `<list>`) and the old `attrs="{...}"` dict
  syntax for the conditional "Linked Record" group (16 predates Odoo 17's
  direct `invisible="..."` expressions).
- The JS widget's core building blocks (`@odoo/owl` hooks, the `orm`,
  `action`, `hotkey`, `notification` services, the `main_components`
  registry, `@web/core/l10n/translation`) are all present in 16 and kept
  as-is. The one call that reads private-ish internals —
  `actionService.currentController.props`, used for the "link to current
  record" feature — is wrapped in try/catch and degrades gracefully if
  that shape differs on 16; everything else keeps working either way.

- Text fields are intentionally *uncontrolled* after first render (no
  re-binding of `value`/text content on every keystroke) to avoid cursor
  jumps while autosave debounces in the background.
