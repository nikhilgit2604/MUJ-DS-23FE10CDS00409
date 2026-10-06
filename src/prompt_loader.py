import yaml


def load_prompts(
    path="prompts/prompts.yaml"
):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)