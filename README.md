Documentation 

1. **Introduction** 

This script utilizes the MediaPipe library for face landmark detection to analyze stress-related features in a video. It calculates stress levels based on factors such as blink patterns, eyebrow movements, and lip movements. 

2. **Installation** 

To install the required Python libraries for this script, you can use the following command in your terminal or command prompt: 

`pip install -r requirements.txt`

3. **Usage** 

To use the script, you can replace the "video.mp4" with the path to your desired input video.  

`input_video_path = "video.mp4"`

The stress data will be saved in the “output/stress\_data.json" file. Adjustments to the stress calculation logic or output format can be made as needed. 

`python main.py`

4. **Code Overview** 
1. **Reference** 

All the landmarks indexes are brought for the image provided by MediaPipe. 

[https://storage.googleapis.com/mediapipe- assets/documentation/mediapipe_face_landmark_fullsize.png ](https://storage.googleapis.com/mediapipe-assets/documentation/mediapipe_face_landmark_fullsize.png)

2. **Imported Libraries** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.004.png)

**cv2 (OpenCV):** Handles video input and facilitates advanced image processing. 

**Mediapipe**: Provides powerful face detection with predefined landmark recognition models. 

**JSON:** Utilized for storing processed stress data in JSON format 

3. **MediaPipe Model Initialization** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.005.png)

**mp\_face\_mesh:** Initializes the MediaPipe Face Mesh model for precise facial landmark detection. 

4. **Eye Aspect Ratio (EAR) Calculation:** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.006.jpeg)

**eye\_aspect\_ratio:** Computing the Eye Aspect Ratio (EAR) is crucial for blink detection, utilizing specific landmarks for each eye. It calculates the distance between the top and bottom of the eye for each one. 

5. **Blink Stress Calculation:** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.007.png)

**calculate\_blink\_stress:** Determines blink stress based on the EAR. 

6. **Eyebrow Displacement and Stress Calculation:** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.008.jpeg)

**calculate\_eyebrow\_stress:** Measures eyebrow displacement for stress assessment. 

**calculate\_eyebrow\_displacement:** Computes the average vertical displacement of both eyebrows landmarks. 

7. **Lip Movement Stress Calculation:** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.009.jpeg)

**calculate\_lip\_stress:** calculates the stress related to the lip movement by measuring the vertical distance between upper and lower lip landmarks. 

8. **Stress Aggregation:** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.010.png)

**calculate\_stress:** Combines the factors related to blink, eyebrow, and lip movement to derive an overall stress level. 

9. **Video Processing and Stress Data Generation:** 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.011.jpeg)

**process\_video:** Processes each frame of a video, utilizing the defined stress calculation components. 

The resulting data includes frame number, blink stress, eyebrow stress, lip stress, and final stress, stored in a dictionary. 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.012.png)

Then dumping the resulting data in a JSON file. 

![](Aspose.Words.207c4370-100b-494a-b2c9-b7ef6b7e6589.013.png)
