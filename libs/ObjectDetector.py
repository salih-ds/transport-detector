import cv2
import numpy as np

class ObjectDetector():
    def __init__(self):
        pass

    # read image in opencv, convert to rgb
    def open_image(self, path, file_name):
        # read image
        image_bgr = cv2.imread(f'{path}/{file_name}')
        # BGR to RGB
        image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

        return image_bgr, image

    # predict array with labels, boxes, scores for all object in image
    def predict(self, labels, model, image):
        # Inference
        results = model([image], size=640)

        # save inference info
        result_info = results.pandas().xyxy[0]

        # Processing outputs
        boxes = result_info[['xmin', 'ymin', 'xmax', 'ymax']]
        scores = result_info[['confidence']]
        classes = np.array(result_info[['class']]).astype('int').T[0]

        pred_labels = [labels[i] for i in classes]
        pred_boxes = np.array(boxes).astype('int')
        pred_scores = list(np.array(scores).astype('float').T[0])

        return pred_labels, pred_boxes, pred_scores

    # Putting the boxes and labels on the image, add count objects
    def put_box_label_count(self, pred_scores, pred_boxes, pred_labels, image_bgr, font, counter, num):
        for score, (xmin, ymin, xmax, ymax), label in zip(pred_scores, pred_boxes, pred_labels):
            # threshold
            if score < 0.5:
                continue

            # add label and border for object in image
            res_txt = f'{label}: {int(100 * round(score, 2))}%'
            cv2.rectangle(image_bgr, (xmin, ymax), (xmax, ymin), (0, 255, 0), 2)
            cv2.putText(image_bgr, res_txt, (xmin, ymax - 10), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # calculate objects in image
            counter[label][num] += 1

        return image_bgr

    # save image in output directory
    def save_img(self, directory, file_name, image_bgr):
        cv2.imwrite(f'output/{directory}/{file_name}', image_bgr)