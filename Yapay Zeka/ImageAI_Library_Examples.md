# ImageAI : Object Detection 

ilk olarak ImageAI kütüphanesini kuralım.

    sudo pip3 install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl 
 
ilk örnek için kullanacağımız RetinaNet modelini [indirelim.](https://github-production-release-asset-2e65be.s3.amazonaws.com/125932201/e7ab678c-6146-11e8-85cc-26bc1cd06ab0?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180704%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180704T165345Z&X-Amz-Expires=300&X-Amz-Signature=6d3991922771262f6d1b826823f20b3974e458d023b79db873d5f092c5c0e782&X-Amz-SignedHeaders=host&actor_id=33426517&response-content-disposition=attachment%3B%20filename%3Dresnet50_coco_best_v2.0.1.h5&response-content-type=application%2Foctet-stream)

İndirdiğimiz RetinaNet modelini ImageAI kütüphanesini kullanarak test edelim. 

    gedit FirstDetection.py

    from imageai.Detection import ObjectDetection
    import os

    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "ImageAI_image.jpeg"), output_image_path=os.path.join(execution_path , "ImageAI_imagenew.jpg"))

    for eachObject in detections:
        print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
        
Konumuzu çalıştıralım.

    python FirstDetection.py        

Test Image;

![Test Image](https://github.com/raclab/RACLAB/blob/master/images/AI/ImageAI_image.jpeg)

Sonuç;

![Result_Image](https://github.com/raclab/RACLAB/blob/master/images/AI/ImageAI_imagenew.jpg)

Terminal Çıktısı;
    
    person : 57.20396637916565
    person : 52.57996916770935
    person : 70.81100940704346
    person : 76.99862718582153
    person : 79.40091490745544
    bicycle : 81.03846907615662
    person : 83.66730809211731
    person : 89.41192626953125
    truck : 60.61035990715027
    person : 69.6576476097107
    bus : 97.92420864105225
    truck : 83.9435338973999
    car : 72.50520586967468
    
extract_detected_objects özelliği True yapılarak algılanan her nesnenin ayrı ayrı kaydedilmesi sağlanabilir.

    from imageai.Detection import ObjectDetection
    import os

    execution_path = os.getcwd()


    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()


    detections, objects_path = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "ImageAI_image.jpeg"), output_image_path=os.path.join(execution_path , "image3new.jpg"), extract_detected_objects=True)


    for eachObject, eachObjectPath in zip(detections, objects_path):
        print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
        print("Object's image saved in " + eachObjectPath)
        print("--------------------------------")

Sonuç;

![Bus](https://github.com/raclab/RACLAB/blob/master/images/AI/bus-11.jpg)

detector.CustomObjects Özelliği kullanılarak model içerisinde tanımlı neslerden istediklerimizin tesbit edilmesini sağlayabiliriz.

    from imageai.Detection import ObjectDetection
    import os

    execution_path = os.getcwd()


    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()


    custom_objects = detector.CustomObjects(person=True)
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path , "ImageAI_image.jpeg"), output_image_path=os.path.join(execution_path , "image3custom.jpg"))


    for eachObject in detections:
        print(eachObject["name"] + " : " + eachObject["percentage_probability"] )
        print("--------------------------------")
        
Sonuç;

![custom_images](https://github.com/raclab/RACLAB/blob/master/images/AI/image3custom.jpg)

detection_speed ile modelin çalışma hızını değiştirebiliriz. "normal"(default), "fast", "faster" , "fastest" ve "flash".
Modelin çalışma hızı artığında algılama oranında düşüş yaşanacaktır.

    detector.loadModel(detection_speed="fastest")

Son örnekte  yukarıdaki satır düzenlenip tekrar çalıştırılırsa;    

![fastest](https://github.com/raclab/RACLAB/blob/master/images/AI/image3_fastest.jpg)

Referans Link;

https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection

# ImageAI : Video Object Detection

Video üzerinde object detection uygulayabiliriz. image object detection bölümünde uyguladıklarımızın benzerlerini burda da uygulamak mümkündür.

Test için bir video [indirelim.](https://raw.githubusercontent.com/OlafenwaMoses/ImageAI/master/videos/traffic.mp4)

    from imageai.Detection import VideoObjectDetection
    import os

    execution_path = os.getcwd()

    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    custom_objects = detector.CustomObjects(person=True, bicycle=True, motorcycle=True)
    video_path = detector.detectCustomObjectsFromVideo(custom_objects=custom_objects, input_file_path=os.path.join(execution_path, "traffic.mp4"),
                                    output_file_path=os.path.join(execution_path, "traffic_custom_detected")
                                    , frames_per_second=20, log_progress=True)
    print(video_path)

Sonuç;

[![Sonuc](https://raw.githubusercontent.com/OlafenwaMoses/ImageAI/master/images/video-4.jpg)](https://www.youtube.com/embed/S-jgBTQgbd4?rel=0)

Referas Link;

https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/VIDEO.md
