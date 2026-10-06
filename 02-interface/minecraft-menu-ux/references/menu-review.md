# Mode-neutral menu review

Use for any picker, form or actionable menu. Confirm the primary task, current
selection, expected consequence and exit behavior. For a loadout this means kit
contents; for settings it means applied values; for a trade it means items/cost.

Check long names, empty states, unavailable options and changing eligibility.
Activate the full intended card at center/edges and keyboard focus. Distinguish
normal, hover, selected, focused and disabled without relying only on color.

Preset quantities are optional. When present, selected count, total and commit label
must agree. Example arithmetic: 40 per item with counts 1/8/64 gives 40/320/2,560;
these are fixtures, not recommended prices. For other menus test equivalent state
coherence, such as selected team versus Join team action.

Native ESC/focus/warning behavior depends on surface/client. Record cursor movement
across changes and avoid screen recreation as a fake animation. Preview images do
not establish actual click bounds or stable focus.
