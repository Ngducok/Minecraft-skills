# Resource pack walkthrough

Example target: Java client 1.21.11, resource format 75.0. No runnable pack or game assets are included.

For that exact target, document min_format/max_format as [75, 0]. A custom translation can live under assets/<namespace>/lang/en_us.json. Resolve other required locales separately.

Generate files in the user's project, enable the pack on a matching client, inspect reload logs and trigger its custom translation. JSON syntax checks do not prove translation resolution, glyph metrics or visual layout. Server API compilation cannot certify client rendering.
