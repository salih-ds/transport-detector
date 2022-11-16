import cv2
import torch

from libs.DialogWindow import DialogWindow
from libs.Files import Files
from libs.ObjectCounter import ObjectCounter
from libs.ObjectDetector import ObjectDetector

# detection labels
labels = ['Ambulance', 'Bus', 'Car', 'Motorcycle', 'Truck']

# font for text
font = cv2.FONT_HERSHEY_SIMPLEX

# select model version and path directory with images
model_v, directory, path = DialogWindow().select_settings()

# Model
model = torch.hub.load('yolov5', 'custom', path=f'trained_weights/best_yolo5{model_v}_half_freeze.pt', source='local')

# list of image names
files = Files().image_list(path)

# create a directory where to save the results
Files().create_res_dir(directory)

# create counter dataframe
counter = ObjectCounter().counter_template(labels, files)

# bypass all files, detect objects and write to table, save images with borders
for num, f in enumerate(files):

    # read image in opencv, convert to rgb
    image_bgr, image = ObjectDetector().open_image(path, f)

    # predict array with labels, boxes, scores for all object in image
    pred_labels, pred_boxes, pred_scores = ObjectDetector().predict(labels, model, image)

    # add image name to table
    ObjectCounter().add_name(counter, num, f)

    # Putting the boxes and labels on the image, add count objects
    image_bgr = ObjectDetector().put_box_label_count(pred_scores, pred_boxes, pred_labels, image_bgr, font, counter, num)

    # save image in output directory
    ObjectDetector().save_img(directory, f, image_bgr)

# save info table to csv
ObjectCounter().save(counter, directory)

# last info about output
DialogWindow().ready(directory)