# pennapps-xv-project
Lookup full images given a rough initial sketch.

## Usage
To open gui and draw
```
$ python start.py
```
Add the `-h` flag for more details on usage.


## Creating Pickled Data
Usage of this program requires preprocessing of the images located in the `images/` directory.
These images cna be preprocessed using the `resizer.py` script. Add the `-h` flag for usage.


### Implementation
From a high level perspective, the program works by feeding a rough sketch of an image drawn by the user 
into the program and the program attempts to find the closest matches to the image in an existing database 
of images as efficitently as possible. 

### Classifiers
Machine learning is involved to compare the input image to all other images 
in the database. More specifically, a K Nearest Neighbors (KNN) classifier is used to due to simplicity of 
implementation, but other classifiers such as Support Vector Machines (SVM) and Artificial Neural Networks
could be used just as well. 

### Features used
The primary features used for classification were the locations of edges in the 
images. Since th input is just a sketch that would normally be drawn with a stylus on a tablet, really
only 2 colors are used (the brush color and the background). Canny edge detection is performed with OpenCV
and to increase the robustness of the edges and decrease granularity, all pixels surrounding those indicating 
edges (returned by the canny edge detection) were also set to white to indicate the possibility of an edge.

### Optimization
Additionally, since we have a very large database comprised of almost 1000 images, loading them all into memory 
and preprocessing them on startup would be costly in terms of time. All training data in the database is 
processed beforehand and serialized into pickle files to counter this. The only image that is processed for feature 
extraction at runtime is the provided input image.


## Technical Challenges
The primary technical challenge of this project was finding the right features for comparing images. More 
specifically, how could we programatically express images in code space that would allow us to process them 
the quickest using the fewest amount of resources. Since the input image is a basic sketch containing little
color, rgb value were not used as features. We decided to go with edges of each image since those can easily 
be extracted from the input sketch. Additionally, KNN and SVN classifiers were tested based on classification 
performance and runtime usage.


## Tools/Tech Used
- OpenCV
- Numpy
- Scipy
- Scikit Learn 
- Scikit Image


## Accomplishments
- Implementation of various classifiers 
- Functionaly working program


Inspired by SketchIt (https://github.com/njiang/sketchIt)
