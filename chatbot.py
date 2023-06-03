import os
import openai

openai.organization = "org-RAUgpYO6HKSPQCszhrY71FA6"
os.environ[
    "OPENAI_API_KEY"] = "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"  # openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")


# print(openai.Model.list())

def _trimmed_fetch_response(resp, n):
    if n == 1:
        return resp.choices[0].text.strip()
    else:
        print('_trimmed_fetch_response :: returning {0} responses from GPT-3'.format(n))
        texts = []
        for idx in range(0, n):
            texts.append(resp.choices[idx].text.strip())
        return texts


async def cleaned_completion(prompt, engine="ada", max_tokens=64, temperature=0.7, top_p=1, stop=None,
                             presence_penalty=0, frequency_penalty=0, echo=False, n=1, stream=False, logprobs=None,
                             best_of=1, logit_bias={}):
    '''
    Wrapper for OpenAI API completion. Returns whitespace trimmed result from GPT-3.
    '''
    resp = openai.Completion.create(prompt,
                                    engine=engine,
                                    max_tokens=max_tokens,
                                    temperature=temperature,
                                    top_p=top_p,
                                    presence_penalty=presence_penalty,
                                    frequency_penalty=frequency_penalty,
                                    echo=echo,
                                    stop=stop,
                                    n=n,
                                    stream=stream,
                                    logprobs=logprobs,
                                    best_of=best_of,
                                    logit_bias=logit_bias)
    return _trimmed_fetch_response(resp, n)

def save_string_to_file(string_to_save):
    # get the number of existing files
    file_prefix = 'fast_file_'
    existing_files = len([filename for filename in os.listdir('.') if filename.startswith(file_prefix)])

    # create the new filename
    new_filename = f'{file_prefix}{existing_files + 1}.cpp'

    # write the string to the new file
    with open(new_filename, 'w') as file:
        file.write(string_to_save)


print(response)
save_string_to_file(response)
