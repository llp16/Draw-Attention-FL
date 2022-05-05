# Be Bad and Draw Attention
This project is based on the Oort framework(https://github.com/SymbioticLab/Oort.git), a utility based participant selection method.

# Overview

* [Environment Setting](#environment-setting)
* [Reproduce Results](#reproduce-results)

# Environment Setting
You can run ```install.sh``` to setup the envrionment for this project.

# Reproduce Results 

1. Download HAR dataset which can be found on [FedScale](https://github.com/SymbioticLab/FedScale). 


2. You can modify the configuration file to personalize the experiment setting, the cofig file can be found in `evals/configs/har/`.

3. Execute the experiment through the command below(The size of HAR dataset is enormous, you may need serveral hours to reproduce the eperiment result, which highly depends on your device's computing power):
``` bash
cd Draw_Attention_FL/training/evals
python manager.py submit configs/har/conf_oort.yml
```

4. The training results would be print in the log file, the path can be specified in config file.

