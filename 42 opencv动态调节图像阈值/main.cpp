#include <iostream>  
#include <opencv/cv.hpp>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  

using namespace std;
using namespace cv;
Mat img;
//定义了窗体名  
string winName = "二值化";

//TrackBar发生改变的回调函数  
void onChangeTrackBar(int pos, void* userdata);

//主函数  
int main()
{
    //trackbar名  
    string trackBarName = "pos";
    //图像文件名  
    string imgName = "./red.png";
    //trackbar的值  
    int posTrackBar = 0;
    //trackbar的最大值  
    int maxValue = 255;


    //读入图像，以灰度图形式读入  
    img = imread(imgName);
	vector<Mat> imgChannels;
  	split(img, imgChannels);
	img = imgChannels[2] - imgChannels[0];
	//threshold(img, img, 100, 255, CV_THRESH_BINARY);
    //新建窗口  
    namedWindow(winName);
    imshow(winName, img);
    //创建trackbar，我们把img作为数据传进回调函数中  
    createTrackbar(trackBarName, winName, &posTrackBar, maxValue, onChangeTrackBar);

    waitKey();
    return 0;
}

// 回调函数  
void onChangeTrackBar(int pos, void* usrdata)
{
    Mat src = img;
    Mat dst;
    // 二值化
    threshold(src, dst, pos, 255, 0);
    imshow(winName, dst);
}
