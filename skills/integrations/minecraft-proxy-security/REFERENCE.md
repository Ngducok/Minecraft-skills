# Evidence reference

Contracts describe intended applicability, not certified binary compatibility. Resolve exact version/build, toolchain and dependency coordinates. Inspect pinned APIs or native assets before using symbols/formats.

Source inspection checks documentation; it does not establish compile, runtime or client success. Rolling documentation may target a different release. Community design guidance and inferred balancing are not official mechanics.

## Sources

- [Velocity backend security](https://docs.papermc.io/velocity/security/) — registry ID `velocity-security`; inspected 2026-10-06. Offline backend authentication requires network isolation and trusted forwarding; forwarding alone is not a firewall.
- [Velocity player forwarding](https://docs.papermc.io/velocity/player-information-forwarding/) — registry ID `velocity-forwarding`; inspected 2026-10-06. Forwarding mode must agree with backend configuration and installed platform support.

Shared source records: [knowledge/sources.json](../../../knowledge/sources.json).
