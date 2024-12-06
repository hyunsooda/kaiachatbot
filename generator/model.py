import json
from llama_cpp import Llama

# portal(O), square(O), api docs, kaia(O), kaia github(O)
# kip(O), governance(O), developer forum(O), kaia scan(O), medium(O)

common_system_prompt_header = """
You are a professional paraphrasing generator. Your task is to rephrase the following example sentences by changing the syntax, but keeping the original meaning intact.
Output format must be as below:
- <generated output 1>
- <generated output 2>
- <generated output 3>
- <generated output N>
Do not add any other stuff except for defined format structure.
Use these sentences as input examples:
"""
common_system_prompt_foot = """
Generate paraphrased at least ten statements per example based on these examples.
You should remember what you have been generated so that you can avoid to generate too similar output duplicately.
You must follow the given output format and do not add your personal input at the end.
"""

portal_intent_prompt = """
1. I want to swap FNSA to KAIA.
2. I'd like to exchange Finschia coin to Kaia coin.
3. How do I trade Finschia asset for Kaia asset?
4. I want to stake my kaia coin and earn reward
"""

square_intent_prompt = """
1. I want to stake KAIA
2. What should I take steps to stake my Kaia coin?
3. How can I see all GC information?
4. Where can I see all GC information?
5. How can I see voting history?
6. Where can I see voting history?
7. Where can I submit my vote?
8. Where can I see voting discussion?
9. Where can I see vote leaderboard?
10. Where can I see vote status?
11. Where can I see tokenmics?
12. Where can I see on-chain transaction statistics?
13. Where can I see on-chain staking statistics and expected APY?
14. Where can I see hot projects?
15. Where can I see KEF(Kaia Ecosystem Fund)/KIF(Kaia Ecosystem Fund)?
16. Where can I see official financial report of Kaia foundation?
"""

kaia_github_intent_prompt ="""
1. Where can I see Kaia source code?
2. Where can I see Kaia SDK code?
3. Where can I see Kaia repository?
4. Where can I see Kaia techincal detail?
"""

kip_intent_prompt ="""
1. Where can I see Kaia improvement proposal?
2. Where can I see new technical idea and suggestion?
3. Where cna I see protocoal change draft?
"""

kaia_intent_prompt ="""
1. Where can I see entire Kaia ecosystem?
2. Where can I see kaia main website?
3. Where can I see main concept of Kaia?
"""

governance_intent_prompt ="""
1. Where can I see Kaia governance discussion?
2. Where can I see Kaia governance forum?
3. Where can I see Kaia governance agenda?
"""

developer_forum_intent_prompt ="""
1. Where can I ask techincal question?
2. I have some technical problems and need a help
3. Kaia node troubleshooting QA
"""

explorer_intent_prompt ="""
1. I want to find on-chain data
2. I have a transaction hash or block hash. I need to search it
3. I need block information
"""

medium_intent_prompt ="""
1. Where can I see Kaia news?
2. Where can I see Kaia ongoing project?
3. Where can I see Kaia new relesae note?
"""

kaia_docs_prompt = """
1. I want to learn how to use Kaia or Ethereum API methods
2. How to run JSON RPC?
3. How to run websoket?
"""

all_prompts = {
        "portal"     : portal_intent_prompt,
        "square"     : square_intent_prompt,
        "github"     : kaia_github_intent_prompt,
        "kip"        : kip_intent_prompt,
        "kaia"       : kaia_intent_prompt,
        "governance" : governance_intent_prompt,
        "devforum"   : developer_forum_intent_prompt,
        "explorer"   : explorer_intent_prompt,
        "medium"     : medium_intent_prompt,
        "docs"       : kaia_docs_prompt
        }

llm = Llama(model_path="Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
            n_gpu_layers=1,
            n_ctx=2048,
            verbose=False)

def make_prompt(intent_prompt):
    return common_system_prompt_header + intent_prompt + common_system_prompt_foot

def test_prompt():
    output = llm(
          make_prompt(portal_intent_prompt),
          # make_prompt(square_intent_prompt),
          max_tokens=50000,
          # stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
          temperature=0.95
          # echo=True # Echo the prompt back in the output
    )
    print(output["choices"][0]["text"])

def generate_rephrased():
    rephrased = {}
    for name, prompt in all_prompts.items():
        output = llm(
                make_prompt(prompt),
                max_tokens=50000,
                temperature=0.95
                )
        generated = output["choices"][0]["text"]
        lines = [line.strip() for line in generated.split('\n') if line.strip().startswith('-')]
        rephrased[name] = lines

    return rephrased

if __name__ == "__main__":
    rephrased = generate_rephrased()
    with open("train.json", "w") as file:
        json.dump(rephrased, file)
