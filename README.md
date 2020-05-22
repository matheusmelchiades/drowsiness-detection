# Drowsiness-detection 🤖📷⚠️

Project about Face recognition that detect if the person is sleppy.

You can also read a translated of this file in 
 - [Portuguese](./documents/README_PT.md)

***

This project aims to provide a tool helps drivers, that work a lot time driving, reporting whether he is sleppy or not.

The implementation this algorithm was based in this article ["Real-Time Eye Blink Detection"](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf), where covers how to detect face landmarks and how to mapping the eye position in the face. So with this data, the algorithm can to apply the intelligence to detect wheather the person is sleppy.

This is an example...

![example](./documents/example.gif)

# Requirements

- Python 3.3+

# 📚 Libraries

* [dlib](http://dlib.net/python/index.html) - To detect faces
* [imutils](https://github.com/jrosebr1/imutils) - To handle operations with openCV.
* [numpy](https://numpy.org/) - Provider a package to data easily. 
* [scipy](https://www.scipy.org/) - Library used for scientific computing and technical computing.

# ⚙ How to config?

``` bash
> python -m venv venv
> pip install -r requirements.txt
> source venv/bin/activate
```

# 🚀 How to Run?

It's simple...

``` bash
> python detector.py
```

# 🔗 References

* [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)
* [face recognition](http://krasserm.github.io/2018/02/07/deep-face-recognition/)
* [Face landmarks](https://medium.com/@aanilkayy/extract-eyes-in-face-i%CC%87mages-with-dlib-and-face-landmark-points-c45ef480c1)