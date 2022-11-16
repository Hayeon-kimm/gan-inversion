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

```
#[e4e train.py] train 할때마다 new 폴더가 생기므로 새로 학습시에 new 폴더를 삭제(rm -rf new)하고 시작해야합니다.
CUDA_VISIBLE_DEVICES=[gpu_num] python scripts/train.py \
--dataset_type ffhq_encode \
--exp_dir new/experiment/directory \
--start_from_latent_avg \
--use_w_pool \
--w_discriminator_lambda 0.1 \
--progressive_start 20000 \
--id_lambda 0.5 \
--val_interval 10000 \
--max_steps 200000 \
--stylegan_size 512 \
--stylegan_weights pretrained_models/stylegan2-ffhq-config-f.pt \
--workers 8 \
--batch_size 8 \
--test_batch_size 4 \
--test_workers 4 
```

e4e inference는 scripts/inference.py에서 gpu 번호를 변경할 수 있습니다.

```
#[e4e inference.py]
python encoder4editing/scripts/inference.py \
--images_dir=data/my_data \
--save_dir=results \
pretrained_models/e4e_ffhq_encode.pt 
```

```
#[hyperstyle inference.py]
CUDA_VISIBLE_DEVICES=[gpu_num] python scripts/inference.py \
--exp_dir=./experiment \
--checkpoint_path=pretrained_models/hyperstyle_ffhq.pt \
--data_path=./datasets/my_data \
--test_batch_size=4 \
--test_workers=4 \
--n_iters_per_batch=5 \
--load_w_encoder \
--w_encoder_checkpoint_path pretrained_models/faces_w_encoder.pt
```
```
#[run_pti.py]
CUDA_VISIBLE_DEVICES=[gpu_num] python scripts/run_PTI.py
```

```
#[hyperstyle inference.py]
CUDA_VISIBLE_DEVICES=[gpu_num] python scripts/inference.py \
--exp_dir=./experiment \
--checkpoint_path=pretrained_models/hyperstyle_ffhq.pt \
--data_path=./datasets/my_data \
--test_batch_size=4 \
--test_workers=4 \
--n_iters_per_batch=5 \
--load_w_encoder \
--w_encoder_checkpoint_path pretrained_models/faces_w_encoder.pt
```
training/coach_hyperstyle.py에서 self.device로 gpu 변경 가능
```
#[hyperstyle train.py]
python scripts/train.py \
--dataset_type=ffhq_hypernet \
--encoder_type=SharedWeightsHyperNetResNet \
--exp_dir=experiments/hyperstyle \
--workers=8 \
--batch_size=8 \
--test_batch_size=8 \
--test_workers=8 \
--val_interval=5000 \
--save_interval=10000 \
--lpips_lambda=0.8 \
--l2_lambda=1 \
--id_lambda=0.1 \
--n_iters_per_batch=5 \
--max_val_batches=150 \
--output_size=1024 \
--load_w_encoder \
--w_encoder_checkpoint_path pretrained_models/e4e_ffhq_encode.pt \ 
--layers_to_tune=0,2,3,5,6,8,9,11,12,14,15,17,18,20,21,23,24
```



