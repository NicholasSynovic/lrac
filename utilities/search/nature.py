from datetime import datetime
from string import Template
from typing import List
from webbrowser import open


def main() -> None:
    urlTemplate: Template = Template(
        template="https://www.nature.com/search?q=${query}&order=date_desc&article_type=research&date_range=${year}-${year}"
    )
    queries: List[str] = [
        r'"Deep Learning"',
        r'"Deep Neural Networks"',
        r'"Hugging Face"',
        r'"HuggingFace"',
        r'"Pre-Trained Model"',
    ]
    years: List[int] = list(range(2015, datetime.now().year))

    query: str
    year: int
    for query in queries:
        for year in years:
            open(url=urlTemplate.substitute(query=query, year=year))


if __name__ == "__main__":
    main()
