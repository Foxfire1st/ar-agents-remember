# dashboard/src/tray/TrayPanel.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Renders the minimized collection line and expanded tray controls.

## Code Commentary

### Logic

Accepts pasted image files, shows named storage/plugin/send outcomes, renders picks/targets/message/Send, keeps helper text on its own row, exposes local preferences and sent log, and starts snapshot sending.

### Invariants And Boundaries

Minimized line has no expanded controls. Close retains picks. Screenshots are pasted OS clipboard files, not display capture or DOM rendering. Positive bounds remain browser preferences.

## Evidence

- Renders the minimized collection line and expanded tray controls. [1]
- Renders the minimized collection line and expanded tray controls. [2]
- Renders the minimized collection line and expanded tray controls. [3]

The minimized line's head is now an accessible button surface: a click outside a nested control, Enter or space expands it. controlWithin excludes button, a, input, textarea, select and elements with role button, link or menuitem; it does not inspect generic contenteditable elements so the existing ⊕ button and Close control keep their own actions; the line does not intercept their clicks or keys. The expanded pick/message/Send view and Close-retains-picks policy remain unchanged.

- The minimized line's head is now an accessible button surface: a click outside a nested control, Enter or space expands it. controlWithin excludes button, a, input, textarea, select and elements with role button, link or menuitem; it does not inspect generic contenteditable elements so the existing ⊕ button and Close control keep their own actions; the line does not intercept their clicks or keys. The expanded pick/message/Send view and Close-retains-picks policy remain unchanged. [4]
