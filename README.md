# MP3 Album Cover (Stitcher)

A small Python desktop application built with **Tkinter** that allows you to embed (stitch) an image as album art into
an MP3 file.

---

## Running the App

You have three ways of doing it:

### 1. Download the Prebuilt EXE *(Normie)*

> [Download the executable](https://github.com/rio282/mp3-album-cover/releases) from the **releases** page

- Simply download and run the executable (no Python installation required).
- Works on Windows 10+.

### 2. Run via Python *(Based)*

1. Clone the repository:
   ```bash
   git clone https://github.com/rio282/mp3-album-cover.git
    ```

2. Install dependencies:
    ```bash
   pip install -r requirements.txt 
   ```

3. Run the app:
    ```bash
   python main.py
   ```

- Should work on any platform

### Build Your Own executable *(Based & Might be convenient in some cases(?))*

If you want to create your own standalone executable using **PyInstaller**:

1. Make sure PyInstaller is installed:
    ```bash
   pip install pyinstaller
    ```

2. Navigate to the project root and run:
    ```bash
   pyinstaller --onefile --no-console main.py
   ```

3. The standalone EXE will be located in the `dist` folder.

---

## How to Use the App

- Select an MP3 file.
- Select an image (JPEG/PNG).
- Press **Stitch** to embed the image into the MP3.
- Use **Clear** to reset selections or **Exit** to quit.

---

## Requirements

- Python 3.9+ (if running via Python)
- Dependencies:
    - [eyeD3](https://pypi.org/project/eyed3/) – for MP3 tag editing
    - [mutagen](https://pypi.org/project/mutagen/) – for reading MP3 info
    - [Pillow](https://pypi.org/project/Pillow/) – for image processing

Install dependencies with:

```bash
pip install -r requirements.txt
```

> Make sure you’re in the project root when running the command above.

---

## Notes

- The MP3 file will be modified in place. *Make a backup if needed.*
- Supported image types: JPEG, PNG.
