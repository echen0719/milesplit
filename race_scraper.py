import requests
import re

# example
race_stats = f"https://nj.milesplit.com/meets/638228-penn-relays-qualifier-2025/results/1134430?type=raw"
request = requests.get(race_stats)

if request.status_code == 200:
    race = request.text.split("<pre>")[1].split("</pre>")[0]
    # example text<pre>hi there</pre>more example text
    # ['example text', 'hi there </pre> more example text'] --> index 1
    # ['hi there', 'more example text] --> index 0
    # result is 'hi there'

    content = '\n'.join([line.strip() for line in race.splitlines()])
    # https://stackoverflow.com/questions/31218253/trim-whitespace-from-multiple-lines
    # really helped me

    with open("hi.txt", mode='w') as file:
            file.write(content)

else:
    print(f"Try Again. Something wrong. Status Code: {request.status_code}")
    exit()