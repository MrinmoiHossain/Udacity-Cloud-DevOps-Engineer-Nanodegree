import json
import decimal

def lambda_handler(event, context):
    print(event)
    
    # check that the request has some input body
    if 'body' in event:
        event = json.loads(event["body"])
    
    # get amount value
    amount = float(event["amount"])
    
    ## calculate the resultant change and store the result
    res = []
    coins = [1, 5, 10, 25] # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}
    
    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem = divmod(int(amount * 100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num: coin_lookup[coin]})

    
    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num: coin_lookup[coin]})
    
    print(res)
    # format the response as JSON and return the result
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"res": res})
    }
    
    return response
