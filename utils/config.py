import torch
from torchvision import transforms
from Model.GaussianDiffusion import GaussianDiffusion


class DefaultConfig(object):
    # 初始化参数
    batch_size = 4
    timesteps = 1000
    image_size = 128
    crop_height = 128
    crop_width = 256
    scale = (crop_height, crop_width)
    num_workers = 1
    lr = 5e-4
    learning_rate_decay=0.98
    data = 'data'
    dataset = 'dataset'
    log_dirs = 'Log'
    save_have_model_path = 'Log/trainning_log/model_train_have'
    save_no_model_path = 'Log/trainning_log/model_train_no'
    in_channels = 3
    model_channels = 96
    out_channels = 3
    channel_mult = (1, 2, 2)
    attention_resolutions = []
    img_output_dir = 'Log/trainning_log/img_output'
    # 前向加噪（使用高斯噪声）
    gaussian_diffusion = GaussianDiffusion(timesteps=timesteps)
    # 定义处理方式
    transform = transforms.Compose([
        transforms.Resize(image_size),
        transforms.CenterCrop(image_size),
        transforms.PILToTensor(),
        transforms.ConvertImageDtype(torch.float),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
    ])

    weights = torch.tensor([0.299, 0.587, 0.114]).view(1, 1, 1, 3)
    # 检查系统上是否有可用的GPU设备
    if torch.cuda.is_available():
        # 设置要使用的GPU设备为GPU 0（如果只有一个GPU）
        device = torch.device("cuda:0")
        print("使用的GPU设备:", torch.cuda.get_device_name(device))
    else:
        device = torch.device("cpu")
        print("没有可用的GPU，将使用CPU")
