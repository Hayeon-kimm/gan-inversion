# GAN-inversion
# gan-inversion
* 이 세팅은 모두 LAIT2 서버에서 구성되었습니다.
1. 세팅되어진 도커 이미지를 이용하여 컨테이너를 생성한다.
~~~
docker run -it --name [컨테이너 이름] --gpus all -v [git clone한 디렉토리명]:/workspace gan-inversion:latest /bin/bash
~~~
2. pretrained_models 디렉토리를 다음 위치에 생성하고, 모든 모델의 모델을 다운받아서 저장한다. (한꺼번에 저장하는 파일을 생성하려고 했으나 wget 명령어가 제대로 실행되지 않아 따로 id 및 file name 올려드립니다.<br/>

| gan-inversion | Repository root folder |
| ------------ | ---------------------- |
| ├  encoder4editing ||
| ├  PTI ||
| ├  hyperstyle ||
| ├  Dockerfile|Dockerfile for image building(stylegan2-ada) |
| ├  pretrained_models|Folder containing all pretrained_models|

| File name | used for |
| ------------ | ---------------------- |
|[e4e_ffhq_encode.pt](https://drive.google.com/file/d/1cUv_reLE6k3604or78EranS7XzuVMWeO/view) |e4e, PTI, hyperstyle|
|[e4e_cars_encode.pt](https://drive.google.com/file/d/17faPqBce2m1AQeLCLHUVXaDfxMRU2QcV/view) |e4e, hyperstyle|
|[e4e_horse_encode.pt](https://drive.google.com/file/d/1TkLLnuX86B_BMo2ocYD0kX9kWh53rUVX/view) |e4e|
|[e4e_church_encode.pt](https://drive.google.com/file/d/1-L0ZdnQLwtdy6-A_Ccgq5uNJGTqE7qBa/view)|e4e|
|[stylegan2-ffhq-config-f.pt](https://drive.google.com/file/d/1EM87UquaoQmk17Q8d5kYIAHqu0dkYqdT/view)|e4e,PTI|
|[model_ir_se50.pth](https://drive.google.com/file/d/1KW7bjndL3QG3sxBbZxreGHigcCCpsDgn/view)|e4e|
|[moco_v2_800ep_pretrain.pt](https://drive.google.com/file/d/18rLcNGdteX5LwT7sv_F7HWr12HpVEzVe/view)|e4e|
|[shape_predictor_68_face_landmarks.dat](https://drive.google.com/file/d/1HKmjg6iXsWr4aFPuU0gBXPGR83wqMzq7/view)|PTI|
|[hyperstyle_ffhq.pt](https://drive.google.com/file/d/1C3dEIIH1y8w1-zQMCyx7rDF0ndswSXh4/view)|hyperstyle|
|[hyperstyle_cars.pt](https://drive.google.com/file/d/1WZ7iNv5ENmxXFn6dzPeue1jQGNp6Nr9d/view)|hyperstyle|
|[hyperstyle_afhq_wild.pt](https://drive.google.com/file/d/1OMAKYRp3T6wzGr0s3887rQK-5XHlJ2gp/view)|hyperstyle|
|[afhq_wild_w_encoder.pt](https://drive.google.com/file/d/1MhEHGgkTpnTanIwuHYv46i6MJeet2Nlr/view)|hyperstyle|
|[stylegan2-car-config-f.pt](https://drive.google.com/file/d/1UmMHHB3DU1trTB8_9Fjkck5ZwArnD81B/view)|hyperstyle|
|[afhqwild.pt](https://drive.google.com/file/d/1z6IVVaCJuFTksKwp1CM3emWOVHbrBip-/view)|hyperstyle|
|[ffhq_cartoon_blended.pt](https://drive.google.com/file/d/1r3XVCt_WYUKFZFxhNH-xO2dTtF6B5szu/view)|hyperstyle|
|[pixar.pt](https://drive.google.com/file/d/1trPW-To9L63x5gaXrbAIPkOU0q9f_h05/view)|hyperstyle|
|[CurricularFace_Backbone.pth](https://drive.google.com/file/d/1f4IwVa2-Bn9vWLwB-bUwm53U_MlvinAj/view)|hyperstyle|
|[mtcnn.tar.gz](https://drive.google.com/file/d/1tJ7ih-wbCO6zc3JhI_1ZGjmwXKKaPlja/view)|hyperstyle|
|[ResNet-34 Model](https://github.com/yuval-alaluf/hyperstyle)|hyperstyle|


