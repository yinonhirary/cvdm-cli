import cloudinary
from cloudinary import config
cloudinary.config(
   cloud_name = 'dvrks8kwb',
   api_key = '915168747516145',
   api_secret = '4v9NFePDnH9hPIv3nD0Vgm5oow8'
)


def uploadImg(pic):
   """"
   this function is using in order to upload image file to cloudinary
   """
   json_response = cloudinary.uploader(pic, public_id=pic)
   return json_response