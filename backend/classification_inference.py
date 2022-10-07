import torch
from arguments import *
from transformers import BertTokenizer, BertConfig, BertForSequenceClassification

# 인퍼런스 설정
args = ClassificationDeployArguments(
    pretrained_model_name="beomi/kcbert-base",
    downstream_model_dir="../Data/모델/분류기/checkpoint-doccls",
    max_seq_length=128,
)

# 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained(
    args.pretrained_model_name,
    do_lower_case=False,
)

# 토크나이저 로드
fine_tuned_model_ckpt = torch.load(
    args.downstream_model_checkpoint_fpath,
    map_location=torch.device("cpu")
)

# BERT 설정 로드
pretrained_model_config = BertConfig.from_pretrained(
    args.pretrained_model_name,
    num_labels=fine_tuned_model_ckpt['state_dict']['model.classifier.bias'].shape.numel(
    ),
)

# BERT 모델 초기화
model = BertForSequenceClassification(pretrained_model_config)

# 체크포인트 읽기
model.load_state_dict({k.replace("model.", ""): v for k,
                      v in fine_tuned_model_ckpt['state_dict'].items()})

# 평가 모드 전환
model.eval()

# 인퍼런스 설정


def inference_fn2(sentence):
    inputs = tokenizer(
        [sentence],
        max_length=args.max_seq_length,
        padding="max_length",
        truncation=True,
    )
    with torch.no_grad():
        outputs = model(**{k: torch.tensor(v) for k, v in inputs.items()})
        prob = outputs.logits.softmax(dim=1)
        # positive_prob = round(prob[0][1].item(), 4)
        # negative_prob = round(prob[0][0].item(), 4)
        pred = "과학" if torch.argmax(
            prob) == 1 else "소설" if torch.argmax(prob) == 0 else "인문"
    return {
        'sentence': sentence,
        'prediction': pred,
        # 'positive_data': f"긍정 {positive_prob}",
        # 'negative_data': f"부정 {negative_prob}",
        # 'positive_width': f"{positive_prob * 100}%",
        # 'negative_width': f"{negative_prob * 100}%",
    }
