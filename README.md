# OK VITO Project

Facial Recognition and Ok sign detection using popular libraries such as OpenCv, Mediapipe, Tensorflow and SQlite DB.

## Project Structure

```
.
├── dataset/                  # Directory to store face images
├── models/                   # Directory to store pre-trained models
│   ├── haarcascade_frontalface_default.xml
├── 01_create_dataset.py      # Script to capture face images and store in database
├── 02_create_clusters.py     # Script to cluster face images using K-Means and VGG16
├── 03_rearrange_data.py      # Script to rearrange data after clustering
├── 04_train_model.py         # Script to train the LBPH face recognizer model
├── 05_add_ok_column.py       # Script to alter customers table and add ok_sign_detected column
├── 06_test_ok_sign.py        # Script to OK sign detection
├── 07_make_predictions.py    # Script to run face recognition and OK sign detection
├── customer_faces_data.db    # SQLite database to store customer information and face images
└── README.md
```

## Setup

1. Install the required Python packages:

```
pip install opencv-python numpy tensorflow keras scikit-learn mediapipe tqdm
```

2. Download the pre-trained `haarcascade_frontalface_default.xml` model from the OpenCV repository and place it in the `models` directory.


## Notes

- You will need `tensorflow version 2.12.0` and `keras version 2.12.0` with a python version of `3.11.9`

## Samples

![alt text](image.png)

## License

This project is licensed under the [MIT License](LICENSE).