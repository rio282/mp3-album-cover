# MP3 Album Cover (Stitcher)

A small Python desktop application built with **Tkinter** that allows you to embed (stitch) an image as album art into
an MP3 file.

## How do I download the app?

Clone the repo:

```bash
git clone https://github.com/rio282/mp3-album-cover.git
```

**OR**

Download via GitHub:

> Press **< > Code** and then **Download ZIP**

## How do I use the app?

- Select an MP3 file
- Select an image (JPEG/PNG)
- Press **Stitch**
- *Uhh... Repeat?*

## Requirements

- *(Built in)* Python 3.9+
- Dependencies:
    - [eyeD3](https://pypi.org/project/eyed3/) (for MP3 tag editing)
    - [mutagen](https://pypi.org/project/mutagen/) (for reading MP3 info)
    - [Pillow](https://pypi.org/project/Pillow/) (for image processing)

Install dependencies with:

```bash
pip install -r requirements.txt
```

> *Make sure that you're in the root directory of the project when running the command above*

## Notes

- The MP3 file will be modified in place. *Make a backup if needed.*
- Supported image types: JPEG, PNG.
