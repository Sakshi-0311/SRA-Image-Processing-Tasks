

# SRA - Image Processing Tasks
## Tables of Contents
  * [About](#about)
  * [Task 1](#task-1-image-rotation)
  * [Task 2](#task-2)
  * [Task 3](#task-3) 
  * [Task 4](#task-4)
  * [Task 5](#task-5) 
  * [Task 6](#task-6) 
   
## About
All the tasks are performed using libraries such as Numpy and Pillow, without using other inbuilt functions from libraries like Open-CV.        

## Task 1- Image Rotation :

Rotating the given image by various angles without the use of inbuilt rotate functions of numpy, PIL or OpenCV. 

### Rotation Matrix:
![Rotation Matrix](https://legacy.voteview.com/images/homework_1_1_18_2011.jpg)
Original image                     |  Result After Rotation(45 degrees)
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Image%20Rotation/rotate.png">|<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Image%20Rotation/Rotated-Image.png">
   
## Task 2 - Applying Kernels :

### Blurring An Image
Blurring the image with 5x5 kernels. Box-Blur and Gaussian Blur Kernels are used.   

 Original image  | Box Blur  | Gaussian Blur 
:-----:|:-----:|:-----:
<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/blur.jpeg">|<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/Box-Blur%20Parliament.jpg">|<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/Gaussian-Blur%20Parliament.jpg">    

 Original image  | Box Blur  | Gaussian Blur 
:-----:|:-----:|:-----:
<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/filter.png">|<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/Box-Blur.jpg">|<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/Gaussian-Blur.jpg"> 


 ### Sharpening Image
 Sharpening the image with 5x5 kernel.
 Original Image                     |  Sharpened Image
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/blur.jpeg">|<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/Sharp%20Parliament.jpg">

 Original Image                     |  Sharpened Image
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/filter.png">|<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Applying%20Kernels/Sharp%20Lena.jpg">

## Task 3 - Edge Detection :

Edge Detection done using 3x3 kernels.
 Original Image  | Vertical Edge Detection  | Horizontal Edge Detection
:-----:|:-----:|:-----:
<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/edge-detection2.jpg">|<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Vertical%20Edge%20Detection-Cube.jpg">|<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Horizontal%20Edge%20Detection-Cube.jpg">
  **Sobel Edge Detection**  | **Canny Edge Detection**
<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Sobel%20Edge%20Detection-Cube.jpg">|<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Canny%20Edge%20Detection-Cube.jpg">

 Original Image  | Vertical Edge Detection  | Horizontal Edge Detection
:-----:|:-----:|:-----:
<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/edge-detection.png">|<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Vertical%20Edge%20Detection-Dog.jpg">|<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Horizontal%20Edge%20Detection-Dog.jpg">
  **Sobel Edge Detection**  | **Canny Edge Detection**
<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Sobel%20Edge%20Detection-Dog.jpg">|<img width="340" height="340" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Edge%20Detection/Canny%20Edge%20Detection-Dog.jpg">

## Task 4 - Morphology :
### Erosion and Dilation 
 Original Image  | Erosion  | Dilation  
 :-----:|:-----:|:-----:|
 <img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Dilation%20and%20Erosion/morphological.png">|<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Dilation%20and%20Erosion/Erosion.png">|<img width="240" height="300" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Dilation%20and%20Erosion/Dilation.jpg">
 
 
## Task 5 - Masking :
Input Image                     |  Blue Ball Detection
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Masking/mask.jpg">|<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/Masking/Masked%20Image.jpg">

## Task 6 - ROI
### Region of Interest extraction
Input Image                     |  Output Image
:-------------------------:|:-------------------------:
<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/ROI/roi.jpg">|<img width="640" height="450" src="https://github.com/Sakshi-0311/SRA-Image-Processing-Tasks/blob/master/ROI/ROI-Result.jpeg">