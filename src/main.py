# Imports
from io import BytesIO

import requests
from PIL import Image


# Functions
def extract_and_print_data(image, exif_tags):
    """
    Extracts and prints formatted EXIF data from an image based on the provided tags.
    Improves readability by formatting binary values and skipping empty categories.

    Args:
        image (Image.Image): Image object to extract EXIF data from.
        exif_tags (dict): Dictionary mapping categories to their relevant EXIF tags.
    """
    exif_data = image._getexif()

    if not exif_data:
        print("""
              No EXIF data found in the image.
              Note that if the photo is from social media platforms,
              they often remove EXIF data during the upload process
              for privacy and data compression reasons.
              """)
        return

    def print_decoded_exif(name, value):
        """Prints EXIF data in a readable format."""
        if isinstance(value, bytes):
            try:
                value = value.decode()
            except UnicodeDecodeError:
                value = str(value)

        print(f"  → {name}: {value}")

    if exif_data is not None:
        # Print categories if they're not empty
        for category, tags in exif_tags.items():
            if any(tag in exif_data for tag in tags.values()):
                print(f"\n{category.upper()}")
                # Print names and values for each tag
                for name, tag in tags.items():
                    if tag in exif_data:
                        print_decoded_exif(name, exif_data[tag])


def get_image(url):
    """
    Attempts to download an image from a URL and open it as a PIL Image object.
    Handles various exceptions related to network issues and image file errors.

    Args:
        url (str): URL of the image to be downloaded.

    Returns:
        Image.Image or str: PIL Image object if successful, otherwise an error message.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))

    except requests.RequestException as e:
        return f"Error downloading the image: {e}"
    except IOError as e:
        return f"Error opening the image: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def main():
    """
    Main function to handle user input and display EXIF data of an image.
    """
    url = input("Image URL (e.g. www.example.com/image.png): ")
    image = get_image(url)

    # If the image variable contains an Image object
    if isinstance(image, Image.Image):
        # Dictionary of EXIF tags and their correspondences
        exif_tags = {
            "General Informations": {
                "ImageWidth": 256,
                "ImageLength": 257,
                "BitsPerSample": 258,
                "Compression": 259,
                "PhotometricInterpretation": 262,
                "ImageDescription": 270,
                "Make": 271,
                "Model": 272,
                "StripOffsets": 273,
                "Orientation": 274,
                "SamplesPerPixel": 277,
                "RowsPerStrip": 278,
                "StripByteCounts": 279,
                "XResolution": 282,
                "YResolution": 283,
                "PlanarConfiguration": 284,
                "ResolutionUnit": 296,
                "TransferFunction": 301,
                "Software": 305,
                "DateTime": 306,
                "Artist": 315,
                "WhitePoint": 318,
                "PrimaryChromaticities": 319,
                "JPEGInterchangeFormat": 513,
                "JPEGInterchangeFormatLength": 514,
                "YCbCrCoefficients": 529,
                "YCbCrSubSampling": 530,
                "YCbCrPositioning": 531,
                "ReferenceBlackWhite": 532,
                "Copyright": 33432
            },
            "Camera Settings": {
                "ExposureTime": 33434,
                "FNumber": 33437,
                "ExposureProgram": 34850,
                "SpectralSensitivity": 34852,
                "ISOSpeedRatings": 34855,
                "OECF": 34856,
                "ExifVersion": 36864,
                "DateTimeOriginal": 36867,
                "DateTimeDigitized": 36868,
                "ComponentsConfiguration": 37121,
                "CompressedBitsPerPixel": 37122,
                "ShutterSpeedValue": 37377,
                "ApertureValue": 37378,
                "BrightnessValue": 37379,
                "ExposureBiasValue": 37380,
                "MaxApertureValue": 37381,
                "SubjectDistance": 37382,
                "MeteringMode": 37383,
                "LightSource": 37384,
                "Flash": 37385,
                "FocalLength": 37386,
                "SubjectArea": 37396,
                "MakerNote": 37500,
                "UserComment": 37510,
                "SubsecTime": 37520,
                "SubsecTimeOriginal": 37521,
                "SubsecTimeDigitized": 37522,
                "FlashpixVersion": 40960,
                "ColorSpace": 40961,
                "PixelXDimension": 40962,
                "PixelYDimension": 40963,
                "RelatedSoundFile": 40964,
                "FlashEnergy": 41483,
                "SpatialFrequencyResponse": 41484,
                "FocalPlaneXResolution": 41486,
                "FocalPlaneYResolution": 41487,
                "FocalPlaneResolutionUnit": 41488,
                "SubjectLocation": 41492,
                "ExposureIndex": 41493,
                "SensingMethod": 41495,
                "FileSource": 41728,
                "SceneType": 41729,
                "CFAPattern": 41730,
                "CustomRendered": 41985,
                "ExposureMode": 41986,
                "WhiteBalance": 41987,
                "DigitalZoomRatio": 41988,
                "FocalLengthIn35mmFilm": 41989,
                "SceneCaptureType": 41990,
                "GainControl": 41991,
                "Contrast": 41992,
                "Saturation": 41993,
                "Sharpness": 41994,
                "DeviceSettingDescription": 41995,
                "SubjectDistanceRange": 41996,
                "LensSpecification": 42034,
                "LensMake": 42035,
                "LensModel": 42036,
                "LensSerialNumber": 42037
            },
            "GPS Information": {
                "GPSVersionID": 0,
                "GPSLatitudeRef": 1,
                "GPSLatitude": 2,
                "GPSLongitudeRef": 3,
                "GPSLongitude": 4,
                "GPSAltitudeRef": 5,
                "GPSAltitude": 6,
                "GPSTimeStamp": 7,
                "GPSSatellites": 8,
                "GPSStatus": 9,
                "GPSMeasureMode": 10,
                "GPSDOP": 11,
                "GPSSpeedRef": 12,
                "GPSSpeed": 13,
                "GPSTrackRef": 14,
                "GPSTrack": 15,
                "GPSImgDirectionRef": 16,
                "GPSImgDirection": 17,
                "GPSMapDatum": 18,
                "GPSDestLatitudeRef": 19,
                "GPSDestLatitude": 20,
                "GPSDestLongitudeRef": 21,
                "GPSDestLongitude": 22,
                "GPSDestBearingRef": 23,
                "GPSDestBearing": 24,
                "GPSDestDistanceRef": 25,
                "GPSDestDistance": 26,
                "GPSProcessingMethod": 27,
                "GPSAreaInformation": 28,
                "GPSDateStamp": 29,
                "GPSDifferential": 30
            },
            "Miscellaneous Information": {
                "ImageUniqueID": 42016,
                "CameraOwnerName": 42032,
                "BodySerialNumber": 42033,
                "Gamma": 42240
            },
            "Thumbnail Settings": {
                "ThumbnailImageWidth": 256,
                "ThumbnailImageLength": 257,
                "ThumbnailBitsPerSample": 258,
                "ThumbnailCompression": 259,
                "ThumbnailPhotometricInterpretation": 262,
                "ThumbnailImageDescription": 270,
                "ThumbnailMake": 271,
                "ThumbnailModel": 272,
                "ThumbnailStripOffsets": 273,
                "ThumbnailOrientation": 274,
                "ThumbnailSamplesPerPixel": 277,
                "ThumbnailRowsPerStrip": 278,
                "ThumbnailStripByteCounts": 279,
                "ThumbnailXResolution": 282,
                "ThumbnailYResolution": 283,
                "ThumbnailPlanarConfiguration": 284,
                "ThumbnailResolutionUnit": 296,
                "ThumbnailTransferFunction": 301,
                "ThumbnailSoftware": 305,
                "ThumbnailDateTime": 306,
                "ThumbnailArtist": 315,
                "ThumbnailWhitePoint": 318,
                "ThumbnailPrimaryChromaticities": 319,
                "ThumbnailJPEGInterchangeFormat": 513,
                "ThumbnailJPEGInterchangeFormatLength": 514,
                "ThumbnailYCbCrCoefficients": 529,
                "ThumbnailYCbCrSubSampling": 530,
                "ThumbnailYCbCrPositioning": 531,
                "ThumbnailReferenceBlackWhite": 532,
                "ThumbnailCopyright": 33432
            },
            "Additional Information": {
                "InteroperabilityIndex": 1,
                "InteroperabilityVersion": 2,
                "RelatedImageFileFormat": 4096,
                "RelatedImageWidth": 4097,
                "RelatedImageLength": 4098
            }
        }

        extract_and_print_data(image, exif_tags)
    else:
        print(image)


# Main
if __name__ == "__main__":
    main()
