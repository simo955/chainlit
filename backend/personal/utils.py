def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def dataframe_to_string(df):
    return df.to_string()


def create_prompt(file_content, df_string):
    prompt = {
        "content": f" ** PROMPT ** \n {file_content} \n\n {df_string}",
        "role": "system",
    }
    return prompt
