# OpenDyslexic Mono build

OpenDyslexic Mono by Abbie Gonzalez has no compiled release. This repository
holds a build of it from the official source, for the OpenDyslexic setting of
the notes app.

- `source/OpenDyslexic-Mono.glyphs`: unchanged, from
  [antijingoist/opendyslexic](https://github.com/antijingoist/opendyslexic),
  `sources/opendyslexic-mono/`, commit `1824da5c0e41dc3e13ffc7f3a636dcaf695d61b7`.
- `fonts/`: the build, one weight (Regular), 585 characters, French accents included.
- `build.py`: makes `fonts/` again. The only change to the source is removing
  44 mark anchors with no name, which stop fontmake. Tool versions are pinned
  in `requirements.txt`.

```
python -m venv venv
venv/Scripts/python -m pip install -r requirements.txt
venv/Scripts/python build.py
```

## Licence

SIL Open Font License 1.1, see `OFL.txt`. OpenDyslexic is a Reserved Font
Name of its author.
