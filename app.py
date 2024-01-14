# 将模型导入
from openxlab.model import download
download(model_repo='aitejiu/quant_personal_assistant', output='/home/xlab-app-center/quant_personal_assistant')
download(model_repo='OpenLMLab/InternLM-chat-7b",output='/home/xlab-app-center/internlm-chat-7b')
import os
os.system('pip install 'lmdeploy[all]==v0.1.0'')
os.system('# 量化权重模型
lmdeploy lite auto_awq \
  --model  /home/xlab-app-center/internlm-chat-7b/ \
  --w_bits 4 \
  --w_group_size 128 \
  --work_dir /home/xlab-app-center/quant_personal_assistant ')
os.system('lmdeploy convert  internlm-chat-7b ./quant_output \
    --model-format awq \
    --group-size 128')
os.system('lmdeploy serve gradio ./workspace')
