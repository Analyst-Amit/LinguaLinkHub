from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    print("Hello Amit")

    linkedin_profile_url = linkedin_lookup_agent(name="Andrew Ng")

    summary_template = """
    Given the Linkedin information {information} about a person. I want you to create:
    1. A short one line summary.
    2. Two interesting facts about them.

    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    # information = scrape_linkedin_profile()

    output = chain.invoke(input=linkedin_data)

    print(output["text"])
