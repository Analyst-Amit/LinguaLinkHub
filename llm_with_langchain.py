from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import person_intel_parser, PersonIntel


def linkedin_summary(name: str) -> PersonIntel:
    print("Hello Amit")

    linkedin_profile_url = linkedin_lookup_agent(name=name)

    summary_template = """
    Given the information {information} about a person. I want you to create:
    1. A short summary.
    2. Two interesting facts about them.
    3. A topic that may interest them.
    4. 2 Creative ice breakers to open a conversation with them.
    \n{format_instructions}

    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # Scrape linkedin profile calls the nebula api which is limited.
    # Inside this function the code is modified to call for a specific gist profile.
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    # information = scrape_linkedin_profile()

    output = chain.invoke(input=linkedin_data)

    print(output["text"])

    return person_intel_parser.parse(output["text"])


if __name__ == "__main__":
    linkedin_summary(name="Andrew Ng")
