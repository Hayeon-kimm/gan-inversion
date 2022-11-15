dataset_paths = {
	#  Face Datasets (In the paper: FFHQ - train, CelebAHQ - test)
	'ffhq': '/home/sosick377/Datasets/FFHQ/00000',
 	#'ffhq': '/data/my_data/1.jpg',
	#'celeba_test': 'data/my_data/1.jpg',
 	'celeba_test': '/home/sosick377/Datasets/CelebA/img_align_celeba/img_align_celeba',

	#  Cars Dataset (In the paper: Stanford cars)
	'cars_train': '',
	'cars_test': '',

	#  Horse Dataset (In the paper: LSUN Horse)
	'horse_train': '',
	'horse_test': '',

	#  Church Dataset (In the paper: LSUN Church)
	'church_train': '',
	'church_test': '',

	#  Cats Dataset (In the paper: LSUN Cat)
	'cats_train': '',
	'cats_test': ''
}

model_paths = {
	'stylegan_ffhq': '/workspace/pretrained_models/stylegan2-ffhq-config-f.pt',
	'ir_se50': '/workspace/pretrained_models/model_ir_se50.pth',
	'shape_predictor': '/workspace/pretrained_models/shape_predictor_68_face_landmarks.dat',
	'moco': '/workspace/pretrained_models/moco_v2_800ep_pretrain.pt'
}
