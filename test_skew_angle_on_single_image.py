from graphics_service import GraphicsService
from deskew_service import DeskewService

# We can analyze how skew angle calculation works and debug each step on a given image
imageCv = GraphicsService().openImageCv('../sample-images/dataset/li_+6.63.png')
angle = DeskewService().getSkewAngle(imageCv, debug=True)
print('Found angle', angle)
