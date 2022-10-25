import json
import math
import sys
from datetime import datetime


def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points. Dict: { start node : {end node: distance} } """
    distances = {}
    print(locations)
    for from_place in locations:
        distances[from_place] = {}
        for to_place in locations:
            if from_place == to_place:
                distances[from_place][to_place] = None
            else:
                # Euclidean distance
                distances[from_place][to_place] = round(math.hypot((locations[from_place][0] - locations[to_place][0]),
                                                                   (locations[from_place][1] - locations[to_place][1])), 2)

    # origin_place = list(distance.keys())[0]
    # for to_node in distances[origin_place]:
    #     if distances[origin_place][to_node] is not None and distances[origin_place][to_node] < min_dist:
    #         min_node = to_node
    #         min_dist = distances[0][to_node]
    return distances


def find_next_minimum(distance_matrix, nodes_visited):
    """" find the next best node given """
    min_dist = sys.maxsize * 2 + 2
    prev_node = nodes_visited[-1]

    next_node = -1
    # if len(distance_matrix) ==1:
    #     next_node = to_place

    # find next node
    for to_place in distance_matrix[prev_node]:
        if distance_matrix[prev_node][to_place] != None and distance_matrix[prev_node][to_place] < min_dist:
            next_node = to_place
            min_dist = distance_matrix[prev_node][to_place]

    # removal of visited nodes
    distance_matrix_keys = distance_matrix.keys()
    distance_matrix.pop(prev_node)
    for a_node in distance_matrix_keys:
        if prev_node in nodes_visited:
            distance_matrix[a_node].pop(prev_node)

    nodes_visited.append(next_node)
    return distance_matrix, nodes_visited


def lambda_handler(event, context):
    # TODO implement
    received_locations = json.loads(event["Records"][0]["body"])["locations"]
    print("locations", received_locations)
    nodes_count = len(received_locations)
    origin_place = list(received_locations.keys())[0]
    distance_matrix = compute_euclidean_distance_matrix(received_locations)
    nodes_visited = [origin_place]
    # print("initial distance_matrix", distance_matrix)
    # print("inital nodes_visited", nodes_visited)
    while nodes_count != len(nodes_visited):
        distance_matrix, nodes_visited = find_next_minimum(
            distance_matrix, nodes_visited)
        # print("distance_matrix", distance_matrix)
        print("nodes_visited", nodes_visited)

    route = [i for i in nodes_visited]
    print(json.dumps(route))
    return {
        'statusCode': 200,
        'body': json.dumps(route)
    }


event = {
    "Records": [
        {
            "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
            "receiptHandle": "MessageReceiptHandle",
            "body": "{\"locations\": {\"singapore management university\": [103.85199000000006, 1.2962000000000558], \"Singapore Sports Hub\": [103.87218000000007, 1.3045900000000756], \"aperia mall\": [103.86484000000007, 1.310890000000029], \"boruda climbing\": [-123.95563999999996, 45.31890000000004], \"Stickies @ dhoby ghaut\": [100.30866000000003, 5.411650000000066]}}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1523232000000",
                "SenderId": "123456789012",
                "ApproximateFirstReceiveTimestamp": "1523232000001"
            },
            "messageAttributes": {},
            "md5OfBody": "{{{md5_of_body}}}",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
            "awsRegion": "us-east-1"
        }
    ]
}

lambda_handler(event, None)
