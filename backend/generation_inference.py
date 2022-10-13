import torch
from arguments import *
from transformers import PreTrainedTokenizerFast, GPT2Config, GPT2LMHeadModel

# 인퍼런스 설정
args = GenerationDeployArguments(
    pretrained_model_name="skt/kogpt2-base-v2",
    downstream_model_dir="../Data/모델/생성기/checkpoint-generation",
)

# 토크나이저 로드
tokenizer = PreTrainedTokenizerFast.from_pretrained(
    args.pretrained_model_name,
    eos_token="</s>",
)

# 모델 로드

# model = torch.load('../Data/모델/top3/3total_model')

# model = GPT2LMHeadModel.from_pretrained(
#     args.pretrained_model_name,
# )

pretrained_model_config = GPT2Config.from_pretrained(
    args.pretrained_model_name,
)

model = GPT2LMHeadModel(pretrained_model_config)

fine_tuned_model_ckpt = torch.load(
    args.downstream_model_checkpoint_fpath,
    map_location=torch.device("cpu"),
)


# 체크포인트 읽기
model.load_state_dict({k.replace("model.", ""): v for k,
                      v in fine_tuned_model_ckpt['state_dict'].items()})

# 평가 모드 전환
model.eval()

# 인퍼런스 설정


def inference_fn(
    prompt,
    min_length=20,
    max_length=30,
    top_p=0.8,
    top_k=30,
    repetition_penalty=1.5,
    no_repeat_ngram_size=3,
    temperature=0.9
):
    try:
        # generated_sentence = """성공입니다."""
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        print("start")
        print("prompt: ", prompt)
        with torch.no_grad():
            generated_ids = model.generate(
                input_ids,
                do_sample=True,
                min_length=int(min_length),
                max_length=int(max_length),
                top_p=float(top_p),
                top_k=int(top_k),
                repetition_penalty=float(repetition_penalty),
                no_repeat_ngram_size=int(no_repeat_ngram_size),
                temperature=float(temperature),
            )
        generated_sentence = tokenizer.decode(
            [el.item() for el in generated_ids[0]])
        print("generated_sentence:", generated_sentence)
    except Exception as e:
        # generated_sentence = """처리 중 오류가 발생했습니다. <br>
        #   변수의 입력 범위를 확인하세요. <br><br>
        #   min_length: 1 이상의 정수 <br>
        #   max_length: 1 이상의 정수 <br>
        #   top-p: 0 이상 1 이하의 실수 <br>
        #   top-k: 1 이상의 정수 <br>
        #   repetition_penalty: 1 이상의 실수 <br>
        #   no_repeat_ngram_size: 1 이상의 정수 <br>
        #   temperature: 0 이상의 실수
        #   """
        generated_sentence = """실패했습니다."""
        print("eeeeeeeeeeee", e)
    return {
        'result': generated_sentence,
    }
