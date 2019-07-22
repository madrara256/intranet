import getpass
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.conf import settings
from django.utils import timezone
import os
import glob
import traceback
from documents.models import *

class Command(BaseCommand):
	help = "This Command enables batch upload of images\n Type upload_images path_to_image_folder]"

	def upload_batch(self, path, tag):
		try:
			print("This is Path: %s" % path)
			print("This is Tag: %s" % tag)
			image_tag = ImageTag.objects.all().filter(tag_name__exact=tag)[:1]
			image_tag_object = None
			if image_tag:
				print("This is Tag: %s" % list(image_tag))
				for tag in list(image_tag):
					image_tag_object = tag
				print("The Tag Object: %s" % image_tag_object)
				# Traverse to folder
				# Programatically Upload Images to django
				image_list = glob.glob(path+"/*.JPG")
				print("The Image List: %s" % image_list)
				if image_tag_object is not None:
					# image_gallery = ImageGallery(image_tag=image_tag_object)
					# image_gallery.image.save('MIK3631.JPG', File(open('/home/sedward/LUGOGO-14TH-OCT-2018/_MIK3631.JPG', 'r')))
					for item in image_list:
						image_gallery = ImageGallery(image_tag=image_tag_object)
						image_gallery.image.save(str(os.path.basename(item)), File(open(item, 'rb')))
			else:
				print("Please Enter Valid Tag Name.")
		except Exception as e:
			print("Error Occured")
			print(str(e))
			traceback.print_exc()

	def add_arguments(self, parser):
		parser.add_argument('-p','--path', type=str, help='Path to the Image Folder')

		# Optional Argument -- not in this case
		parser.add_argument('-t', '--tag', type=str, help='Tag for the Image when stored')

	def handle(self, *args, **kwargs):
		time = timezone.now().strftime('%X')
		self.stdout.write(self.style.SUCCESS("Time Started Task: %s" % time))
		path = kwargs['path']
		tag = kwargs['tag']
		if path and tag:
			self.upload_batch(path, tag)
		else:
			self.stdout.write(self.style.ERROR("Please specify the path to image folder and tag e.g \nupload_images --path /path/to/image/folder --tag sports event"))
		self.stdout.write(self.style.SUCCESS("Time Ended Task: %s" % time))