import os
import numpy as np
import random
import cv2

folder0 = '../images/opencv_flowers'


def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def create_new_images():
    project_images = load_images(folder0)
    resized_images = []
    rotflip_images = []
    final_images = []

    for image in project_images:
        new_image = cv2.resize(image, (500, 500))
        resized_images.append(new_image)

    for index, image in enumerate(resized_images):
        if index % 2 == 0:
            rot_image = cv2.rotate(image, cv2.cv2.ROTATE_180)
            if index % 4 == 0:
                new_image = cv2.flip(rot_image, 1)
            else:
                new_image = rot_image
            rotflip_images.append(new_image)
        else:
            rot_image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
            if index % 3 == 0:
                new_image = cv2.flip(rot_image, -1)
            else:
                new_image = rot_image
            rotflip_images.append(new_image)

    for image in rotflip_images:
        blanks = np.zeros(image.shape[:2], dtype='uint8')
        blur_img = cv2.GaussianBlur(image, (3, 3), cv2.BORDER_DEFAULT)
        b, g, r = cv2.split(blur_img)
        # colors = ['b', 'g', 'r']
        # color = random.choice(colors) we originally had randomized color channels for final images.

        color_merge = cv2.merge([b, blanks, blanks])
        final_images.append(color_merge)

    return final_images


def show_save_images(images):
    # path = '../images/altered_flowers/alt_red'
    path = '../images/altered_flowers/alt_blue'
    # path = '../images/altered_flowers/alt_purple'
    i = 0

    for img in images:
        # show the image
        window = 'Image ' + str(i)
        cv2.imshow(window, img)
        cv2.waitKey(0)
        i += 1

        # save the image
        cv2.imwrite(os.path.join(path, window + '.jpg'), img)


if __name__ == '__main__':
    final_works = create_new_images()
    show_save_images(final_works)
