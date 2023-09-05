import magic
from django.core.exceptions import ValidationError


def validate_file_mimetype(file):
    accept = ['audio/mpeg', 'audio/x-wav', 'audio/x-m4a', 'audio/mp4', 'audio/ogg', 'audio/flac', 'application/octet-stream']
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in accept:
        raise ValidationError(f'File type {file_mime_type} not supported')
