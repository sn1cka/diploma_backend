import random
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from autofixture import AutoFixture, register
from autofixture.generators import ImageGenerator
from django.core.files import File

from api.models import Tour, TourPhoto


def get_placeholder_image(width, height):
	image_url = f'https://picsum.photos/{width}/{height}'
	img_temp = NamedTemporaryFile(delete=True)
	img_temp.write(urlopen(image_url).read())
	img_temp.flush()

	return File(img_temp)


class MyImageGenerator(ImageGenerator):
	default_sizes = (
		(600, 600),
		(1280, 1024),
		(400, 600),
	)

	def generate(self):
		width, height = random.choice(self.sizes)
		i = 0
		path = self.generate_file_path(width, height)

		while self.storage.exists(path):
			i += 1
			path = self.generate_file_path(width, height, '_{0}'.format(i))

		return self.storage.save(
			path,
			get_placeholder_image(width, height)
		)


class PhotoAutoFixture(AutoFixture):
	field_values = {
		'photo': MyImageGenerator(),
	}


register(Tour, PhotoAutoFixture)
register(TourPhoto, PhotoAutoFixture)
