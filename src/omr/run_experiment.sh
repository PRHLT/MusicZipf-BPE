#/bin/bash

# 1. Create model
pylaia-htr-create-model --config Models/EIN_bpe-1-5-inter/config/model_config.yaml

# 2. Train model 
pylaia-htr-train-ctc --config Models/EIN_bpe-1-5-inter/config/train_config.yaml

# 3. Evaluate resulting model
# Decode test set
pylaia-htr-decode-ctc -- config Models/EIN_bpe-1-5-inter/config/decode_config.yaml > \
    Models/EIN_bpe-1-5-inter/hyps/test_hyp.txt
# Run metrics
python3 compute_cer.py \
    -hyp Models/EIN_bpe-1-5-inter/hyps/test_hyp.txt \
    -ref ../data/lines/transcriptions/bpe/EIN_test_gt_inter_bpe-1-5.txt > \
    Models/EIN_bpe-1-5-inter/results/test_cer.txt
    