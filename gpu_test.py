import torch
print(torch.__version__)
print(f"devices: {torch.cuda.device_count()}")
print(f"devices: {torch.cuda.is_available()}")

if torch.cuda.is_available():


  print(f"GPU Name: {torch.cuda.get_device_name()}")
  print(f"GPU Is Available: {torch.cuda.is_available()}")
else:
  print("GPU is not available")