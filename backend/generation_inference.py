import torch
from arguments import *
from transformers import PreTrainedTokenizerFast, GPT2Config, GPT2LMHeadModel

# 인퍼런스 설정
args = GenerationDeployArguments(
  pretrained_model_name="skt/kogpt2-base-v2",
  downstream_model_dir="../Data/모델/사피엔스/checkpoint-generation",
)

# 토크나이저 로드
tokenizer = PreTrainedTokenizerFast.from_pretrained(
  args.pretrained_model_name,
  eos_token="</s>",
)

model = torch.load('../Data/모델/사피엔스/Sapiens.pt')
model.eval()

model = GPT2LMHeadModel.from_pretrained(
  args.pretrained_model_name,
)

def inference_fn(
  prompt,
  min_length=10,
  max_length=20,
  top_p=1.0,
  top_k=50,
  repetition_penalty=1.0,
  no_repeat_ngram_size=0,
  temperature=1.0
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
    generated_sentence = tokenizer.decode([el.item() for el in generated_ids[0]])
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
  