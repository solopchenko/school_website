import uuid

def get_slide_upload_to(isinstance, filename):
    return "pages/{0}/slider/{1}".format(isinstance.page.pk, generate_random_filename(filename))

def generate_random_filename(filename):
    f_name = uuid.uuid4()
    f_extension = filename.split('.')[-1]
    return "{0}.{1}".format(f_name, f_extension)
