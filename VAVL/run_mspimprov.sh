
audio_model_type=wav2vec2-large-robust

model=AuxFormer

corpus=MSP-IMPROV
num_classes=att #four or ALL
output_num=3
label_rule=D       #P, M, D
partition_number=6
data_mode=primary #primary or secondary
seed=0
label_type=dimensional
label_learning=hard-label


corpus_type=${corpus}_${num_classes}_${data_mode}

# Training
python -u train.py \
--device            cuda \
--model_type        $audio_model_type \
--lr                .05e-3 \
--corpus_type       $corpus_type \
--seed              $seed \
--epochs            20 \
--batch_size        9 \
--hidden_dim        1024 \
--num_layers        2 \
--output_num        $output_num \
--label_type        $label_type \
--label_learning    $label_learning \
--corpus            $corpus \
--num_classes       $num_classes \
--label_rule        $label_rule \
--partition_number  $partition_number \
--data_mode         $data_mode \
--model_path        model/${model_type}/${corpus_type}/${label_type}/${label_learning}/${data_mode}/${label_rule}/${model}/partition${partition_number}/seed_${seed}

# Evaluation
# python -u test.py \
# --device            cuda \
# --model_type        $audio_model_type \
# --corpus_type       $corpus_type \
# --seed              $seed \
# --batch_size        1 \
# --hidden_dim        1024 \
# --num_layers        2 \
# --output_num        $output_num \
# --label_type        $label_type \
# --label_learning    $label_learning \
# --corpus            $corpus \
# --num_classes       $num_classes \
# --label_rule        $label_rule \
# --partition_number  $partition_number \
# --data_mode         $data_mode \
# --model_path        model/${model_type}/${corpus_type}/${label_type}/${label_learning}/${data_mode}/${label_rule}/${model}/partition${partition_number}/seed_${seed}


