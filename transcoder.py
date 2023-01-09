# First clone the git repository for transcoder
# in local environment
! git clone https: // github.com/facebookresearch/TransCoder transcoder/
   
# Download the model files (link given in official
# git repository)
! wget https: // dl.fbaipublicfiles.com/transcoder/model_1.pth /
 
 # Since transcoder is implemented in pytorch,
 # we need to install pytorch first
! pip install torch torchvision
 
# Now install other required documentations
! pip install numpy fastBPE Moses Apex libclang submitit six sacrebleu == 1.2.11
 
# Now we run the translate.py file with following arguments:
# src_lang = source language file
# tgt_lang = target language file
# model_path = path of the model which we downloaded above
#  > file.java/cpp/py = file which we want to convert
# the command below may take some time to run
! sudo python transcoder/translate.py - -src_lang java - -tgt_lang python - -model_path model_1.pth > code2.java