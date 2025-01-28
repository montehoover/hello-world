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
    outputs = model(input_ids)

# The kv_cache:
past_key_values = outputs.past_key_values


# Demonstrate using a kv_cache and getting out attention scores.
# Note that even with the kv_cache, we still need to pass in the original input ids.
# Internally the model uses the kv_cache to avoid recomputing the original attention scores.
next_input_text = "and lived happily ever "
new_input_ids = tokenizer(input_text + next_input_text, return_tensors="pt").input_ids

generated_outputs = model.generate(
    new_input_ids,
    max_new_tokens=10,
    past_key_values=past_key_values,
    return_dict_in_generate=True,
    output_attentions=True,
)


# Look at the output
generated_ids = generated_outputs.sequences
generated_text = tokenizer.decode(generated_ids[0])
print(generated_text)

# Attentions are a list of lists of tensors with the following shape:
# [new_tokens, n_layers, batch, n_heads, n_next_input_ids, total_input_ids]
print(generated_outputs.attentions[0][0].shape)
print(generated_outputs.attentions[1][0].shape)
print(generated_outputs.attentions[8][0].shape)
print(generated_outputs.attentions[9][0].shape)
