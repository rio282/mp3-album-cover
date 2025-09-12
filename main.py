import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from mutagen.mp3 import MP3
from album_factory import make as album_make


class AlbumStitcherApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("MP3 Album Art Stitcher")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.mp3_path = None
        self.image_path = None
        self.image_preview = None

        # mp3 selection
        self.mp3_label = ttk.Label(root, text="No MP3 selected")
        self.mp3_label.pack(pady=5)
        ttk.Button(root, text="Select MP3", command=self.select_mp3).pack(pady=5)

        # image selection
        self.image_label = ttk.Label(root, text="No image selected")
        self.image_label.pack(pady=5)
        ttk.Button(root, text="Select Image", command=self.select_image).pack(pady=5)

        # image preview
        self.preview_label = ttk.Label(root)
        self.preview_label.pack(pady=10)

        # controls
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Stitch", command=self.stitch).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)

    def select_mp3(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if path:
            self.mp3_path = path
            try:
                audio = MP3(path)
                info = f"MP3: {path}\nLength: {audio.info.length:.1f}s, Bitrate: {audio.info.bitrate // 1000} kbps"
                self.mp3_label.config(text=info)
            except Exception as e:
                self.mp3_label.config(text=f"Failed to read MP3: {e}")

    def select_image(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
        if path:
            self.image_path = path
            self.image_label.config(text=f"Image: {path}")

            img = Image.open(path)
            img.thumbnail((120, 120))
            self.image_preview = ImageTk.PhotoImage(img)
            self.preview_label.config(image=self.image_preview)

    def clear(self) -> None:
        self.mp3_path = None
        self.image_path = None
        self.image_preview = None
        self.mp3_label.config(text="No MP3 selected")
        self.image_label.config(text="No image selected")
        self.preview_label.config(image="", text="")

    def stitch(self):
        if not self.mp3_path or not self.image_path:
            messagebox.showerror("Error", "Please select both an MP3 and an image.")
            return

        try:
            success = album_make(self.mp3_path, self.image_path)
            if success:
                messagebox.showinfo("Success", "Image stitched into MP3 successfully!")
            else:
                messagebox.showerror("Error", "Failed to stitch image.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stitch: {e}")


def main():
    root = tk.Tk()
    app = AlbumStitcherApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
