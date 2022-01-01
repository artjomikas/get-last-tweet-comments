import requests
from random_username.generate import generate_username

def create_url(id):
    tweet_fields = "&max_results=100&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id"
    url = f"https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{id}{tweet_fields}"
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()

def create_txt_file(json_response):
    data = json_response["data"]
    list_of_ids = []
    for id in data:
        list_of_ids.append(id["id"])
    f = open('generated_links.txt', 'w')
    list_of_usernames = generate_username(100)
    for item in range(len(list_of_ids)):
        f.write("https://twitter.com/" + list_of_usernames[item] + "/status/" + "%s\n" % list_of_ids[item])

def main():
    bearer_token = "ENTER YOUR BEARER TOKEN"
    tweet_id = "ENTER TWEET ID"
    url = create_url(tweet_id)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    create_txt_file(json_response)
    print("Created file: generated_links.txt")

if __name__ == "__main__":
    main()
