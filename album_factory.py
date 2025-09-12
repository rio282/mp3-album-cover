import eyed3
from eyed3.id3.frames import ImageFrame
import mimetypes


def make(mp3_filepath: str, cover_image_filepath: str) -> bool:
    try:
        # load mp3
        audio_file = eyed3.load(mp3_filepath)
        if audio_file.tag is None:
            audio_file.initTag()

        # load cover image
        cover_image = open(cover_image_filepath, "rb")
        cover_image_bytes = cover_image.read()
        mimetype, _ = mimetypes.guess_type(cover_image_filepath)
        if mimetype is None:
            raise OSError("Couldn't guess mimetype for cover image")

        # set & save cover image to mp3 file
        audio_file.tag.images.set(ImageFrame.FRONT_COVER, cover_image_bytes, mimetype)
        audio_file.tag.save(version=eyed3.id3.ID3_V2_3)

        return True
    except FileNotFoundError:
        return False
    except OSError:
        return False
