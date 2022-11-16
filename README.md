# transport-detector
Transport detection on the image pool with custom detector and counter recording

<a href="https://github.com/ultralytics/yolov5">Yolo v5</a> is used as a detector, retrained on the data <a href="https://public.roboflow.com/object-detection/vehicles-openimages">"Vehicles-OpenImages Dataset"</a>

In <a href="https://colab.research.google.com/drive/1eij2D9IpWwU6bSCwWpUbtXrDIjw0tL7p?usp=sharing">this notebook</a> I improve models and upload updated <a href='https://drive.google.com/drive/folders/1EdQ-blIAN6rrLDBNpHItF6oj9JyIjqyH?usp=sharing'>models and weights</a>

## Install
Python 3.7.7

Need to clone yolo v5 and load required modules

    git clone https://github.com/ultralytics/yolov5  # clone
    cd yolov5
    pip install -r requirements.txt  # install

Added base weights for YOLOv5s to the "trained_weights" directory. To use the latest versions, you need to <a href='https://drive.google.com/drive/folders/1EdQ-blIAN6rrLDBNpHItF6oj9JyIjqyH?usp=sharing'>download the weights</a> and add them to the "trained_weights" directory - replace the base weights for YOLOv5s with the new one.

## Instruction
1. Add a folder with your images to the "img" directory or you can use test images in "test" folder
2. Run "main.py" in terminal
3. In the terminal select the version of yolo "s" or "m" and press Enter (only "s" basic is available by default). To use the retrained "s" or "m" load the weights according to the instructions in the "Install"
4. Specify the name of the folder in the "img" directory in which the images are stored and press Enter (to use test data, specify "test")
5. A folder with the name specified in the step above will appear in the "output" directory. Images with boxes and labels and a table in csv format with object counters for each image will be added to the folder

If the folder specified in step 4 already exists in the "output" directory, then you will get an error






