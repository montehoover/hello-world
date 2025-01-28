from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


# Setup model and tokenizer
name = "gradientai/Llama-3-8B-Instruct-262k"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name).eval()


# Pass in text
input_text = "Once upon a time there was a magic dragon and a brave knight. They had many adventures together "
input_ids = tokenizer(input_text, return_tensors="pt").input_ids
with torch.no_grad():
    outputs = model(input_ids, use_cache=True)

past_key_values = outputs.past_key_values


# Pass in more text
next_input_text = "and lived happily ever"
next_input_ids = tokenizer(next_input_text, return_tensors="pt").input_ids
attention_mask = torch.ones_like(input_ids)  # shape: [batch_size, seq_len]
next_attention_mask = torch.ones_like(next_input_ids)
combined_attention_mask = torch.cat([attention_mask, next_attention_mask], dim=1)
generated_outputs = model.generate(
    next_input_ids,
    max_new_tokens=4,
    past_key_values=past_key_values,
    attention_mask=combined_attention_mask,
    return_dict_in_generate=True,
    output_attentions=True,
)


# Look at the output
generated_ids = generated_outputs.sequences
generated_text = tokenizer.decode(generated_ids[0])
print(generated_text)
