from bs4 import BeautifulSoup
import re
import argparse

def extract_data(input_file_path, output_file_path=None):
    with open(input_file_path, "r") as input_file:
        content = input_file.read()

    soup = BeautifulSoup(content, 'html.parser')

    validators = soup.find_all('div', class_=re.compile(r'ListRow_container__\w+'))

    data = []
    for validator in validators:
        address_tag = validator.find('a', class_=re.compile(r'Moniker_link__\w+'))
        if address_tag:
            address = address_tag['href'].split('/')[-1]
            name_tag = validator.find('p', class_=re.compile(r'Moniker_validatorName__\w+'))
            if name_tag:
                name = name_tag.get_text().strip()
                ranking_tag = validator.find('div', class_=re.compile(r'ListRow_rankWrapper__\w+'))
                if ranking_tag:
                    ranking = ranking_tag.find('p').get_text().strip()
                voting_power_tag = validator.find('div', class_=re.compile(r'VotingPower_container__\w+'))
                if voting_power_tag:
                    voting_power_text = voting_power_tag.find('h3').get_text().strip()
                    voting_power = voting_power_text
                cumulative_share_tag = validator.find('div', class_=re.compile(r'CumulativeShare_container__\w+'))
                if cumulative_share_tag:
                    cumulative_share_text = cumulative_share_tag.find('p').get_text().strip()
                    cumulative_share = cumulative_share_text
                voting_participation_tag = validator.find('div', class_=re.compile(r'ListRow_right__\w+'))
                if voting_participation_tag:
                    voting_participation = voting_participation_tag.find('span').get_text().strip()
                data.append((name, address, ranking, voting_power, cumulative_share, voting_participation))

    if output_file_path:
        with open(output_file_path, "w") as output_file:
            output_file.write("Name;Address;Ranking;Voting Power;Cumulative Share;Voting Participation\n")
            for record in data:
                output_file.write(";".join(map(str, record)) + "\n")
        print("Data saved to:", output_file_path)
    else:
        print("Name;Address;Ranking;Voting Power;Cumulative Share;Voting Participation")
        for record in data:
            print(";".join(map(str, record)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract JunoValidator data.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("-o", "--output_file", help="Path to the output file.")
    args = parser.parse_args()

    input_file_path = args.input_file
    output_file_path = args.output_file

    extract_data(input_file_path, output_file_path)

