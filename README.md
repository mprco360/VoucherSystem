# 🎟️ Voucher Management API

A lightweight serverless API to manage exam discount vouchers per organization and exam. Built using AWS Lambda, API Gateway, and DynamoDB.

---

## 📘 Base URL

```
https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod
```

---

## 📌 Features

- ✅ **Create** vouchers with discount, expiry date, and quantity
- 🔍 **Fetch** vouchers for a specific organization or exam
- 🛡️ **Validate** voucher codes and calculate discounted price

---

## 🚀 Endpoint: `/vouchers` (GET)

This single endpoint supports different operations via the `type` query parameter.

| Parameter   | Type    | Required | Description |
|-------------|---------|----------|-------------|
| `type`      | string  | ✅ Yes   | Operation type: `create`, `get`, `validate` |
| `orgName`   | string  | ❌ No    | Organization name (used in `create` and `get`) |
| `orgId`     | string  | ❌ No    | Organization ID (used in `create` and `get`) |
| `examName`  | string  | ❌ No    | Exam name (used in `create` and `get`) |
| `examId`    | string  | ❌ No    | Exam ID (used in `create` and `get`) |
| `discount`  | integer | ❌ No    | Discount percentage (used in `create`) |
| `expiryDate`| string  | ❌ No    | Expiry date in `MM-DD-YYYY` format (used in `create`) |
| `nVouchers` | integer | ❌ No    | Number of vouchers to generate (used in `create`) |
| `voucherId` | string  | ❌ No    | Voucher ID to validate (used in `validate`) |
| `price`     | float   | ❌ No    | Original price to apply discount (used in `validate`) |

---

## 📥 Example Requests

### 🔧 Create Vouchers

```bash
curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=create&orgName=abc&orgId=123&examName=test&examId=test123&discount=10&expiryDate=10-09-2025&nVouchers=5'
```

### 📄 Fetch Vouchers

```bash
curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=get&orgName=abc&examName=test'
```

You can also use `orgId` and `examId` instead of `orgName` and `examName`.

### 🧾 Validate Voucher

```bash
curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=validate&voucherId=9F6AA494'
```

### 💰 Validate Voucher With Price

```bash
curl --location 'https://npnc11v0y5.execute-api.us-east-1.amazonaws.com/Prod/vouchers?type=validate&voucherId=9F6AA494&price=150.0'
```

> If valid and not expired, you’ll receive the discounted price.

---

## 📤 Sample Responses

### ✅ 200 OK

```json
{
  "message": "Operation completed successfully"
}
```

Or (for validation):

```json
{
  "valid": true,
  "original_price": 150.0,
  "discount_percent": 10,
  "discounted_price": 135.0,
  "expires_on": "10-09-2025"
}
```

### ❌ 400 Bad Request

```json
{
  "error": "Missing required parameters: type"
}
```

### ❌ 500 Internal Server Error

```json
{
  "error": "An unexpected error occurred"
}
```

---

## 🧱 DynamoDB Schema (Example)

| Attribute     | Type    | Notes                     |
|---------------|---------|---------------------------|
| `voucherId`   | String  | Partition key             |
| `orgName`     | String  | Optional                  |
| `orgId`       | String  | Optional                  |
| `examName`    | String  | Optional                  |
| `examId`      | String  | Optional                  |
| `discount`    | Number  | Discount %                |
| `expiryDate`  | String  | MM-DD-YYYY                |
| `maxUsers`    | Number  | How many times it can be used |
| `used`        | Number  | Counter                   |
| `createdAt`   | String  | ISO timestamp             |

---

## 🛠️ Tech Stack

- AWS API Gateway + Lambda (Python or Node.js)
- DynamoDB for storage
- Optional: SAM or Serverless Framework for deployment



---

## 🧑‍💻 Maintainer

> Made with 💡 by your friendly backend engineer.

---

## 📄 License

MIT License
