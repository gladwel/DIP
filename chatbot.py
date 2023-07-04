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
    file_prefix = 'test_task_'
    existing_files = len([filename for filename in os.listdir('.') if filename.startswith(file_prefix)])

    # create the new filename
    new_filename = f'{file_prefix}{existing_files + 1}.md'

    # write the string to the new file
    with open(new_filename, 'w') as file:
        file.write(string_to_save)



# response = openai.ChatCompletion.create(
#   model="gpt-4",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": """The thesis aims to develop a personalized system that summarizes proposals related to decentralized autonomous organizations (DAO) governance, with the goal of increasing accessibility and participation in the decision-making process. The research will explore different summarization approaches, including abstractive and extractive summarization, and determine the most effective machine learning-based method for summarizing complex documents related to DAO governance. As a thesis byproduct, a dataset containing text summarization will be produced.
# - Conduct a thorough review of the existing literature on DAO, their governance structures, and the decision-making processes involved.
# - Identify the current challenges and limitations related to summarizing proposals related to DAO governance, and how they impact accessibility and participation in the decision-making process.
# - Evaluate different summarization approaches, such as abstractive and extractive summarization, and determine their advantages and disadvantages in the context of DAO governance proposals.
# - Determine the criteria for evaluating the effectiveness of a summarization system for DAO governance proposals, such as accuracy, comprehensibility, and relevance.
# - Develop a customized system for summarizing DAO governance proposals that address the limitations of existing approaches and meet the identified criteria for effectiveness.
# - Test the system on a sample of DAO governance proposals, and evaluate its effectiveness using the identified criteria.
# - Compare the results of the customized machine learning-based system with existing approaches to summarize DAO governance proposals to demonstrate the improvements in accessibility and participation in the decision-making process.
# - Draw conclusions from the research and recommend future research areas to improve DAO governance proposals' summarization further.
#
# I have following outline for it:
# 1. Introduction
#  1.1 Motivation
#  1.2 Problem statement
#  1.3 Goals of the dissertation thesis
#  1.4 Structure of thesis
#
# 2. Background and literature review
#  2.1 Overview of DAOs
#  2.2 Governance structures and decision-making processes in DAOs
#  2.3 Challenges and limitations related to summarizing DAO governance proposals
#  2.4 The impact of summarization on accessibility and participation in the decision-making process
#
# 3. Methodology
#  3.1 Research design
#  3.2 Data collection and preprocessing
#  3.3 Machine learning-based summarization approaches
#   3.3.1 Overview of different summarization approaches, including abstractive and extractive summarization
#   3.3.2 Analysis of the advantages and disadvantages of each approach in the context of DAO governance proposals
#  3.4 Criteria for evaluating the effectiveness of summarization system
#  3.5 Development of customized summarization system
#  3.6 Testing and evaluation methodology
#
# 4. Results and Discussion
#  4.1 Description of the dataset used for the research
#  4.2 Development of a personalized system for summarizing DAO governance proposals
#   4.2.1 System overview
#   4.2.2 System architecture
#  4.3 Evaluation of the system's effectiveness using identified criteria
#  4.4 Comparison of results with existing summarization approaches
#    (to demonstrate improvements in accessibility and participation in the decision-making process)
#  4.5 Interpretation and discussion of the results
#  4.6 Discussion of the advantages and limitations of the developed system
#    4.6.1 Explanation of how the system addresses limitations of existing approaches and meets criteria for effectiveness
#    4.6.2 Analysis of potential limitations and opportunities for improvement in the system
#    4.6.3 Analysis of the practical implications of the research findings on DAO governance and decision-making processes
#
# 5. Conclusion and Future Work
#   5.1 Summary of the research objectives, methods, and key findings
#   5.2 Implications and contributions of the study to the field of DAO governance and summarization
#   5.3 Discussion of the limitations and future research directions
#   5.4 Conclusion and final remarks on the research outcomes
#   5.5 Recommendations for improving the summarization of DAO governance proposals
#
# Describe in detail the problem statement for this thesis"""},
#         {"role": "assistant", "content": """The problem statement for this thesis is the lack of accessibility and participation in the decision-making process of decentralized autonomous organizations (DAOs) due to the complexity of governance proposals. DAOs are decentralized entities that operate based on smart contracts and blockchain technology, and their decision-making process is based on a consensus mechanism where stakeholders participate in decision-making by voting on proposals. However, governance proposals related to DAOs can be complex and lengthy, which can hinder stakeholders' ability to access and participate in the decision-making process.
#
# The problem is further compounded by the limited availability of tools and techniques for summarizing complex DAO governance proposals effectively. Extracting key information and summarizing it in a concise and understandable way can help increase accessibility and participation in the decision-making process, but existing summarization approaches may not be suitable for DAO governance proposals. Therefore, there is a need for a personalized system that can effectively summarize DAO governance proposals, increasing accessibility and participation in the decision-making process. This thesis aims to address this problem by developing and evaluating a customized machine learning-based system for summarizing DAO governance proposals."""},
#         {"role": "user", "content": "Write goals of the dissertation thesis"},
#         {"role": "assistant", "content": """The thesis aims to contribute to the field of DAO governance and decision-making processes by developing a personalized system for summarizing proposals that can increase accessibility and participation in the decision-making process.
# The goals of the dissertation thesis are:
# To explore the current state of decentralized autonomous organizations (DAOs), their governance structures, and the decision-making processes involved.
# To identify the challenges and limitations related to summarizing proposals related to DAO governance and how they impact accessibility and participation in the decision-making process.
# To evaluate different summarization approaches, such as abstractive and extractive summarization, and determine their advantages and disadvantages in the context of DAO governance proposals.
# To determine the criteria for evaluating the effectiveness of a summarization system for DAO governance proposals, such as accuracy, comprehensibility, and relevance.
# To develop a customized system for summarizing DAO governance proposals that addresses the limitations of existing approaches and meets the identified criteria for effectiveness.
# To test the system on a sample of DAO governance proposals and evaluate its effectiveness using the identified criteria.
# To compare the results of the customized machine learning-based system with existing approaches to summarize DAO governance proposals to demonstrate the improvements in accessibility and participation in the decision-making process.
# To draw conclusions from the research and recommend future research areas to improve DAO governance proposals' summarization further.
# """},
#         {"role": "user", "content": "Write the structure of the thesis"},
#
#     ]
# )

response = openai.ChatCompletion.create(
  model="gpt-4",
  max_tokens = 2000,
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": """I have the following test assignment for hiring:

Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

This test will qualify you to be a python developer. Use the easiest path to the goal."""},
        {"role": "user", "content": "Write detailed instructions with code on how to make it for me step by step. I prefer windows, PyCharm IDE, Flask."},
    ]
)['choices'][0]['message']['content']


print(response)
save_string_to_file(response)
