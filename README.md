# UDEMY EĞİTİMLERİM

## Udemy Üzerinde yayınlamakta olduğum eğitimlerime aşadağıdaki indirim kuponlarını kullanarak ulaşabilirsiniz.

## Temel ROS Eğitimi

### [Udemy - Temel ROS Eğitimi İndirim Kuponu](https://www.udemy.com/temel-ros-egitimi/?couponCode=2018_ROS)

### [Kursun Tanıtım Videosu](https://youtu.be/K92_CLqbFT4)

## ROS - Urdf ve Xacro ile Robot Modelleme

### [Udemy - ROS - Urdf ve Xacro ile Robot Modelleme Eğitimi İndirim Kuponu](https://www.udemy.com/ros-ile-robot-modelleme/?couponCode=ROSXACRO)


# Paket-Kurulumları

## CUDA 9.0 KURULUMU

https://developer.nvidia.com/cuda-90-download-archive

adresinden cuda paketi indirilir. (Linux>x86_64>Ubuntu>16.04>deb(local))

	sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb
	sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub
	sudo apt-get update
	sudo apt-get install cuda

Komutları ile kurulum tamamlanır.

.bashrc dosyasına `export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}` satırı eklenir.

Referans Link:

https://github.com/earcz/NVIDIA-GPU-Surucusu-ve-CUDA-Yukleme/wiki/CUDA-Yukleme

## cuDNN 7.1.4 KURULUMU

https://developer.nvidia.com/rdp/cudnn-download

**Metod 1:** cuDNN v7.1.4 Library for Linux	Paketi indirilir.

indirilen paket açılır.

	tar -xzvf cudnn-9.0-linux-x64-v7.1.tgz
	
gerekli paketler cuda dizinine kopyalanır.

	sudo cp cuda/include/cudnn.h /usr/local/cuda/include
	sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
	sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

**Metod 2:** Cudnn Debian dosyaları ile kurulum için;

cuDNN v7.1.4 Runtime Library for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn7_7.1.4.18-1+cuda9.0_amd64.deb

cuDNN v7.1.4 Developer Library for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn7-dev_7.1.4.18-1+cuda9.0_amd64.deb 

cuDNN v7.1.4 Code Samples and User Guide for Ubuntu16.04 (Deb)

	sudo dpkg -i libcudnn7-doc_7.1.4.18-1+cuda9.0_amd64.deb


Referans Link:

http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html
## TensorFlow KURULUMU

python 2.7 için paket kurulumu

	sudo apt-get install python-pip			(pip kurulu değil ise önce pip kurulumu yapılır.)
	sudo pip2 install tensorflow-gpu		-gpu için
	sudo pip2 install tensorflow			-cpu için

python 3.5+ için paket kurulumu

	sudo apt-get install python3-pip		(pip kurulu değil ise önce pip kurulumu yapılır.)
	sudo pip3 install tensorflow-gpu		-gpu için
	sudo pip3 install tensorflow			-cpu için

Referans Link:

https://www.tensorflow.org/install/install_linux

## KERAS KURULUMU

python 2.7 için paket kurulumu
	
	sudo pip2 install keras

python 3.5+ için paket kurulumu
	
	sudo pip3 install keras

Referans Link:

https://keras.io/

## ZED KAMERA SDK KURULUMU

https://www.stereolabs.com/developers/ Adresinden işletim sistemimize uygun sdk dosyası indirilir. sdk indirilirken kurulu olan CUDA sürümüne dikkat edilmelidir.

indirilen pakete çalışma izni verilir.

	sudo chmod +x ZED_SDK_Linux_Ubuntu16_CUDA9_v2.5.1.run
	
indirilen paket çalıştırılarak kurulum tamamlanır.

	./ZED_SDK_Linux_Ubuntu16_CUDA9_v2.5.1.run
	
	
## ROS KİNETİC KURULUMU

	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

	sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

	sudo apt-get update


	sudo apt-get install ros-kinetic-desktop-full


	sudo rosdep init
	rosdep update


	echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
	source ~/.bashrc
	source /opt/ros/kinetic/setup.bash

	sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential

Referans Link:

http://wiki.ros.org/kinetic/Installation/Ubuntu

## OPENCV KURULUMU

#### ROS Kinetic ile birlikte opencv3.2 sürümü kurulu olarak geldiği için opencv kurulumu yapmaya gerek yoktur. python 2.7 de opencv direk import edilebilir.

Kurulum yapmak isteyenler için;

### Metod1:
	sudo apt-get install python-opencv
Komut ile Opencv Kurulması Halinde Linux'ta kamera fonksiyonu çalışmayacaktır.

python3 için opencv Kurulumu sadece aşağıdaki satır kullanılarak yapılabilir.

	pip3 install opencv-python
### Metod2:
	sudo apt-get update
	sudo apt-get upgrade

	sudo apt-get install build-essential cmake git pkg-config
	sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev	

*eğer libtiff4-dev kütüphanesi bulunamazsa bunun yerine libtiff5-dev kullanılabilir.*

	sudo apt-get install libgtk2.0-dev libgtk-3-dev
	sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
	sudo apt-get install libxvidcore-dev libx264-dev



	sudo apt-get install libatlas-base-dev gfortran
	sudo apt-get install python2.7-dev python3.5-dev



	cd ~
	wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.3.0.zip
	unzip opencv.zip
	
	wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.3.0.zip
	unzip opencv_contrib.zip



	sudo apt-get install python-pip
	sudo pip install numpy



	sudo pip install virtualenv virtualenvwrapper
	
	export WORKON_HOME=$HOME/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh
	
	echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
	echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
	
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
	source ~/.bashrc

	mkvirtualenv cv -p python2



	workon cv
	cd ~/opencv-3.3.0/
	mkdir build
	cd build

	cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.3.0/modules \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
	-D BUILD_EXAMPLES=ON ..



	make -j4
	sudo make install
	sudo ldconfig



	cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
	ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

*Eğer /usr/local/lib/python2.7/site-packages/ konumu boşsa aşağıdaki satır kullanılmalıdır.*

	ln -s /usr/local/lib/python2.7/dist-packages/cv2.so cv2.so

Kurulum tamamlandı.

	python
	>>> import cv2
	>>> cv2.__version__
	'3.3.0'

kurulumu kontrol edebiliriz.


*Eğer opencv kurulumu tamamlandı ve kurulan terminalde çalıştığı halde 
yeni açılan terminallerde çalışmıyorsa aşağıdaki işlemler uygulanmalıdır.*

	sudo nano ~/.bashrc
	export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH yada
	export PYTHONPATH=/usr/local/lib/python2.7/dist-packages:$PYTHONPATH 
	.bashrc dosyasına bu satır(cv2.so dosyasının bulunduğu konum) eklenerek kaydedilir.

**Raspberry Pi için;**

	sudo raspi-config
	Advanced Options > Expand Filesystem
	reboot

*Komutları uygulanarak opencv kurulumu için hazır hale getirilir.Eğer görüntü sadece raspberry pi kamera modülünden alınacaksa Metod1 ile, harici kameradan görüntü alınacaksa Metod2 Kullanılarak kurulum tamamlanır.*

Referans Link:

Ubuntu için:

http://pythonopencv.com/install-opencv-3-3-and-python2-7-3-5-bindings-on-ubuntu-16-04/
https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

Raspberry Pi için:

https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/















