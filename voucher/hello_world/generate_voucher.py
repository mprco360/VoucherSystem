import json
import hashlib
import time
from datetime import date
from typing import Union
import boto3
from boto3.dynamodb.conditions import Key

def generate_voucher_code(org_name: str,exam_name: str, discount: int, max_uses: int, expiry_date: Union[date,None], length=8) -> str:
    if expiry_date:
        seed = f"{org_name.strip().upper()}-{exam_name.strip().upper()}-{discount}-{max_uses}-{expiry_date.isoformat()}"
    else:
        seed = f"{org_name.strip().upper()}-{exam_name.strip().upper()}-{discount}-{max_uses}"
    hash_digest = hashlib.sha256(seed.encode()).hexdigest().upper()
    return hash_digest[:length]

table = boto3.resource("dynamodb").Table("Vouchers")

def create_handler(event, context):
    body = json.loads(event['body'])
    org = body.get("orgName")
    exam = body.get("examName")
    discount = int(body.get("discount",0))
    max_redemptions = int(body.get("maxRedemptions", 1))
    expiry_date = body.get("expiryDate",None)
    hash_code = generate_voucher_code(org,exam,discount,max_redemptions,expiry_date)
    created_date = time.time()

    if expiry_date:
        obj_ = {
            'orgName': org,
            'voucherId': hash_code,
            'examName': exam,
            'expiresAt': expiry_date,
            'discount': discount,
            'maxUses': max_redemptions,
            'currUses':0,
            'createdAt':created_date
        }
    else:
        obj_ = {
        'orgName':org,
        'voucherId':hash_code,
        'examName':exam,
        'discount':discount,
        'maxUses':max_redemptions,
        'currUses':0,
        'createdAt':created_date
    }
    table.put_item(Item = obj_)

    return {
        "statusCode": 200,
        "body": json.dumps(
            obj_
        )
    }

def get_handler(event,context):
    body = json.loads(event['body'])
    org_name = body.get("orgName",None)
    exam_name = body.get("examName",None)
    res = []
    if org_name:
        if exam_name:
            res = table.query(
                IndexName="GSI1",
                KeyConditionExpression = Key('orgName').eq(org_name) & Key('examName').eq(exam_name)
            )
        else:
            res = table.query(
                IndexName="GSI1",
                KeyConditionExpression=Key('orgName').eq(org_name)
            )
    else:
        items = table.scan()
        res.extend(items.get("Items",[]))
    res = sorted(res,key = lambda x : x.get("createdAt",0))
    return {
        "statusCode":200,
        "body": json.dumps(res)
    }

def validate_handler(event,context):
    body = json.loads(event['body'])
    voucher_id = body.get("voucherId",None)
    ret = None
    is_redeemable = False
    if voucher_id:
        res = table.get_item(
            Key = {
                "voucherId": voucher_id
            }
        )
        if "Item" in res:
            ret = res["Item"]
            k = ret[0]
            if k["currUsers"] < k["maxUsers"]:
                is_redeemable = True
                response = table.update_item(
                    Key = {
                        "voucherId":voucher_id,
                    },
                    UpdateExpression="SET currUsers = :val",
                    ExpressionAttributeValues={
                        ":val" : k["currUsers"] + 1
                    }
                )
            return {
                "statusCode" : 200,
                "body":json.dumps({
                    "validCoupon":is_redeemable
                })
            }
    return {
        "statusCode": 422,
        "body": json.dumps({
            "validCoupon": is_redeemable
        })
    }

def lambda_handler(event,context):
    body = json.loads(event["body"])
    type_ = body.get("type",None)
    if type_:
        if type_ == "create":
            return create_handler(event,context)
        elif type_ == "get":
            return get_handler(event, context)
        elif type_ == "validate":
            return validate_handler(event,context)
        else:
            return "TypenotFound"
    return {
        "statusCode":400,
        "body":{
            "event": "Missing attribute type"
        }
    }
