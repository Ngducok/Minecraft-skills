# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Paper plugin descriptors](https://docs.papermc.io/paper/dev/plugin-yml/) — registry ID `plugin-yml`; inspected 2026-10-06. Plugin metadata, API compatibility, commands and permission defaults belong in the correct descriptor.
- [Paper project setup](https://docs.papermc.io/paper/dev/project-setup/) — registry ID `paper-setup`; inspected 2026-10-06. Rolling examples use newer dependency coordinates; pin API and toolchain to requested release.
- [Paper event listeners](https://docs.papermc.io/paper/dev/event-listeners/) — registry ID `events`; inspected 2026-10-06. Cancellation and priorities affect cooperation with other plugins; observer handlers should not mutate results.

Shared source records: [knowledge/sources.json](../../../../knowledge/sources.json).
