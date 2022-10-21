import json
import requests


endpoint = "https://maps.geo.ap-southeast-1.amazonaws.com"
index_name = "LambdaLocationIndex1"
create_index_url = endpoint + "/places/v0/indexes"
search_place_suggestions_url = endpoint + \
    "/places/v0/indexes/" + index_name + "/search/suggestions"

index_json = {
    "DataSource": "Esri",
    "DataSourceConfiguration": {
        "IntendedUse": "SingleUse"
    },
    "Description": "string",
    "IndexName": index_name,
    "Tags": {
        "Tag1": "LambdaLocationCall"
    }
}


def lambda_handler(event, context):
    # TODO implement
    x = requests.post(create_index_url, json=index_json)
    print(x.json())
    return {
        'statusCode': 200,
        'body': json.dumps(x.json())
    }
