from rest_framework.exceptions import ValidationError


def get_extension(extension):
    parts = extension.split(".")
    if len(parts) < 2:
        raise ValidationError({"error": "File has no extension"})
    return parts[-1]
