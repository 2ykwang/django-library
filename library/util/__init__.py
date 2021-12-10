import os
from uuid import uuid4


def rename_imagefile_to_uuid(instance, filename):
    ext = filename.split(".")[-1]
    uuid = uuid4().hex

    if instance:
        filename = "{}_{}.{}".format(uuid, instance, ext)
    else:
        filename = "{}.{}".format(uuid, ext)

    return filename
