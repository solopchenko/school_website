import uuid

def get_user_profile_photo_upload_to(isinstance, filename):
    return "staff/{0}/{1}".format(isinstance.login.username, generate_random_filename(filename))

def generate_random_filename(filename):
    f_name = uuid.uuid4()
    f_extension = filename.split('.')[-1]
    return "{0}.{1}".format(f_name, f_extension)
