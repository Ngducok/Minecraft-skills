---
name: minecraft-animation-sound
description: "Add or assess resource-pack texture animation, display-entity interpolation, menu motion and gameplay sound feedback."
---

# Minecraft motion and sound feedback

Identify the actual animation surface first: texture atlas sprite, display entity transform, native widget, modded screen or server-redrawn menu. These mechanisms have different timing and support.

- Use texture metadata only for sprites/atlases that the target renderer animates. Bitmap-font images and arbitrary UI glyphs do not inherit atlas animation support by assumption.
- Use display interpolation for world-space visual movement where supported; pair interaction/collision separately. A Paper server cannot inject arbitrary client screen tweening.
- Let motion explain a user action, cooldown or production state. Avoid constant flashing and repeated Dialog reopen loops that move the pointer or interrupt input.
- Register sound assets/events according to target format and provide volume-aware, sparse cues. Sound must not be the only signal of success, error or danger.
- Cap particles, viewers and update frequency; no task per decorative pixel. Offer reduced feedback where the product needs it rather than treating busy animation as polish.

## Verification

Test target client reload, muted audio, low FPS and rapid repeated actions. Check server update rate and whether controls remain stable during feedback.

## Example request

A shop animation resets the mouse every frame; replace repeated screen redraws with supported action feedback.

## Contract and evidence

Read [contract.json](contract.json) for applicability and required outputs; [REFERENCE.md](REFERENCE.md) for evidence and version limits. No listed verified release means resolve the target before generation. [tests/scenario.json](tests/scenario.json) contains a behavioral evaluation prompt, not proof that an agent passed.
